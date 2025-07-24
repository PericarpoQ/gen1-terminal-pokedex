"""Module to create the pokemon learnset screen."""

from gen1_terminal_pokedex.pokemon import Pokemon


def get_learnset_screen(pokemon: Pokemon) -> str:
    """Generate string that represents pokemon learnset as a screen.

    Args:
        pokemon (Pokemon): Pokemon object whose screen will be created.

    Returns:
        str: Learnset to be printed as a screen.

    """
    p = pokemon

    total_width = 132
    left_width = total_width // 2
    right_width = (total_width - left_width) - 1

    content_height = len(p.image.splitlines())

    title = f"{p.id} - {p.name.upper()}"
    centered_title = title.center(total_width)

    level_up_moves = sorted(
        [m for m in p.learnset if m["method"] == "level-up"], key=lambda m: m["level"]
    )
    machine_moves = sorted(
        [m for m in p.learnset if m["method"] == "machine"], key=lambda m: m["move"]
    )

    left_lines = [
        f"{m['level']:>2} - {m['move'].replace('-', ' ').title()}"
        for m in level_up_moves
    ]
    right_lines = [f"{m['move'].replace('-', ' ').title()}" for m in machine_moves]

    max_lines = max(len(left_lines), len(right_lines))
    padded_lines = max(max_lines, content_height)

    left_lines += [""] * (padded_lines - len(left_lines))
    right_lines += [""] * (padded_lines - len(right_lines))

    screen = []
    screen.append(f"╔{'═' * total_width}╗")
    screen.append(f"║{centered_title}║")
    screen.append(f"╠{'═' * left_width}╦{'═' * right_width}╣")

    left_subtitle = "LEVEL-UP".center(left_width)
    right_subtitle = "MACHINE".center(right_width)
    screen.append(f"║{left_subtitle}║{right_subtitle}║")
    screen.append(f"╠{'═' * left_width}╬{'═' * right_width}╣")

    for lft, rgt in zip(left_lines, right_lines):
        screen.append(f"║ {lft.ljust(left_width - 1)}║ {rgt.ljust(right_width - 1)}║")

    screen.append(f"╚{'═' * left_width}╩{'═' * right_width}╝")
    return "\n".join(screen)
