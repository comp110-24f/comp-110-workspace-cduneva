"""Mutating functions."""

__author__ = "730653037"
list_1 = [1, 2, 3]
list_2 = list_1


def manual_append(list1: list[int], appendage: int) -> None:
    list1.append(appendage)


def double(list1: list[int]) -> None:
    i = 0
    while i < len(list1):
        list1[i] *= 2
        i += 1


double(list_2)
print(list_1)
print(list_2)
