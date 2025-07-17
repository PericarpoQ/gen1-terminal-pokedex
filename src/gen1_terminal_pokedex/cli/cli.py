"""Module to enter the CLI."""

import os

import click

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

from src.gen1_terminal_pokedex.cli import cli_functions


@click.command()
def cli() -> None:
    """Run the CLI."""
    cli_functions.setup_initial_screen()
    cli_functions.show_options()
    cli_functions.validate_option()


cli()
