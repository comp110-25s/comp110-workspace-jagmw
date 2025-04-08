"""Unit tests for dictionary functions in ex03."""

__author__ = "730580305"

import pytest
from exercises.ex03.dictionary import invert, count, favorite_color, bin_len


def test_invert_normal_case():
    """Tests a typical case with unique values."""
    assert invert({"a": "x", "b": "y"}) == {"x": "a", "y": "b"}


def test_invert_single_pair():
    """Tests inversion with only one key-value pair."""
    assert invert({"hello": "world"}) == {"world": "hello"}


def test_invert_duplicate_values():
    """Tests for KeyError when duplicate values exist in the input dict."""
    with pytest.raises(KeyError):
        invert({"a": "1", "b": "1"})


def test_count_repeated_items():
    """Tests counting items with duplicates."""
    assert count(["a", "b", "a"]) == {"a": 2, "b": 1}


def test_count_unique_items():
    """Tests counting items with no duplicates."""
    assert count(["apple", "banana", "cherry"]) == {
        "apple": 1,
        "banana": 1,
        "cherry": 1,
    }


def test_count_empty_list():
    """Tests counting an empty list."""
    assert count([]) == {}


def test_favorite_color_normal_case():
    """Tests finding the most common color."""
    favorites = {"Alice": "blue", "Bob": "blue", "Charlie": "red"}
    assert favorite_color(favorites) == "blue"


def test_favorite_color_tie():
    """Tests tie case: first encountered color should be returned."""
    favorites = {"Alice": "red", "Bob": "blue", "Charlie": "blue", "Dave": "red"}
    assert favorite_color(favorites) == "red"


def test_favorite_color_one_person():
    """Tests when only one favorite color is given."""
    assert favorite_color({"Alice": "green"}) == "green"


def test_bin_len_normal_case():
    """Tests grouping words by length with unique values."""
    assert bin_len(["hi", "cat", "sun"]) == {2: {"hi"}, 3: {"cat", "sun"}}


def test_bin_len_duplicates():
    """Tests that duplicates do not create multiple entries."""
    assert bin_len(["yo", "yo", "no"]) == {2: {"yo", "no"}}


def test_bin_len_empty_list():
    """Tests behavior with an empty input list."""
    assert bin_len([]) == {}
