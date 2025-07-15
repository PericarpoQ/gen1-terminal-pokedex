"""Module to create the pokemon initial screen."""

from src.gen1_terminal_pokedex.screens.utils import LOGO


def get_initial_screen() -> str:
    """Generate string that represents the pokemon initial menu as a screen.

    Returns:
        str: initial menu to be printed as a screen.

    """
    total_width = 132
    screen = []

    logo_lines = LOGO.copy()

    screen.append(f"╔{'═' * total_width}╗")

    for line in logo_lines:
        padding = (total_width - 70) // 2
        screen.append(
            f"║{' ' * padding}{line.center(total_width - padding)}{' ' * padding}║"
        )

    screen.append(f"╠{'═' * total_width}╣")

    prompt = "Welcome to the Terminal Pokédex. Insert a Pokémon name or number.".center(
        total_width
    )
    screen.append(f"║{prompt}║")
    screen.append(f"╚{'═' * total_width}╝")

    return "\n".join(screen)
