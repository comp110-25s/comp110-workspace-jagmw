"""This module defines the River class that simulates fish and bear populations."""

__author__ = "730580305"

from bear import Bear
from fish import Fish
from typing import List


class River:
    """A River that contains both Bears and Fish."""

    def __init__(self, num_fish: int, num_bears: int) -> None:
        """Initialize the River with a starting number of Fish and Bears."""
        self.day: int = 0
        self.fish: List[Fish] = [Fish() for _ in range(num_fish)]
        self.bears: List[Bear] = [Bear() for _ in range(num_bears)]

    def view_river(self) -> None:
        """Print the current day and population of Fish and Bears."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")

    def one_river_day(self) -> None:
        """Simulate one day in the River ecosystem."""
        self.day += 1
        for fish in self.fish:
            fish.one_day()
        for bear in self.bears:
            bear.one_day()
        self.check_ages()
        self.bears_eating()
        self.check_hunger()
        self.repopulate_fish()
        self.repopulate_bears()
        self.view_river()

    def one_river_week(self) -> None:
        """Simulate seven days in the River."""
        for _ in range(7):
            self.one_river_day()

    def check_ages(self) -> None:
        """Remove Fish older than 3 and Bears older than 5."""
        self.fish = [f for f in self.fish if f.age <= 3]
        self.bears = [b for b in self.bears if b.age <= 5]

    def remove_fish(self, amount: int) -> None:
        """Remove the first 'amount' of Fish from the river."""
        self.fish = self.fish[amount:]

    def bears_eating(self) -> None:
        """Each Bear eats 3 fish if there are at least 5 Fish in the river."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)

    def check_hunger(self) -> None:
        """Remove Bears with hunger_score below 0 (they starve)."""
        self.bears = [b for b in self.bears if b.hunger_score >= 0]

    def repopulate_fish(self) -> None:
        """Each pair of Fish produces 4 offspring."""
        new_fish: int = (len(self.fish) // 2) * 4
        self.fish.extend(Fish() for _ in range(new_fish))

    def repopulate_bears(self) -> None:
        """Each pair of Bears produces 1 offspring."""
        new_bears: int = len(self.bears) // 2
        self.bears.extend(Bear() for _ in range(new_bears))
