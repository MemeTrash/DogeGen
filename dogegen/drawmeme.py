"""
Meme drawing functionality.

Author: Jack Romo <sharrackor@gmail.com>
"""

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import random

MAX_FONT_SIZE = 20
TEXT_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]   # will choose from these randomly


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
    texts = []
    for phrase in phrases:
        new_text = make_drawn_text(
            image,
            phrase,
            font_path,
            texts
        )
        texts.append(new_text)
    for text in texts:
        text.draw(image)
    image.save(to_dir)


def make_drawn_text(image, text, font_path, existing_texts):
    """
    Create DrawnText to draw on image.

    Args:
        image (Image.Image): Image to draw on.
        text (str): Text to draw.
        font_path (str): Directory of font to use.
        existing_texts (list[DrawnText]): List of already existing drawn texts.
    """
    width, height = image.size
    font = get_font(image, text, font_path, 0.3)
    color = random.choice(TEXT_COLORS)
    max_x = width - font.getsize(text)[0]
    max_y = height - font.getsize(text)[1]
    x, y = random.randint(0, max_x), random.randint(0, max_y)
    drawn_text = DrawnText(text, color, font, x, y)
    num_attempts = 0
    while any(drawn_text.intersects(txt) for txt in existing_texts):
        drawn_text.x = random.randint(0, max_x)
        drawn_text.y = random.randint(0, max_y)
        num_attempts += 1
        if num_attempts > 10:
            break
    return drawn_text


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


class DrawnText(object):
    """
    Piece of text to draw on image.
    """

    def __init__(self, contents, color, font, x=0, y=0):
        self.contents = contents
        self.color = color
        self.font = font
        self._x = x
        self._y = y
        self.update_box()

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, new_x):
        self._x = new_x
        self.update_box()

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, new_y):
        self._y = new_y
        self.update_box()

    def update_box(self):
        self._box = (
            self.x,
            self.y,
            self.x + self.font.getsize(self.contents)[0],
            self.y + self.font.getsize(self.contents)[1]
        )

    def draw(self, image):
        """
        Draw self on image.

        Args:
            image (Image.Image): Image to draw self on.
        """
        drawer = ImageDraw.Draw(image)
        drawer.text((self.x, self.y), self.contents, self.color, font=self.font)

    def intersects(self, other):
        """
        Check if self intersects physically with another DrawnText.

        Args:
            other (DrawnText): Other check to check intersection with.

        Returns:
            bool: True if intersecting.
        """
        return self.is_inside_text(other) or other.is_inside_text(self)

    def is_inside_text(self, other):
        """
        Check if self is inside of other DrawnText.

        Args:
            other (DrawnText): Other drawn text to check if self is inside of.

        Returns:
            bool: True if self is partially or fully inside of other box.
        """
        self_corners = [
            (self._box[0], self._box[1]),
            (self._box[0], self._box[3]),
            (self._box[2], self._box[1]),
            (self._box[2], self._box[3])
        ]
        return any(other.point_inside(pnt) for pnt in self_corners)

    def point_inside(self, point):
        """
        Check if point is inside of own bounding box.

        Args:
            point (tuple(int, int)): XY coordinates of point.

        Returns:
            bool: True if point inside of own bounding box.
        """
        px, py = point
        return self._box[0] <= px <= self._box[2] and \
               self._box[1] <= py <= self._box[3]
