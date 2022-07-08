#!/usr/bin/env python3
# -*- coding: utf-8, vim: expandtab:ts=4 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from libmonty_artnet.packets.base import ArtNetBasePacket
from libmonty_artnet.protocol.op_codes import OpSync


class ArtSyncPacket(ArtNetBasePacket):

    @property
    def op_code(self) -> int:
        return OpSync

    @property
    def field_5_aux_1(self) -> bytes:
        return b'\0'

    @property
    def field_6_aux_2(self) -> bytes:
        return b'\0'

    def compose(self):
        return \
            self.field_1_id + \
            self.field_2_op_code + \
            self.field_3_prot_ver_hi + \
            self.field_4_prot_ver_lo + \
            self.field_5_aux_1 + \
            self.field_6_aux_2
