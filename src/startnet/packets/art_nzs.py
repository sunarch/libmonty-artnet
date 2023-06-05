#!/usr/bin/env python3
# -*- coding: utf-8, vim: expandtab:ts=4 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from argparse import Namespace

from startnet.packets.base import ArtNetBasePacket


class ArtNzsPacket(ArtNetBasePacket):

    subcommand = 'nzs'

    @classmethod
    def create_subparser(cls, add_to_subparsers) -> None:
        parser = add_to_subparsers.add_parser(
            cls.subcommand,
            help='ArtNzs'
        )

    @staticmethod
    def process_args(args: Namespace) -> None:
        raise NotImplementedError

    @property
    def op_code(self) -> int:
        raise NotImplementedError

    def compose(self) -> bytes:
        raise NotImplementedError
