"""Download, store and play the pokemon cry sound."""

from __future__ import annotations

from pathlib import Path

import requests


def download_sound(
    cry_url: str,
    file_name: str | None = None,
    directory: str = "src/gen1_terminal_pokedex/assets",
) -> str:
    """Download a pokemon cry sound file from a URL.

    Args:
        cry_url (str): URL pointed to a sound file.
        file_name (str | None, optional): Name for the file that will be downloaded.
            Defaults to None.
        directory (str, optional): Directory where the downloaded sound will be saved
            to. Defaults to "src/gen1_terminal_pokedex/assets".

    Returns:
        str: Path to downloaded sound file.

    """
    path_dir = Path(directory)
    if not path_dir.exists():
        path_dir.mkdir()

    if file_name is None:
        file_name = cry_url.split("/")[-1]

    file_path = path_dir / file_name

    if not file_path.exists():
        response = requests.get(cry_url, timeout=5)
        response.raise_for_status()
        with file_path.open("wb") as file:
            file.write(response.content)

    return str(file_path)
