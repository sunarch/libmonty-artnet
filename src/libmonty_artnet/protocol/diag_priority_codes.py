#!/usr/bin/env python3

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
    """Diag priority codes - enum"""

    # NOT IN SPECIFICATION: All messages.
    DP_ALL: int = 0x00

    # Low priority message.
    DP_LOW: int = 0x10

    # Medium priority message.
    DP_MED: int = 0x40

    # High priority message.
    DP_HIGH: int = 0x80

    # Critical priority message.
    DP_CRITICAL: int = 0xe0

    # Volatile message.
    DP_VOLATILE: int = 0xf0
