#!/usr/bin/env python3
# -*- coding: utf-8, vim: expandtab:ts=4 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from abc import ABC
from argparse import Namespace


class ArtNetBasePacket(ABC):

    subcommand = None

    @classmethod
    def create_subparser(cls, add_to_subparsers) -> None:
        raise NotImplementedError

    @staticmethod
    def process_args(args: Namespace) -> None:
        raise NotImplementedError

    @property
    def id(self) -> str:
        return 'Art-Net\0'

    @property
    def field_1_id(self) -> bytes:
        return bytes(self.id, encoding='ASCII')

    @property
    def op_code(self) -> int:
        raise NotImplementedError

    @property
    def field_2_op_code(self) -> bytes:
        return self.op_code.to_bytes(2, byteorder='little')

    @property
    def protocol_version(self) -> int:
        return 14

    @property
    def field_3_prot_ver_hi(self) -> bytes:
        """Not present in all packet types"""
        return bytes([self.protocol_version.to_bytes(2, byteorder='big')[0]])

    @property
    def field_4_prot_ver_lo(self) -> bytes:
        """Not present in all packet types"""
        return bytes([self.protocol_version.to_bytes(2, byteorder='big')[1]])

    def compose(self) -> bytes:
        raise NotImplementedError
