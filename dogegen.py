import sys
import dogegen

FONT_PATH = "./resources/comic_sans_font.ttf"
IMAGE_PATH = "./resources/doge_orig.jpg"


def main(args):
    """
    Given command line arguments, generates a Doge meme.

    Args:
        args (list[str]): List of command line arguments.
    """
    text = args[1]
    output_path = args[2]
    max_phrases = int(args[3])
    translated = dogegen.dogeify_text(text, 0.3, 0.2, max_phrases)
    dogegen.draw_doge_meme(IMAGE_PATH, output_path, FONT_PATH, translated)

if __name__ == "__main__":
    main(sys.argv)
