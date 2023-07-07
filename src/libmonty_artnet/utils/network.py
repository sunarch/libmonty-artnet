#!/usr/bin/env python3

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""
Network functionality
"""

import logging
import socket
from typing import Generator


UNIVERSAL_BROADCAST_IP_ADDRESS = '255.255.255.255'
DEFAULT_REPEAT_WAIT_SECS = 0.5


def udp_send(ip_address: str,
             port: int,
             payload: bytes,
             enable_broadcast: bool = True
             ) -> None:
    """UPD send"""

    logging.info('Sending to IP "%s" PORT "%s"', ip_address, port)
    logging.info('|-> Payload size: %s', len(payload))

    sock = socket.socket(socket.AF_INET,  # IPv4
                         socket.SOCK_DGRAM)  # UDP

    if enable_broadcast:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    sock.sendto(payload, (ip_address, port))


def udp_create_listener(ip_address: str,
                        port: int
                        ) -> socket.socket:
    """UDP create listener"""

    logging.info('UDP binding: IP "%s" PORT "%s"', ip_address, port)

    sock = socket.socket(socket.AF_INET,  # internet
                         socket.SOCK_DGRAM)  # UDP
    sock.bind((ip_address, port))

    return sock


def udp_receive(sock: socket.socket,
                buffer_size: int = 1024
                ) -> tuple[bytes, str]:
    """UDP receive"""

    data, addr = sock.recvfrom(buffer_size)

    logging.info('Received %s bytes from %s', len(data), addr)

    return data, addr


def tcp_receive(ip_address: str = '127.0.0.1',
                port: int = 9000
                ) -> Generator:
    """TCP receive"""

    with socket.socket(
        socket.AF_INET,  # IPv4
        socket.SOCK_STREAM  # TCP
    ) as tcp_socket:

        tcp_socket.bind((ip_address, port))
        tcp_socket.listen(1)

        while True:
            logging.info('Waiting for connection')
            connection, client = tcp_socket.accept()
            client_ip, client_port = client

            try:
                logging.info('Connected to client IP: %s:%s', client_ip, client_port)

                while True:
                    data = connection.recv(1024)

                    logging.info('Received data.')

                    if data == b'\x00':
                        break

                    yield [int(byte) for byte in data]

            finally:
                connection.close()
