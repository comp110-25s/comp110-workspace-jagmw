"""This module runs the river simulation with an initial population."""

__author__ = "730580305"

from river import River

# Create a River with 10 Fish and 2 Bears
my_river: River = River(10, 2)

# View initial status
my_river.view_river()

# Simulate one week in the river
my_river.one_river_week()
