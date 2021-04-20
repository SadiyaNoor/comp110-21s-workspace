"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730411656"


class Simpy:
    values: list[float]

    # TODO: Your constructor and methods will go here.
    def __init__(self, x: list[float]):
        """Constructs a list when given a set of numbers."""
        self.values = x

    def __repr__(self) -> str:
        return f"Simpy({self.values})"

    def fill()

