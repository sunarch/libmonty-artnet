#!/usr/bin/env python3
# -*- coding: utf-8, vim: expandtab:ts=4 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import argparse
from argparse import ArgumentParser
import logging
from multiprocessing import Process, Pipe, Value
import tkinter as tk
from tkinter import ttk

from libmonty_artnet.utils import common_args, network


SUBCOMMAND = 'controller'


def create_subparser(add_to_subparsers) -> None:
    parser = add_to_subparsers.add_parser(
        SUBCOMMAND,
        help='Controller'
    )

    common_args.use_experimental(parser)


def process_args(args: argparse.Namespace) -> None:

    if not args.use_experimental:
        logging.error('Experimental feature, its use is disabled by default.')
        logging.error('If you wish to proceed regardless, see --help for the CLI option.')
        logging.error('Exiting.')
        return

    run()


def _create_cli_parser() -> ArgumentParser:
    parser = ArgumentParser(prog='libmonty Art-Net controller')

    parser.add_argument('--quit',
                        help='End controller operation',
                        action='store_true',
                        dest='quit')

    return parser


def run():

    end_loop_cli = Value('b', False)
    end_loop_listener = Value('b', False)

    pipe_cli_parent, pipe_cli_child = Pipe()
    pipe_listener_parent, pipe_listener_child = Pipe()

    p_cli = Process(target=loop_cli, args=(pipe_cli_child,
                                           end_loop_cli))
    p_listener = Process(target=loop_listener, args=(pipe_listener_child,
                                                     end_loop_listener))

    p_cli.start()
    p_listener.start()

    while True:
        cli_result = pipe_cli_parent.recv()
        listener_result = pipe_listener_parent.recv()

        print(listener_result)

        if end_loop_cli.value:
            end_loop_cli.value = True
            end_loop_listener.value = True
            break

    p_cli.join()
    p_listener.join()


def terminal_enter_key_callback(root, terminal_listbox, input_field, parser: ArgumentParser):
    terminal_text = input_field.get()
    input_field.delete(0, tk.END)

    terminal_listbox.insert(tk.END, f'$ {terminal_text}')
    terminal_listbox.yview_moveto(1)  # scrolls the listbox down to the very last.

    try:
        args, unknown = parser.parse_known_args([terminal_text])
    except argparse.ArgumentError as err:
        terminal_listbox.insert(tk.END, f'{err}')
        return
    except argparse.ArgumentTypeError as err:
        terminal_listbox.insert(tk.END, f'{err}')
        return

    if unknown is not None:
        terminal_listbox.insert(tk.END, f'Unrecognized args: {unknown}')

    if args.quit:
        root.quit()


def loop_cli(conn, end_loop):

    parser = _create_cli_parser()

    root = tk.Tk()
    frm = ttk.Frame(root, padding=10)
    frm.grid()

    root.title('libmonty Art-Net controller CLI')
    root.geometry('800x420')
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    main = tk.Frame(root)
    main.grid(row=0, column=0, sticky='nsew')
    main.grid_rowconfigure(0, weight=1)
    main.grid_columnconfigure(0, weight=1)
    main.rowconfigure(0, weight=1)
    main.rowconfigure(1, weight=0)
    main.columnconfigure(0, weight=0)
    main.columnconfigure(1, weight=1)
    main.columnconfigure(2, weight=0)

    terminal_listbox = tk.Listbox(main, bg='black', fg='green',
                                  highlightcolor='green', highlightthickness=1,
                                  selectbackground='red')
    terminal_listbox.grid(row=0, column=0, columnspan=2)
    terminal_scrollbar = tk.Scrollbar(main)
    terminal_scrollbar.grid(row=0, column=2)

    terminal_listbox.insert(tk.END, 'libmonty Art-Net controller CLI')

    text = tk.Label(main, text="$ ")
    text.grid(row=1, column=0)

    input_field = tk.Entry(main)
    input_field.grid(row=1, column=1, columnspan=2)
    input_field.bind('<Return>', lambda x: terminal_enter_key_callback(main,
                                                                       terminal_listbox,
                                                                       input_field,
                                                                       parser))

    root.mainloop()

    end_loop.value = True
    conn.send('quit')
    conn.close()


def loop_listener(conn, end_loop: bool):
    sock = network.udp_create_listener('127.0.0.1', 0x1936)

    while not end_loop:
        data, addr = network.udp_receive(sock)
        conn.send(data)

    sock.close()
    conn.close()
