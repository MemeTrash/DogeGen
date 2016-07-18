"""
Entry point for program.

Author: Jack Romo <sharrackor@gmail.com>
"""

import sys
from dogegen import *


def main(args):
    """
    Given command line arguments, generate a Doge meme or start a server.

    Args:
        args (list[str]): List of command line arguments.
    """
    if args[1] == "--server-start":
        start_server(args)
    else:
        make_meme_no_server(args)


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
