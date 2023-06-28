#!/usr/bin/env python3
# -*- coding: utf-8, vim: expandtab:ts=4 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""
Art-Net base packet
"""

from abc import ABC
from argparse import Namespace


class ArtNetBasePacket(ABC):
    """Art-Net base packet"""

    subcommand = None

    @classmethod
    def create_subparser(cls, add_to_subparsers) -> None:
        """Create subparser"""

        raise NotImplementedError

    @staticmethod
    def process_args(args: Namespace) -> None:
        """Process args"""

        raise NotImplementedError

    @property
    def id(self) -> str:
        """ID"""

        return 'Art-Net\0'

    @property
    def field_1_id(self) -> bytes:
        """Field 1: ID"""

        return bytes(self.id, encoding='ASCII')

    @property
    def op_code(self) -> int:
        """Op code"""

        raise NotImplementedError

    @property
    def field_2_op_code(self) -> bytes:
        """Field 2: Op code"""

        return self.op_code.to_bytes(2, byteorder='little')

    @property
    def protocol_version(self) -> int:
        """Protocol version"""

        return 14

    @property
    def field_3_prot_ver_hi(self) -> bytes:
        """Field 3: Protocol version - HI

        Not present in all packet types
        """
        return bytes([self.protocol_version.to_bytes(2, byteorder='big')[0]])

    @property
    def field_4_prot_ver_lo(self) -> bytes:
        """Field 4: Protocol version - LO

        Not present in all packet types
        """

        return bytes([self.protocol_version.to_bytes(2, byteorder='big')[1]])

    def compose(self) -> bytes:
        """Compose"""

        raise NotImplementedError
