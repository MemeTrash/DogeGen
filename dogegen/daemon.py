"""
Daemon so nltk doesn't initialize for every meme request.

Author: Jack Romo <sharrackor@gmail.com>
"""

import Pyro.core
from main import DogeGen


class DogeDaemon(Pyro.core.ObjBase):
    """
    Daemon that can be sent requests for memes.
    """

    def __init__(self, resources):
        Pyro.core.ObjBase.__init__(self)
        self._generator = DogeGen(resources)

    def make_meme(self, *args):
        """
        Create a meme file and draw to an output directory.
        """
        self._generator.make_meme(*args)

    @staticmethod
    def make_daemon(resources):
        """
        Make and start up a doge generator daemon.

        Returns:
            str: URI to access daemon by.
        """
        Pyro.core.initServer()
        daemon = Pyro.core.Daemon()
        uri = daemon.connect(DogeDaemon(resources))
        print uri
        print "Ready for wow"
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
