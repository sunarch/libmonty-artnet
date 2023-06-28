#!/usr/bin/env python3
# -*- coding: utf-8, vim: expandtab:ts=4 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

PORT_ADDRESS_MIN = 0
PORT_ADDRESS_MAX = 32767

DEFAULT_BROADCAST_IP_ADDRESSES = [
    '2.255.255.255',
    '10.255.255.255'
]
DEFAULT_IP_PORT = 0x1936  # 6454

DMX_CHANNELS = 512

RGB_UNITS_PER_UNIVERSE = DMX_CHANNELS - (DMX_CHANNELS % 3)
