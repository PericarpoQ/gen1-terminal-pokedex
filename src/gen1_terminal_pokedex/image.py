"""Handles image processing and ASCII art generation for Pokémon sprites.

This module provides functionalities to fetch Pokémon sprite images from a given URL,
process them to remove unnecessary transparent borders, and then convert them into ASCII
art representations.

The primary function, `process_image`, orchestrates this entire workflow, leveraging the
`requests` library for fetching the image, `Pillow` for image manipulation, and
`ascii_magic` for the final conversion to text-based art. This is essential for
displaying Pokémon sprites within a terminal-based PokéDex application.
"""

import io

import ascii_magic
import requests
from PIL import Image, UnidentifiedImageError


def process_image(image_url: str, columns: int = 64) -> str:
    """Process a PNG image from a URL to generate ASCII art.

    This function takes the URL of a PNG file, crops any transparent
    borders, and then converts the result into an ASCII art string.

    Args:
        image_url: The URL of the PNG image file.
        columns: The number of columns for the ASCII art.

    Returns:
        A string containing the generated ASCII art.

    """
    try:
        response = requests.get(image_url, timeout=5)
        response.raise_for_status()  # Raise an exception for bad status codes
        image_data = io.BytesIO(response.content)
        with Image.open(image_data) as img:
            # To avoid overwriting the `with` statement variable, use new variables
            img_for_processing = img.convert("RGBA") if img.mode != "RGBA" else img

            # Get the bounding box of the non-transparent parts
            bbox = img_for_processing.getbbox()

            # Crop the image if a bounding box is found
            final_img = img_for_processing.crop(bbox) if bbox else img_for_processing

            # Generate ASCII art from the cropped image
            return ascii_magic.from_pillow_image(final_img).to_ascii(columns=columns)
    except requests.exceptions.RequestException as e:
        return f"Error fetching image: {e}"
    except UnidentifiedImageError:
        return "Error: The provided file is not a valid image."
