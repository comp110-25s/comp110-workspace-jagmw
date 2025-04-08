"""Dictionary utility functions for EX03."""

__author__ = "730580305"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of a dictionary. Raises KeyError if duplicate values exist."""
    result: dict[str, str] = {}
    for key, value in input_dict.items():
        if value in result:
            raise KeyError(f"Duplicate key detected when inverting: {value}")
        result[value] = key
    return result


def count(values: list[str]) -> dict[str, int]:
    """Counts how many times each string appears in a list."""
    result: dict[str, int] = {}
    for item in values:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result


def favorite_color(favorites: dict[str, str]) -> str:
    """Returns the most frequent favorite color. If tie, returns the first encountered."""
    color_counts = count(list(favorites.values()))
    max_count = 0
    fav_color = ""
    for name in favorites:
        color = favorites[name]
        if color_counts[color] > max_count:
            fav_color = color
            max_count = color_counts[color]
    return fav_color


def bin_len(words: list[str]) -> dict[int, set[str]]:
    """Groups words by their lengths into sets."""
    result: dict[int, set[str]] = {}
    for word in words:
        length = len(word)
        if length not in result:
            result[length] = set()
        result[length].add(word)
    return result
