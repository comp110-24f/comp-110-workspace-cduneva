import unittest
from utils import only_evens, sub, add_at_index

"""Comp110 Utils tests 5"""

__author__: str = "730653037"


class TestListFunctions(unittest.TestCase):

    def test_only_evens_empty(self) -> None:
        """tests w empty list"""
        self.assertEqual(only_evens([]), [])

    def test_only_evens_all_even(self) -> None:
        """tests w all even list"""
        self.assertEqual(only_evens([2, 4, 6]), [2, 4, 6])
        self.assertEqual(only_evens([2, 4, 6]), [2, 4, 6])

    def test_only_evens_mixed(self) -> None:
        """tests w mixed list"""
        data = [1, 2, 3, 4, 5, 6]
        self.assertEqual(only_evens(data), [2, 4, 6])
        self.assertEqual(data, [1, 2, 3, 4, 5, 6])

    def test_sub_empty(self) -> None:
        """tests w empty list"""
        self.assertEqual(sub([], 0, 1), [])

    def test_sub_normal(self) -> None:
        """tests w normal list"""
        self.assertEqual(sub([1, 2, 3, 4, 5], 1, 4), [2, 3, 4])
        data = [1, 2, 3, 4, 5]
        self.assertEqual(sub(data, 1, 4), [2, 3, 4])

    def test_sub_out_of_bounds(self) -> None:
        """tests w out of bounds ints"""
        self.assertEqual(sub([1, 2, 3, 4, 5], 10, 20), [])

    def test_add_at_index_normal(self) -> None:
        """tests with normal list"""
        data = [1, 2, 3, 4, 5]
        add_at_index(data, 6, 2)
        self.assertEqual(data, [1, 2, 6, 3, 4, 5])

    def test_add_at_index_beginning(self) -> None:
        """tests w add at beginning"""
        data = [1, 2, 3]
        add_at_index(data, 0, 0)
        self.assertEqual(data, [0, 1, 2, 3])

    def test_add_at_index_end(self) -> None:
        """tests adding at the end"""
        data = [1, 2, 3]
        add_at_index(data, 4, 3)
        self.assertEqual(data, [1, 2, 3, 4])

    def test_add_at_index_error(self) -> None:
        """tests to ensure error prints"""
        data = [1, 2, 3]
        with self.assertRaises(IndexError):
            add_at_index(data, 4, 10)
