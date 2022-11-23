"""This file contains functions related to pillow"""
from PIL import ImageFont
from PIL.ImageDraw import Draw
from qrcode.image.pil import PilImage
from config import Config
from file_operations import get_current_working_directory, join_path


def save_image(image: PilImage, destination_path: str) -> None:
    """Saves image to a given path"""

    image.save(destination_path)


def add_text_to_image(image: PilImage, text: str, coords: tuple) -> PilImage:
    """add text to the image"""

    font_path = join_path([get_current_working_directory(), Config.TEXT_FONT])
    title_font = ImageFont.truetype(font_path, 14)

    Draw(image).text(coords, text=text, font=title_font)

    return image


def watermark(image: PilImage) -> PilImage:
    """adds watermark to image"""

    text = "- " + Config.IMAGE_WATER_MARK
    return add_text_to_image(image, text, (350, 430))
