#!/usr/bin/env python3
# -*- coding: utf-8, vim: expandtab:ts=4 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

# imports: library
from argparse import ArgumentParser
import configparser
import logging
import logging.config
import pkg_resources

# imports: project
from libmonty_artnet import version
from libmonty_artnet.controller import controller
from libmonty_artnet.packets.base import ArtNetBasePacket


def main() -> None:

    logger_config_name = 'data/logger.ini'

    if not pkg_resources.resource_exists(__name__, logger_config_name):
        logging.error('logger config does not exist')
        return

    logger_config = pkg_resources.resource_stream(__name__, logger_config_name)
    logger_config_str = logger_config.read().decode('UTF-8')
    logger_config_parser = configparser.ConfigParser()
    logger_config_parser.read_string(logger_config_str)
    logging.config.fileConfig(logger_config_parser)

    logging.info(version.PROGRAM_NAME)
    logging.info('-' * len(version.PROGRAM_NAME))

    parser = ArgumentParser(prog=version.PROGRAM_NAME)

    parser.add_argument('--version',
                        help='Display version',
                        action='store_const', const=True, default=False,
                        dest='version')

    subparsers = parser.add_subparsers(dest='cmd')

    for subclass in ArtNetBasePacket.__subclasses__():
        subclass.create_subparser(add_to_subparsers=subparsers)

    args = parser.parse_args()

    if args.version:
        print(f'{version.PROGRAM_NAME} {version.__version__}')
        return

    subcommands = {subclass.subcommand: subclass.process_args
                   for subclass
                   in ArtNetBasePacket.__subclasses__()}

    if args.cmd in subcommands:
        try:
            subcommands[args.cmd](args)
        except NotImplementedError:
            logging.error('Method not implemented.')
        return

    controller.run()


if __name__ == '__main__':
    main()

# -------------------------------------------------------------------- #
