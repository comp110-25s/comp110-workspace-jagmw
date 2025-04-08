"""This program will plsn a cozy tea party."""

__author__: str = "730580305"


def main_planner(guests: int) -> None:
    """Brings all functions together"""
    print("A cozy tea party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """calculates the number of tea bags needed based on the number of guests."""
    return people * 2


def treats(people: int) -> int:
    """calculates the number of treats needed bases on teas"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """calculates the total cost of tea bags and treats."""
    return tea_count * 0.50 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
