#!/usr/bin/env python3
# -*- coding: utf-8, vim: expandtab:ts=4 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import logging
import socket


def udp_send(ip_address: str,
             port: int,
             payload: bytes,
             enable_broadcast: bool = True
             ) -> None:

    logging.info('Sending to IP "%s" PORT "%s"', ip_address, port)
    logging.info('|-> Payload size: %s', len(payload))

    sock = socket.socket(socket.AF_INET,  # internet
                         socket.SOCK_DGRAM)  # UDP

    if enable_broadcast:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    sock.sendto(payload, (ip_address, port))


def udp_create_listener(ip_address: str,
                        port: int
                        ) -> socket.socket:
    logging.info('UDP binding: IP "%s" PORT "%s"', ip_address, port)

    sock = socket.socket(socket.AF_INET,  # internet
                         socket.SOCK_DGRAM)  # UDP
    sock.bind((ip_address, port))

    return sock


def udp_receive(sock: socket.socket,
                buffer_size: int = 1024
                ) -> tuple[bytes, str]:

    data, addr = sock.recvfrom(buffer_size)

    logging.info('Received %s bytes from %s', len(data), addr)

    return data, addr
