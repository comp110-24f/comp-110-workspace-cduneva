"""Comp110 Utils Exercise 5"""

__author__: str = "730653037"


def only_evens(data: list[int]) -> list[int]:
    new_list = []
    for element in data:
        if element % 2 == 0:
            new_list.append(element)
    return new_list


"""creates list of only even integers from list"""


def sub(data: list[int], start: int, end: int) -> list[int]:
    if len(data) == 0 or start >= len(data) or end <= 0:
        return []

    actual_start = max(0, start)
    """Handle negative start index"""
    actual_end = min(len(data), end)
    """Handle end index exceeding list length"""

    return data[actual_start:actual_end]


"""executes subset function"""


def add_at_index(data: list[int], element: int, index: int) -> None:
    if index < 0 or index > len(data):
        raise IndexError("Index is out of bounds for the input list")
    """Prints the indexerror when the data is out of bounds"""
    data.insert(index, element)
