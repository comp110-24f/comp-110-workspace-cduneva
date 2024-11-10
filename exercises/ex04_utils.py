"""Comp110 Utils Exercise 4"""

__author__: str = "730653037"


def all(numbers: list[int], target: int) -> bool:
    if not numbers:
        return False
    for number in numbers:
        if number != target:
            return False
    return True


"""checks to esnure the list contains numbers, then checks numbers"""


def max(numbers: list[int]) -> int:
    if not numbers:
        raise ValueError("max() arg is an empty List")
    """creates error for improper list"""
    largest = numbers[0]
    """sets the largest number with index 0"""
    for number in numbers:
        if number > largest:
            largest = number
    return largest


"""tests the list for the largest number, returns error for bad list"""


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """checks the lengths of the 2 lists to test if equal"""
    if len(list1) != len(list2):
        return False
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False
    return True


def extend(list1: list[int], list2: list[int]) -> None:
    for element in list2:
        list1.append(element)


"""extends the lists with the element"""
