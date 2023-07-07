#!/usr/bin/env python3

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""
Grid
"""

def chunk_list(source: list,
               chunk_size: int
               ) -> list[list]:
    """Chunk list"""

    if len(source) > chunk_size:
        return [source[0:chunk_size]] + \
               chunk_list(source[chunk_size:], chunk_size=chunk_size)

    return [source]
