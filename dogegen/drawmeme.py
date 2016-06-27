"""
Meme drawing functionality.

Author: Jack Romo <sharrackor@gmail.com>
"""

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import random

MAX_FONT_SIZE = 20


def draw_doge_meme(from_dir, to_dir, font_path, phrases):
    """
    Draw a doge meme, given an image path and text to draw on it.

    Args:
        from_dir (str): Directory of template doge image.
        to_dir (str): Path where to store result, including file name and extension.
        font_path (str): Directory of font to use.
        phrases (list[str]): Doge phrases to draw onto image.
    """
    image = Image.open(from_dir)
    text_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
    for phrase in phrases:
        draw_text_on(image, phrase, font_path, random.choice(text_colors))
    image.save(to_dir)


def draw_text_on(image, text, font_path, color):
    """
    Draw piece of text on opened image.

    Args:
        image (Image.Image): Image to draw on.
        text (str): Text to draw.
        font_path (str): Directory of font to use.
        color (tuple(int, int, int)): Color of text.
    """
    width, height = image.size
    font = get_font(image, text, font_path, 0.3)
    drawer = ImageDraw.Draw(image)
    max_x = width - font.getsize(text)[0]
    max_y = height - font.getsize(text)[1]
    coords = random.randint(0, max_x), random.randint(0, max_y)
    drawer.text(coords, text, color, font=font)


def get_font(image, text, font_path, img_width_fraction):
    """
    Get desired font for image.

    Args:
        image (Image.Image): Image being drawn on.
        text (str): Text being drawn.
        font_path (str): Path to font.
        img_width_fraction (float): Fraction of image's width that text's width should be.

    Returns:
        ImageFont.Font: Font to draw text with.
    """
    width, height = image.size
    font_size = 1
    font = ImageFont.truetype(font_path, font_size)
    # +1 is to ensure font size is below requirement
    while (font.getsize(text)[0]+1) < img_width_fraction*width and font_size < MAX_FONT_SIZE:
        font_size += 1
        font = ImageFont.truetype(font_path, font_size)
    return font
