#!/usr/bin/env python3
# -*- coding: utf-8, vim: expandtab:ts=4 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from argparse import Namespace
import logging
import time

from libmonty_artnet.packets.base import ArtNetBasePacket
from libmonty_artnet.protocol import constants
from libmonty_artnet.protocol.op_codes import OpOutput
from libmonty_artnet.utils import common_args, grid, network


class ArtDmxPacket(ArtNetBasePacket):

    subcommand = 'dmx'

    @classmethod
    def create_subparser(cls, add_to_subparsers) -> None:
        parser = add_to_subparsers.add_parser(
            cls.subcommand,
            help='ArtDmx'
        )

        common_args.ip_address(parser)
        common_args.ip_port(parser, default=constants.DEFAULT_IP_PORT)
        common_args.repeat(parser)

        parser.add_argument(
            '--universe',
            help='Universe',
            type=int, default=0,
            dest='universe'
        )

        dmx_source = parser.add_mutually_exclusive_group(required=True)

        dmx_source.add_argument(
            '--data',
            help='Data values',
            type=int, nargs='+',
            default=None,
            dest='data'
        )

        dmx_source.add_argument(
            '--file',
            help='Data values from file',
            default=None,
            dest='data_file'
        )

    @staticmethod
    def read_display_file(filename: str) -> list[int]:
        data = []
        with open(filename, 'r', encoding='UTF-8') as data_file:
            for line in data_file:
                for item in line.split():
                    item = item.replace('-', '') \
                        .replace('|', '') \
                        .replace(' ', '')
                    if item == '':
                        continue
                    elif item[0:1] == '#':
                        hex_val = item[1:]
                        if len(hex_val) == 3:
                            for nibble in hex_val:
                                data.append(int(nibble * 2, 16))
                        elif len(hex_val) == 6:
                            for byte in [hex_val[i*2:(i*2)+2] for i in range(3)]:
                                data.append(int(byte, 16))
                        else:
                            logging.warning('Invalid display value %s', item)
                    else:
                        try:
                            data.append(int(item.strip()))
                        except ValueError:
                            logging.warning('Invalid display value %s', item)
        return data

    @classmethod
    def process_args(cls, args: Namespace) -> None:

        data = [0]
        if args.data is not None:
            data = args.data
        if args.data_file is not None:
            data = cls.read_display_file(args.data_file)

        chunk_size = 512 - (512 % 3)
        chunked_data = grid.chunk_list(data, chunk_size=chunk_size)

        while True:
            try:
                time.sleep(network.DEFAULT_REPEAT_WAIT_SECS)

                for index, data_list in enumerate(chunked_data):
                    universe = args.universe + index
                    packet = ArtDmxPacket(data_list, universe=universe)

                    network.udp_send(args.ip, args.port, packet.compose())

                if not args.repeat:
                    break
            except KeyboardInterrupt:
                break

    def __init__(self,
                 data: list[int],
                 sequence: int = 0,
                 physical: int = 0,
                 universe: int = 0
                 ) -> None:

        self._sequence = sequence
        self._physical = physical
        self._universe = universe

        if len(data) == 0:
            data.append(0)
        if len(data) % 2 != 0:
            data.append(0)
        if len(data) > 512:
            raise ValueError('Data too long')
        self._data = data

    @property
    def op_code(self) -> int:
        return OpOutput

    @property
    def field_5_sequence(self) -> bytes:
        return bytes([self._sequence])

    @property
    def field_6_physical(self) -> bytes:
        return bytes([self._physical])

    @property
    def field_7_sub_uni(self) -> bytes:
        return bytes([self._universe.to_bytes(2, byteorder='little')[0]])

    @property
    def field_8_net(self) -> bytes:
        return bytes([self._universe.to_bytes(2, byteorder='little')[1]])

    @property
    def length(self) -> int:
        return len(self._data)

    @property
    def field_9_length_hi(self) -> bytes:
        return bytes([self.length.to_bytes(2, byteorder='big')[0]])

    @property
    def field_10_length(self) -> bytes:
        return bytes([self.length.to_bytes(2, byteorder='big')[1]])

    @property
    def field_11_data(self) -> bytes:
        return bytes(self._data)

    def compose(self) -> bytes:
        return \
            self.field_1_id + \
            self.field_2_op_code + \
            self.field_3_prot_ver_hi + \
            self.field_4_prot_ver_lo + \
            self.field_5_sequence + \
            self.field_6_physical + \
            self.field_7_sub_uni + \
            self.field_8_net + \
            self.field_9_length_hi + \
            self.field_10_length + \
            self.field_11_data
