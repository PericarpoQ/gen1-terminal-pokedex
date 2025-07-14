"""Module to create the pokemon initial screen."""

from src.gen1_terminal_pokedex.pokemon import Pokemon


def get_initial_screen(pokemon: Pokemon) -> str:
    """Generate string that represents the pokemon initial menu as a screen.

    Args:
        pokemon (Pokemon): Pokemon object whose screen will be created.

    Returns:
        str: initial menu to be printed as a screen.

    """
    p = pokemon
    total_width = 132
    title = f"{p.id} - {p.name.upper()}"
    centered_title = title.center(total_width)

    menu_options = ["1 - Information", "2 - Learnset", "3 - Areas Found"]

    screen = []
    screen.append(f"╔{'═' * total_width}╗")
    screen.append(f"║{centered_title}║")
    screen.append(f"╠{'═' * total_width}╣")

    for option in menu_options:
        line = option.center(total_width)
        screen.append(f"║{line}║")

    screen.append(f"╚{'═' * total_width}╝")
    return "\n".join(screen)
