"""This module defines the Fish class used in the river simulation."""

__author__ = "730580305"


class Fish:
    """A Fish that lives in the river ecosystem."""

    def __init__(self) -> None:
        """Initialize a Fish with age 0."""
        self.age: int = 0

    def one_day(self) -> None:
        """Simulate one day for the Fish: age increases."""
        self.age += 1
