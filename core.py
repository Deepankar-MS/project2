"""Core functionality for project2."""

from project1 import greet


def enhanced_greet(name: str) -> str:
    """Return an enhanced greeting using project1."""
    base_greeting = greet(name)
    return f"{base_greeting} Enhanced by project2!"


def format_message(message: str, style: str = "default") -> str:
    """Format a message with different styles.
    
    Args:
        message: The message to format
        style: One of 'default', 'uppercase', 'title', 'reverse'
    
    Returns:
        Formatted message string
    """
    if style == "uppercase":
        return message.upper()
    elif style == "title":
        return message.title()
    elif style == "reverse":
        return message[::-1]
    return message


def add_prefix(text: str, prefix: str = "[INFO]") -> str:
    """Add a prefix to text.
    
    Args:
        text: The text to prefix
        prefix: The prefix to add (default: [INFO])
    
    Returns:
        Prefixed text string
    """
    return f"{prefix} {text}"


def count_words(text: str) -> int:
    """Count the number of words in a text.
    
    Args:
        text: The text to count words in
    
    Returns:
        Number of words
    """
    return len(text.split())
