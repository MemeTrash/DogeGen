"""
Entry point for program.

Author: Jack Romo <sharrackor@gmail.com>
"""

import sys
from dogegen import *


def main(args):
    """
    Given command line arguments, generates a Doge meme or manages a daemon.

    Args:
        args (list[str]): List of command line arguments.
    """
    if args[1] == "--daemon-start":
        DogeDaemon.make_daemon(args[2])
    elif args[1] == "--with-daemon":
        DogeDaemon.get_daemon(args[2]).make_meme(args[3], args[4], int(args[5]))
    else:
        DogeGen(args[3]).make_meme(args[1], args[2], int(args[4]))


if __name__ == "__main__":
    main(sys.argv)
