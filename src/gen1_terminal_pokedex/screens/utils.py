"""Utilities module with useful functions."""

import click


def clear_previous_lines(n: int) -> None:
    """Clear previous lines by specifying the number of lines.

    Args:
        n (int): Number of lines to be erased.

    """
    for _ in range(n):
        click.echo("\x1b[1A\x1b[2K", nl=False)
