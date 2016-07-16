"""
Main doge creation function.

Author: Jack Romo <sharrackor@gmail.com>
"""

from translate import dogeify_text
from drawmeme import draw_doge_meme

FONT_PATH = "./resources/comic_sans_font.ttf"
IMAGE_PATH = "./resources/doge_orig.jpg"


class DogeGen(object):
    def __init__(self, translator):
        self.translator = translator

    def make_meme(self, text, output_path, max_phrases):
        """
        Given command line arguments, generates a Doge meme.

        Args:
            text (str): Text to translate into Dogespeak.
            output_path (str): Output path for Doge meme.
            max_phrases (int): Maximum number of phrases.
        """
        translated = self.translator.dogeify_text(text, 0.3, 0.2, max_phrases)
        draw_doge_meme(IMAGE_PATH, output_path, FONT_PATH, translated)
