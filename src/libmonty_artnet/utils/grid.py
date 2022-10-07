#!/usr/bin/env python3
# -*- coding: utf-8, vim: expandtab:ts=4 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

# lib
from dataclasses import dataclass
import math

# dependencies
import numpy as np


def chunk_list(source: list,
               chunk_size: int
               ) -> list[list]:

    if len(source) > chunk_size:
        return [source[0:chunk_size]] + \
               chunk_list(source[chunk_size:], chunk_size=chunk_size)
    else:
        return [source]


@dataclass
class RGB:
    r: int
    g: int
    b: int


def rotate_to_diagonal(source: list,
                       grid_width: int,
                       grid_height: int
                       ) -> list:

    print('Source:', source)
    print('len(source):', len(source))
    grouped_source = [RGB(source[i], source[i+1], source[i+2]) for i in range(0, len(source), 3)]
    print('Grouped source:', grouped_source)
    print('len(grouped_source):', len(grouped_source))
    grid = np.array(grouped_source).reshape(grid_width, grid_height)
    print('Grid:', grid)

    outer_square_side_part_1 = math.sqrt((grid_width ** 2) / 2)
    print('outer_square_side_part_1:', outer_square_side_part_1)
    outer_square_side_part_2 = math.sqrt((grid_height ** 2) / 2)
    print('outer_square_side_part_2:', outer_square_side_part_2)

    diagonal_square_side = round(outer_square_side_part_1 + outer_square_side_part_2)
    print('diagonal_square_side:', diagonal_square_side)

    print('Grid to list:', grid.tolist())
    flattened = []
    for x in grid.tolist():
        flattened.extend(x)
    print('Flattened:', flattened)
    print('len(flattened):', len(flattened))

    result = []
    for x in flattened:
        result.extend([x.r, x.g, x.b])
    print('Result:', result)
    print('len(result):', len(result))

    return result
