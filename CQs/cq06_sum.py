"""Summing the elements of a list using different loops"""

__author__ = "730653037"


def w_sum(vals: list[float]) -> float:
    total = 0.0
    idx = 0
    """creating teh variables for index and total"""
    while idx < len(vals):
        total += vals[idx]
        idx += 1
        """cycles through the list to add all of the variables"""
    return total


"""iterates through a list to add all the variables"""


def f_sum(vals: list[float]) -> float:
    total = 0.0
    for val in vals:
        total += val
    return total


"""simple adds all the values in the list"""


def f_range_sum(vals: list[float]) -> float:
    total = 0.0
    for i in range(len(vals)):
        """adds all the elements in a list of floats using the for in loop"""
        total += vals[i]
    return total
