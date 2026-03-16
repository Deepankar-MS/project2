"""Core functionality for proj2."""

from proj1 import greet


def enhanced_greet(name: str) -> str:
    """Return an enhanced greeting using proj1."""
    base_greeting = greet(name)
    return f"{base_greeting} Enhanced by proj2!"
