#!/usr/bin/env python3
# -*- coding: utf-8, vim: expandtab:ts=4 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""
ArtSync packet handler
"""

from argparse import Namespace
import time

from libmonty_artnet.packets.base import ArtNetBasePacket
from libmonty_artnet.protocol import constants
from libmonty_artnet.protocol.op_codes import OP_SYNC
from libmonty_artnet.utils import common_args, network


class ArtSyncPacket(ArtNetBasePacket):
    """ArtSync packet"""

    subcommand = 'sync'

    @classmethod
    def create_subparser(cls, add_to_subparsers) -> None:
        """Create subparser"""

        parser = add_to_subparsers.add_parser(
            cls.subcommand,
            help='ArtSync'
        )

        common_args.ip_address(parser)
        common_args.ip_port(parser, default=constants.DEFAULT_IP_PORT)
        common_args.repeat(parser)

    @staticmethod
    def process_args(args: Namespace) -> None:
        """Process args"""

        packet = ArtSyncPacket()

        while True:
            try:
                time.sleep(network.DEFAULT_REPEAT_WAIT_SECS)

                network.udp_send(args.ip, args.port, packet.compose())

                if not args.repeat:
                    break
            except KeyboardInterrupt:
                break

    @property
    def op_code(self) -> int:
        """Op code"""

        return OP_SYNC

    @property
    def field_5_aux_1(self) -> bytes:
        """Field 5: Aux 1"""

        return b'\0'

    @property
    def field_6_aux_2(self) -> bytes:
        """Field 6: Aux 2"""

        return b'\0'

    def compose(self) -> bytes:
        """Compose"""

        return \
            self.field_1_id + \
            self.field_2_op_code + \
            self.field_3_prot_ver_hi + \
            self.field_4_prot_ver_lo + \
            self.field_5_aux_1 + \
            self.field_6_aux_2
