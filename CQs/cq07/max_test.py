__author__ = "730653037"

from find_max import find_and_remove_max

"""imports the function being tested"""


def test_find_and_remove_max_returns_expected_value():
    input_list = [1, 5, 2, 5, 3]
    expected_max = 5
    actual_max = find_and_remove_max(input_list)
    assert actual_max == expected_max


"""tests to ensure the right value is returned"""


def test_find_and_remove_max_mutates_input_correctly():
    input_list = [1, 5, 2, 5, 3]
    find_and_remove_max(input_list)
    assert 5 not in input_list


"""tests to ensure the list mutates correctly"""


def test_find_and_remove_max_edge_case_empty_list():
    input_list = []
    expected_max = -1
    actual_max = find_and_remove_max(input_list)
    assert actual_max == expected_max


"""tests edge cases"""
