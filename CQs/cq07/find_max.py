__author__ = "730653037"


def find_and_remove_max(list1: list[int]) -> int:
    if not list1:
        return -1
    max_num = max(list1)
    """creates the max number variable"""
    while max_num in list1:
        """deletes the max number variable"""
        list1.remove(max_num)
    return max_num
