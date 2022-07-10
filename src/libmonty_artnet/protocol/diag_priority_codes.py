#!/usr/bin/env python3
# -*- coding: utf-8, vim: expandtab:ts=4 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""Table 5 – Priority Codes

The following table details the Diagnostics Priority codes.
These are used in ArtPoll and ArtDiagData.

Messages of type 'DpVolatile' are displayed on a single line
    in the DMX-Workshop diagnostics display.
All other types are displayed in a list box.

Enum field name: Mnemonic
Enum field value: Code (hex coded integer)
"""

from enum import Enum


class DiagPriorityCode(Enum):

    # NOT IN SPECIFICATION: All messages.
    DpAll = 0x00

    # Low priority message.
    DpLow = 0x10

    # Medium priority message.
    DpMed = 0x40

    # High priority message.
    DpHigh = 0x80

    # Critical priority message.
    DpCritical = 0xe0

    # Volatile message.
    DpVolatile = 0xf0
