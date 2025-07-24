"""Module to create the pokemon information screen."""

from gen1_terminal_pokedex.pokemon import Pokemon


def get_info_screen(pokemon: Pokemon) -> str:
    """Generate string that represents pokemon information as a screen.

    Args:
        pokemon (Pokemon): Pokemon object whose screen will be created.

    Returns:
        str: Information to be printed as a screen.

    """
    p = pokemon

    total_width = 132
    left_width = total_width // 2
    right_width = (total_width - left_width) - 1

    title = f"{p.id} - {p.name.upper()}"
    centered_title = title.center(total_width)

    types = ", ".join([p.type1] + ([p.type2] if p.type2 else []))

    sprite_lines = p.image.splitlines()
    max_sprite_lines = len(sprite_lines)

    info_lines = [
        f"Types: {types}",
        f"Genus: {p.genus}",
        f"Height: {p.height} m",
        f"Weight: {p.weight} kg",
    ]
    info_list = []
    info_list.append(f"╔{'═' * total_width}╗")
    info_list.append(f"║{centered_title}║")
    info_list.append(f"╠{'═' * left_width}╦{'═' * right_width}╣")

    for i in range(max_sprite_lines):
        left = sprite_lines[i].center(left_width)
        right = (
            info_lines[i].ljust(right_width - 1)
            if i < len(info_lines)
            else " " * (right_width - 1)
        )
        info_list.append(f"║ {left} \033[0m║ {right}║")

    info_list.append(f"╠{'═' * left_width}╩{'═' * right_width}╣")

    flavor_line = f" {p.flavor_text}".ljust(total_width)
    info_list.append(f"║{flavor_line}║")

    info_list.append(f"╚{'═' * total_width}╝")

    return "\n".join(info_list)
