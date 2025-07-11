"""Module to create the pokemon areas screen."""

from src.gen1_terminal_pokedex.pokemon import Pokemon


def get_area_screen(pokemon: Pokemon) -> str:
    """Generate string that represents pokemon encounter areas as a screen.

    Args:
        pokemon (Pokemon): Pokemon object whose screen will be created.

    Returns:
        str: Areas to be printed as a screen.

    """
    p = pokemon

    total_width = 132
    left_width = total_width // 2
    right_width = (total_width - left_width) - 1

    content_height = len(p.image.splitlines())

    title = f"{p.id} - {p.name.upper()}"
    centered_title = title.center(total_width)

    def format_area(area: str) -> str:
        area = area.replace("-", " ")
        area = area.replace(" area", "")
        return area.title()

    right_subtitle = [
        "║ " + "AREAS FOUND".center(right_width - 1),
        f"╠{'═' * right_width}╣",
    ]
    formatted_areas = ["", ""] + [format_area(area) for area in p.areas]

    right_lines = formatted_areas
    right_lines += [""] * (content_height - len(right_lines))
    left_lines = p.image.splitlines()
    left_lines += [""] * (content_height - len(left_lines))

    screen = []
    screen.append(f"╔{'═' * total_width}╗")
    screen.append(f"║{centered_title}║")
    screen.append(f"╠{'═' * left_width}╦{'═' * right_width}╣")

    initial_rows_missing = 0
    for lft, rgt in zip(left_lines, right_lines):
        if initial_rows_missing == 1:
            screen.append(
                f"║ {lft.ljust(left_width - 1)}\033[0m"
                f" {right_subtitle[initial_rows_missing]}"
            )
            initial_rows_missing += 1
        elif initial_rows_missing == 0:
            screen.append(
                f"║ {lft.ljust(left_width - 1)}\033[0m"
                f" {right_subtitle[initial_rows_missing]}║"
            )
            initial_rows_missing += 1
        else:
            screen.append(
                f"║ {lft.ljust(left_width - 1)}\033[0m ║ {rgt.ljust(right_width - 1)}║"
            )

    screen.append(f"║{' ' * left_width}║{' ' * right_width}║")
    screen.append(f"║{' ' * left_width}║{' ' * right_width}║")
    screen.append(f"╚{'═' * left_width}╩{'═' * right_width}╝")
    return "\n".join(screen)
