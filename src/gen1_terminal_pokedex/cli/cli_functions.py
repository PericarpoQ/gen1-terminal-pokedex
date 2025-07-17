"""Module with functions to be used by the CLI."""

import time

import click

from src.gen1_terminal_pokedex.pokemon import Pokemon
from src.gen1_terminal_pokedex.screens.info_screen import get_info_screen
from src.gen1_terminal_pokedex.screens.initial_screen import get_initial_screen
from src.gen1_terminal_pokedex.screens.utils import clear_previous_lines


def setup_initial_screen() -> Pokemon:
    """Print initial screen, validade input and print info screen.

    Returns:
        Pokemon: Pokémon whose screen was generated.

    """
    while True:
        initial_screen = get_initial_screen()
        click.echo(initial_screen)

        user_input = click.prompt(">")

        try:
            pkmn = Pokemon(user_input)
        except ValueError:
            click.echo("Invalid Pokémon, try again!")
            time.sleep(1)
            lines_to_clear = initial_screen.count("\n") + 3
            clear_previous_lines(lines_to_clear)
            continue

        lines_to_clear = initial_screen.count("\n") + 2
        clear_previous_lines(lines_to_clear)

        click.echo(get_info_screen(pkmn))
        pkmn.play_cry()
        break
    return pkmn


def show_options() -> None:
    """Show the options."""
    click.echo("Options → AREA | CRY | LEARNSET | QUIT\n")


def validate_option() -> str:
    """Validate user input for options.

    Returns:
        str: Validated option.

    """
    user_input = click.prompt(">")
    options = ["AREA", "CRY", "LEARNSET", "QUIT"]
    while user_input not in options:
        click.echo("Invalid option, try again!")
        time.sleep(1)
        clear_previous_lines(2)
        user_input = click.prompt(">")
    return user_input
