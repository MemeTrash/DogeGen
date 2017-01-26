"""
Server so nltk doesn't initialize for every meme request.

Author: Jack Romo <sharrackor@gmail.com>
"""

from flask import Flask, request
from main import DogeGen


class DogeServer(object):
    """
    Server to generate Doge images.
    """

    app = Flask(__name__)
    dogegen = None

    @staticmethod
    def run_server(resources, host_name='0.0.0.0', port=5000):
        """
        Run the internal server.

        Args:
            resources (str): Resources directory, eg. "./resources".
            host_name (str): Host name of server.
            port (int): Port of server.
        """
        if not DogeServer.dogegen:
            DogeServer.dogegen = DogeGen(resources)
        DogeServer.app.run(debug=True, host=host_name, port=port)

    @staticmethod
    @app.route('/makememe')
    def makememe():
        """
        Make a meme upon a server GET request.

        Args:
            inptext (str): Escaped input text.
            outdir (str): Escaped output directory, including image name and extension.
            maxphrases (int): Number of phrases allowed. No escaping needed.

        Returns:
            str: Directory of image.

        """
        inptext = request.args.get('inptext')
        outdir = request.args.get('outdir')
        maxphrases = int(request.args.get('maxphrases'))
        DogeServer.dogegen.make_meme(inptext, outdir, maxphrases)
        return outdir

    @staticmethod
    @app.route('/shutdown', methods=['POST'])
    def shutdown():
        """
        Shut down server internally.

        Returns:
            str: Status string.
        """
        func = request.environ.get('werkzeug.server.shutdown')
        if func is None:
            raise RuntimeError('Not running with the Werkzeug Server')
        func()
        return "Shutting down."
