"""Module to enter the CLI."""

import os

import click

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

from gen1_terminal_pokedex.cli import cli_functions


@click.command()
def cli() -> None:
    """Run the CLI."""
    pokemon, screen_size = cli_functions.setup_initial_screen()
    cli_functions.set_up_cli_loop(pokemon, screen_size)


cli()
