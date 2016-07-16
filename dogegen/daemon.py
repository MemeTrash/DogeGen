"""
Daemon so nltk doesn't initialize for every meme request.

Author: Jack Romo <sharrackor@gmail.com>
"""

import Pyro.core
import main


class DogeDaemon(Pyro.core.ObjBase):
    """
    Daemon that can be sent requests for memes.
    """

    def __init__(self):
        Pyro.core.ObjBase.__init__(self)
        self._generator = DogeGen()

    def make_meme(self, *args):
        """
        Create a meme file and draw to an output directory.
        """
        self._generator.make_meme(*args)

    @staticmethod
    def make_daemon():
        """
        Make and start up a doge generator daemon.

        Returns:
            str: URI to access daemon by.
        """
        Pyro.core.initServer()
        daemon = Pyro.core.Daemon()
        uri = daemon.connect(DogeDaemon())
        print uri
        daemon.requestLoop()

    @staticmethod
    def get_daemon(uri):
        """
        Get reference to DogeDaemon object from daemon.

        Args:
            uri (str): URI to locate object with.

        Returns:
            DogeDaemon: Doge daemon to make meme with.
        """
        return Pyro.core.getProxyForURI(uri)
