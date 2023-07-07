#!/usr/bin/env python3

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""
ArtInput packet handler
"""

from argparse import Namespace

from libmonty_artnet.packets.base import ArtNetBasePacket


class ArtInputPacket(ArtNetBasePacket):
    """ArtInput packet"""

    subcommand = 'input'

    @classmethod
    def create_subparser(cls, add_to_subparsers) -> None:
        """Create subparser"""

        parser = add_to_subparsers.add_parser(
            cls.subcommand,
            help='ArtInput'
        )

    @staticmethod
    def process_args(args: Namespace) -> None:
        """Process args"""

        raise NotImplementedError

    @property
    def op_code(self) -> int:
        """Op code"""

        raise NotImplementedError

    def compose(self) -> bytes:
        """Compose"""

        raise NotImplementedError
