#!/usr/bin/env python3
# -*- coding: utf-8, vim: expandtab:ts=4 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from argparse import Namespace
from enum import Enum

from libmonty_artnet.packets.base import ArtNetBasePacket
from libmonty_artnet.protocol import constants
from libmonty_artnet.protocol.op_codes import OP_POLL
from libmonty_artnet.protocol.diag_priority_codes import DiagPriorityCode
from libmonty_artnet.utils import common_args, network


class DiagnosticsMethod(Enum):
    BROADCAST = 'broadcast'
    UNICAST = 'unicast'


class ArtPollPacket(ArtNetBasePacket):

    subcommand = 'poll'

    @classmethod
    def create_subparser(cls, add_to_subparsers) -> None:
        parser = add_to_subparsers.add_parser(
            cls.subcommand,
            help='ArtPoll'
        )

        common_args.ip_address(parser)
        common_args.ip_port(parser, default=constants.DEFAULT_IP_PORT)

    @staticmethod
    def process_args(args: Namespace) -> None:
        packet = ArtPollPacket()
        network.udp_send(args.ip, args.port, packet.compose())

    def __init__(self,
                 targeted_mode: bool = False,
                 target_port_bottom: int = constants.PORT_ADDRESS_MIN,
                 target_port_top: int = constants.PORT_ADDRESS_MAX,

                 vlc_transmission: bool = True,

                 send_diagnostics: bool = False,
                 diagnostics_method: DiagnosticsMethod = DiagnosticsMethod.BROADCAST,
                 diag_priority: DiagPriorityCode = DiagPriorityCode.DpLow,

                 reply_on_cond_change: bool = False
                 ) -> None:

        self._targeted_mode = targeted_mode
        self._target_port_bottom = target_port_bottom
        self._target_port_top = target_port_top

        self._vlc_transmission = vlc_transmission

        self._send_diagnostics = send_diagnostics
        self._diagnostics_method = diagnostics_method
        self._diag_priority = diag_priority

        self._reply_on_cond_change = reply_on_cond_change

    @property
    def op_code(self) -> int:
        return OP_POLL

    @property
    def targeted_mode(self) -> bool:
        return self._targeted_mode

    def enable_targeted_mode(self,
                             target_port_bottom: int = constants.PORT_ADDRESS_MIN,
                             target_port_top: int = constants.PORT_ADDRESS_MAX
                             ) -> None:
        self._targeted_mode = True
        self.target_port_bottom = target_port_bottom
        self.target_port_top = target_port_top

    def disable_targeted_mode(self) -> None:
        self._targeted_mode = False

    @property
    def vlc_transmission(self) -> bool:
        return self._vlc_transmission

    def enable_vlc_transmission(self) -> None:
        self._vlc_transmission = True

    def disable_vlc_transmission(self) -> None:
        self._vlc_transmission = False

    @property
    def diagnostics_messages(self) -> bool:
        return self._send_diagnostics

    def enable_diagnostics_messages(self) -> None:
        self._send_diagnostics = True

    def disable_diagnostics_messages(self) -> None:
        self._send_diagnostics = False

    @property
    def diagnostics_method(self) -> DiagnosticsMethod:
        return self._diagnostics_method

    def diagnostics_method_broadcast(self) -> None:
        self._diagnostics_method = DiagnosticsMethod.BROADCAST

    def diagnostics_method_unicast(self) -> None:
        self._diagnostics_method = DiagnosticsMethod.UNICAST

    @property
    def reply_on_cond_change(self) -> bool:
        return self._reply_on_cond_change

    def reply_only_as_response(self) -> None:
        self._reply_on_cond_change = False

    def reply_on_all_cond_changes(self) -> None:
        self._reply_on_cond_change = True

    @property
    def field_5_flags(self) -> bytes:
        """Set behaviour of Node

        Int8
        """

        field = b''

        # 7-6 - 2 Bits
        # Unused, transmit as zero, do not test
        # upon receipt.
        field += b'\0\0'

        # 5 - Bit
        #     0 = Disable Targeted Mode.
        #     1 = Enable Targeted Mode.
        flag_targeted_mode = 1 if self.targeted_mode else 0
        field += bytes([flag_targeted_mode])

        # 4 - Bit
        #     0 = Enable VLC transmission.
        #     1 = Disable VLC transmission.
        flag_vlc_transmission = 1 if self.vlc_transmission else 0
        field += bytes([flag_vlc_transmission])

        # 3 - Bit
        #     0 = Diagnostics messages are broadcast. (if bit 2).
        #     1 = Diagnostics messages are unicast. (if bit 2).
        if self.diagnostics_method is DiagnosticsMethod.UNICAST:
            flag_diagnostics_method = 1
        else:  # DiagnosticsMethod.BROADCAST
            flag_diagnostics_method = 0
        field += bytes([flag_diagnostics_method])

        # 2 - Bit
        #     0 = Do not send me diagnostics messages.
        #     1 = Send me diagnostics messages.
        flag_send_diagnostics = 1 if self._send_diagnostics else 0
        field += bytes([flag_send_diagnostics])

        # 1 - Bit
        #     0 = Only send ArtPollReply in response to an ArtPoll or ArtAddress.
        #     1 = Send ArtPollReply whenever Node conditions change.
        #         This selection allows the Controller to be informed
        #         of changes without the need to continuously poll.
        flag_reply_on_cond_change = 1 if self._reply_on_cond_change else 0
        field += bytes([flag_reply_on_cond_change])

        # 0 - Bit
        #     0 = Deprecated.
        field += b'\0'

        return field

    @property
    def diagnostics_priority(self) -> DiagPriorityCode:
        return self._diag_priority

    @diagnostics_priority.setter
    def diagnostics_priority(self, new_value: DiagPriorityCode) -> None:
        if not isinstance(new_value, DiagPriorityCode):
            raise ValueError('Given value not of type DiagPriorityCode')
        self._diag_priority = new_value

    @property
    def field_6_diag_priority(self) -> bytes:
        return bytes([self.diagnostics_priority.value])

    @property
    def target_port_top(self) -> int:
        return self._target_port_top

    @target_port_top.setter
    def target_port_top(self, new_value: int) -> None:
        if new_value > constants.PORT_ADDRESS_MAX:
            raise ValueError('Target Port Address Top larger than maximum'
                             f'{new_value} > {constants.PORT_ADDRESS_MAX}')
        self._target_port_top = new_value

    @property
    def field_7_target_port_address_top_hi(self) -> bytes:
        return bytes([self._target_port_top.to_bytes(2, byteorder='big')[0]])

    @property
    def field_8_target_port_address_top_lo(self) -> bytes:
        return bytes([self._target_port_top.to_bytes(2, byteorder='big')[1]])

    @property
    def target_port_bottom(self) -> int:
        return self._target_port_bottom

    @target_port_bottom.setter
    def target_port_bottom(self, new_value: int) -> None:
        if new_value < constants.PORT_ADDRESS_MIN:
            raise ValueError('Target Port Address Top smaller than minimum'
                             f'{new_value} < {constants.PORT_ADDRESS_MIN}')
        self._target_port_bottom = new_value

    @property
    def field_9_target_port_address_bottom_hi(self) -> bytes:
        return bytes([self._target_port_bottom.to_bytes(2, byteorder='big')[0]])

    @property
    def field_10_target_port_address_bottom_lo(self) -> bytes:
        return bytes([self._target_port_bottom.to_bytes(2, byteorder='big')[1]])

    def compose(self) -> bytes:
        return \
            self.field_1_id + \
            self.field_2_op_code + \
            self.field_3_prot_ver_hi + \
            self.field_4_prot_ver_lo + \
            self.field_5_flags + \
            self.field_6_diag_priority + \
            self.field_7_target_port_address_top_hi + \
            self.field_8_target_port_address_top_lo + \
            self.field_9_target_port_address_bottom_hi + \
            self.field_10_target_port_address_bottom_lo
