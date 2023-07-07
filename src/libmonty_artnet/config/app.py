#!/usr/bin/env python3

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""
App config
"""

# imports: library
import json
import os.path

# imports: dependencies
from xdg_base_dirs import xdg_config_home

# imports: project
from libmonty_artnet import version


config_v1: dict = {}

default: dict = config_v1


def _config_dir_path() -> str:
    """Config dir path"""

    config_dir_path = os.path.join(xdg_config_home(), version.PROGRAM_NAME)

    if not os.path.isdir(config_dir_path):
        os.makedirs(config_dir_path, mode=0o740, exist_ok=True)

    return config_dir_path


def _config_file_path() -> str:
    """Config file path"""

    return os.path.join(_config_dir_path(), 'config.json')


def config() -> dict:
    """Config"""

    config_file_path: str = _config_file_path()

    try:
        with open(config_file_path, 'r', encoding='UTF-8') as fh_config_file:
            config_dict: dict = json.load(fh_config_file)
    except FileNotFoundError:
        config_dict: dict = default

        with open(config_file_path, 'w', encoding='UTF-8') as fh_config_file:
            json.dump(config_dict, fh_config_file, indent=2)

    return config_dict


def check_config_file():
    """Check config file"""

    _ = config()
