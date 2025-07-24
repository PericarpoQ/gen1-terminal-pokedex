"""Module with functions to be used by the CLI."""

import time
from typing import Callable

import click

from gen1_terminal_pokedex.pokemon import Pokemon
from gen1_terminal_pokedex.screens.areas_screen import get_area_screen
from gen1_terminal_pokedex.screens.info_screen import get_info_screen
from gen1_terminal_pokedex.screens.initial_screen import get_initial_screen
from gen1_terminal_pokedex.screens.learnset_screen import get_learnset_screen
from gen1_terminal_pokedex.screens.utils import clear_previous_lines


def setup_initial_screen() -> tuple[Pokemon, int]:
    """Print initial screen, validade input and print info screen.

    Returns:
        tuple[Pokemon, int]: Pokémon whose screen was generated and the screen size.

    """
    while True:
        initial_screen = get_initial_screen()
        click.echo(initial_screen)

        user_input = click.prompt(">")

        if user_input == "QUIT":
            clear_previous_lines(initial_screen.count("\n") + 2)
            raise SystemExit

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

        info_screen = get_info_screen(pkmn)
        screen_size = info_screen.count("\n") + 4
        click.echo(info_screen)
        pkmn.play_cry()
        break
    return pkmn, screen_size


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


def change_to_area(pkmn: Pokemon, current_screen_size: int) -> int:
    """Print area screen.

    Args:
        pkmn (Pokemon): Pokémon whose screen is to be displayed.
        current_screen_size (int): The size of the current screen.

    Returns:
        int: Size of the current screen.

    """
    return transition_to_screen(get_area_screen, pkmn, current_screen_size)


def change_to_learnset(pkmn: Pokemon, current_screen_size: int) -> int:
    """Print pokemon learnset screen.

    Args:
        pkmn (Pokemon): Pokémon whose screen is to be displayed.
        current_screen_size (int): The size of the current screen.

    Returns:
        int: Size of the current screen.

    """
    return transition_to_screen(get_learnset_screen, pkmn, current_screen_size)


def change_to_info(pkmn: Pokemon, current_screen_size: int) -> int:
    """Print pokemon info screen.

    Args:
        pkmn (Pokemon): Pokémon whose screen is to be displayed.
        current_screen_size (int): The size of the current screen.

    Returns:
        int: Size of the current screen.

    """
    return transition_to_screen(get_info_screen, pkmn, current_screen_size)


def play_pokemon_cry(pkmn: Pokemon) -> None:
    """Play the pokemon cry.

    Args:
        pkmn (Pokemon): Pokémon whose screen is to be displayed.

    """
    pkmn.play_cry()
    clear_previous_lines(3)


def transition_to_screen(
    screen_function: Callable, pkmn: Pokemon, current_screen_size: int
) -> int:
    """Clear previous screen and print a new one.

    Args:
        screen_function (Callable): Function that generates a new screen.
        pkmn (Pokemon): Pokémon whose screen is to be displayed.
        current_screen_size (int): The size of the current screen.

    Returns:
        int: Size of the current screen.

    """
    new_screen = screen_function(pkmn)

    lines_to_clear = new_screen.count("\n") + 4

    clear_previous_lines(current_screen_size)

    click.echo(new_screen)
    return lines_to_clear


def set_up_cli_loop(pkmn: Pokemon, screen_size: int) -> None:
    """Set up main CLI loop."""
    user_input = ""
    while user_input != "QUIT":
        if user_input == "AREA":
            screen_size = change_to_area(pkmn, screen_size)
        if user_input == "LEARNSET":
            screen_size = change_to_learnset(pkmn, screen_size)
        if user_input == "CRY":
            play_pokemon_cry(pkmn)
        if user_input == "INFO":
            screen_size = change_to_info(pkmn, screen_size)
        show_options()
        user_input = validate_option()
    clear_previous_lines(screen_size)
    pkmn, screen_size = setup_initial_screen()
    set_up_cli_loop(pkmn, screen_size)
