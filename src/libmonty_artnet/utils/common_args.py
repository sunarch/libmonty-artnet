#!/usr/bin/env python3
# -*- coding: utf-8, vim: expandtab:ts=4 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""
Common arguments
"""

from argparse import ArgumentParser

from libmonty_artnet.utils.network import UNIVERSAL_BROADCAST_IP_ADDRESS


def ip_address(to_parser: ArgumentParser):
    """Argument: IP address"""

    to_parser.add_argument(
        '--ip',
        help='IP address',
        default=UNIVERSAL_BROADCAST_IP_ADDRESS,
        dest='ip'
    )


def ip_port(to_parser: ArgumentParser, default: int):
    """Argument: IP port"""

    to_parser.add_argument(
        '--port',
        help='IP port',
        type=int, default=default,
        dest='port'
    )


def repeat(to_parser: ArgumentParser):
    """Argument: Repeat"""

    to_parser.add_argument(
        '--repeat',
        help='Repeat',
        action='store_true',
        dest='repeat'
    )


def use_experimental(to_parser: ArgumentParser):
    """Argument: Use experimental features"""

    to_parser.add_argument(
        '--use-experimental',
        help='Override safety check to disable the use of unfinished features',
        action='store_true',
        dest='use_experimental'
    )
