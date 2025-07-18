"""Module to enter the CLI."""

import os

import click

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

from src.gen1_terminal_pokedex.cli import cli_functions


@click.command()
def cli() -> None:
    """Run the CLI."""
    pokemon = cli_functions.setup_initial_screen()
    user_input = ""
    while user_input != "QUIT":
        if user_input == "AREA":
            cli_functions.change_to_area(pokemon)
        if user_input == "LEARNSET":
            cli_functions.change_to_learnset(pokemon)
        if user_input == "CRY":
            cli_functions.play_pokemon_cry(pokemon)
        if user_input == "INFO":
            cli_functions.change_to_info(pokemon)
        cli_functions.show_options()
        user_input = cli_functions.validate_option()


cli()
