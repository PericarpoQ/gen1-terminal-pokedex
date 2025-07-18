"""Module with functions to be used by the CLI."""

import time
from typing import Callable

import click

from src.gen1_terminal_pokedex.pokemon import Pokemon
from src.gen1_terminal_pokedex.screens.areas_screen import get_area_screen
from src.gen1_terminal_pokedex.screens.info_screen import get_info_screen
from src.gen1_terminal_pokedex.screens.initial_screen import get_initial_screen
from src.gen1_terminal_pokedex.screens.learnset_screen import get_learnset_screen
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
    click.echo("Options → AREA | CRY | INFO | LEARNSET | QUIT\n")


def validate_option() -> str:
    """Validate user input for options.

    Returns:
        str: Validated option.

    """
    user_input = click.prompt(">")
    options = ["AREA", "CRY", "LEARNSET", "QUIT", "INFO"]
    while user_input not in options:
        click.echo("Invalid option, try again!")
        time.sleep(1)
        clear_previous_lines(2)
        user_input = click.prompt(">")
    return user_input


def change_to_area(pkmn: Pokemon) -> None:
    """Print area screen.

    Args:
        pkmn (Pokemon): Pokémon whose screen is to be displayed.

    """
    transition_to_screen(get_area_screen, pkmn)


def change_to_learnset(pkmn: Pokemon) -> None:
    """Print pokemon learnset screen.

    Args:
    pkmn (Pokemon): Pokémon whose screen is to be displayed.

    """
    transition_to_screen(get_learnset_screen, pkmn)


def change_to_info(pkmn: Pokemon) -> None:
    """Print pokemon info screen.

    Args:
    pkmn (Pokemon): Pokémon whose screen is to be displayed.

    """
    transition_to_screen(get_info_screen, pkmn)


def play_pokemon_cry(pkmn: Pokemon) -> None:
    """Play the pokemon cry.

    Args:
        pkmn (Pokemon): Pokémon whose screen is to be displayed.

    """
    pkmn.play_cry()
    clear_previous_lines(3)


def transition_to_screen(screen_function: Callable, pkmn: Pokemon) -> None:
    """Clear previous screen and print a new one.

    Args:
        screen_function (Callable): Function that generates a new screen.
        pkmn (Pokemon): Pokémon whose screen is to be displayed.

    """
    new_screen = screen_function(pkmn)

    lines_to_clear = new_screen.count("\n") + 4

    clear_previous_lines(lines_to_clear)

    click.echo(new_screen)
