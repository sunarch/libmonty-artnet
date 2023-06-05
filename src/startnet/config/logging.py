#!/usr/bin/env python3
# -*- coding: utf-8, vim: expandtab:ts=4 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

# imports: library
import os.path

# imports: dependencies
from xdg_base_dirs import xdg_cache_home

# imports: project
from startnet import version


def _cache_dir_path() -> str:
    cache_dir_path = os.path.join(xdg_cache_home(), version.PROGRAM_NAME)

    if not os.path.isdir(cache_dir_path):
        os.makedirs(cache_dir_path, mode=0o740, exist_ok=True)

    return cache_dir_path


def _log_file_name() -> str:
    return f'{version.PROGRAM_NAME}-{version.__version__}.log'


def _log_file_path() -> str:
    return os.path.join(_cache_dir_path(), _log_file_name())


config_v1 = {
    'version': 1,
    'formatters': {
        'form01': {
            'format': '[%(asctime)s] [%(levelname)-8s] %(message)s',
            'datefmt': '%H:%M:%S'
        },
        'form02': {
            'format': '[%(asctime)s] [%(levelname)-8s] %(message)s'
        }
    },
    'handlers': {
        'hand01': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'form01',
            'stream': 'ext://sys.stdout'
        },
        'hand02': {
            'class': 'logging.FileHandler',
            'level': 'INFO',
            'formatter': 'form02',
            'filename': _log_file_path(),
            'mode': 'w',
            'encoding': 'UTF-8'
        }
    },
    'loggers': {
        'root': {
            'level': 'NOTSET',
            'handlers': ['hand01', 'hand02']
        }
    }
}

default = config_v1
