#!/usr/bin/env python3
# -*- coding: utf-8, vim: expandtab:ts=4 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

# imports: library
from argparse import ArgumentParser
import logging

# imports: dependencies
from libmonty_logging.config.file_and_stream.v1 import config as logging_config
import libmonty_logging.helper as logging_helper
import libmonty_logging.message as logging_message

# imports: project
from libmonty_artnet import version
from libmonty_artnet.controller import controller
from libmonty_artnet.packets.base import ArtNetBasePacket
import libmonty_artnet.config.app as app_config


def main() -> None:

    logging_helper.apply_config(version.PROGRAM_NAME,
                                version.__version__,
                                logging_config)

    logging_message.program_header(version.PROGRAM_NAME)

    parser = ArgumentParser(prog=version.PROGRAM_NAME)

    parser.add_argument('--version',
                        help='Display version',
                        action='store_true',
                        dest='version')

    subparsers = parser.add_subparsers(dest='cmd')

    for subclass in ArtNetBasePacket.__subclasses__():
        subclass.create_subparser(add_to_subparsers=subparsers)

    controller.create_subparser(add_to_subparsers=subparsers)

    args = parser.parse_args()

    app_config.check_config_file()

    if args.version:
        print(f'{version.PROGRAM_NAME} {version.__version__}')
        return

    subcommands = {subclass.subcommand: subclass.process_args
                   for subclass
                   in ArtNetBasePacket.__subclasses__()}

    subcommands[controller.SUBCOMMAND] = controller.process_args

    if args.cmd in subcommands:
        try:
            subcommands[args.cmd](args)
        except NotImplementedError:
            logging.error('Method not implemented.')
        return

    logging.warning('No subcommand selected.')
    logging.warning('Exiting.')


if __name__ == '__main__':
    main()

# -------------------------------------------------------------------- #
