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

    def fill(self, fill_val: float, val2_fill: int) -> None:
        fillist = []
        length = len(self.values)
        for i in range(val2_fill):
            fillist.append(fill_val)
        self.values = fillist

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        assert step != 0.0
        newlist = []
        i = start
        if step > 0:
            while i < stop: 
                newlist.append(i)
                i += step
        else:
            while i > stop:
                newlist.append(i)
                i += step
        self.values = newlist

    def sum(self) -> float:
        return sum(self.values)

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        newlist = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for item in range(len(self.values)):
                newlist.append(self.values[item] + rhs.values[item])
            return Simpy(newlist)
        else: 
            for item in self.values:
                newlist.append(item + rhs)
            return Simpy(newlist)

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        newlist = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for item in range(len(self.values)):
                newlist.append(self.values[item] ** rhs.values[item])
        else:
            for item in self.values:
                newlist.append(item ** rhs)
        return Simpy(newlist)

    def __mod__(self, rhs: Union[float, Simpy]) -> Simpy:
        newlist = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for item in range(len(self.values)):
                    newlist.append(self.values[item] % rhs.values[item])
            return Simpy(newlist)
        else: 
            for item in self.values:
                newlist.append(item % rhs)
            return Simpy(newlist)

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        newlist: list[bool] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for item in range(len(self.values)):
                    newlist.append(self.values[item] == rhs.values[item])
            return newlist
        else: 
            for item in self.values:
                newlist.append(item == rhs)
            return newlist
    
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        newlist: list[bool] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for item in range(len(self.values)):
                    newlist.append(self.values[item] > rhs.values[item])
            return newlist
        else: 
            for item in self.values:
                newlist.append(item > rhs)
            return newlist
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        result = []
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            for i in range(len(self.values)):
                if rhs[i]:
                    result.append(self.values[i])
            return Simpy(result)
