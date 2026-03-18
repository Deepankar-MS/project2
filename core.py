"""Core functionality for project2."""

from project1 import greet


def enhanced_greet(name: str) -> str:
    """Return an enhanced greeting using project1."""
    base_greeting = greet(name)
    return f"{base_greeting} Enhanced by project2!"
