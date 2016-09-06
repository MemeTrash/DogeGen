"""
Entry point for program.

Author: Jack Romo <sharrackor@gmail.com>
"""

import sys, os
from dogegen import *


def main(args):
    """
    Given command line arguments, generate a Doge meme or start a server / Unix service.

    NB: The 'service' option is used internally by the dogegenservice script.

    Args:
        args (list[str]): List of command line arguments.
    """
    if args[1] == "--server-start":
        start_server(args)
    elif args[1] == "--service-start":
        start_service(args)
    else:
        make_meme_no_server(args)


def start_service(args):
    """
    Given command line arguments, start a server as a Unix service.

    Args:
        args (list[str]): List of command line arguments.
    """
    with open("/var/run/dogegenservice.pid", 'w') as pid_file:
        pid_file.write(str(os.getpid()))
    start_server(args)


def start_server(args):
    """
    Given command line arguments, start a server.

    Args:
        args (list[str]): List of command line arguments.
    """
    DogeServer.run_server(args[2], args[3], int(args[4]))


def make_meme_no_server(args):
    """
    Given command line arguments, generate a Doge meme.

    Args:
        args (list[str]): List of command line arguments.
    """
    DogeGen(args[3]).make_meme(args[1], args[2], int(args[4]))


if __name__ == "__main__":
    main(sys.argv)
