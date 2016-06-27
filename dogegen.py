"""
Entry point for program.

Author: Jack Romo <sharrackor@gmail.com>
"""

import sys
import dogegen


def main(args):
    """
    Given command line arguments, generates a Doge meme or manages a daemon.

    Args:
        args (list[str]): List of command line arguments.
    """
    if args[1] == "--daemon-start":
        dogegen.make_daemon()
    elif args[1] == "--with-daemon":
        doge_daemon = dogegen.get_daemon(args[2])
        doge_daemon.make_meme(args[3], args[4], int(args[5]))
    else:
        dogegen.make_meme(args[1], args[2], int(args[3]))


if __name__ == "__main__":
    main(sys.argv)
