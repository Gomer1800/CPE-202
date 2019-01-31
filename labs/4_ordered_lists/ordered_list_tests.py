"""
Author: Luis Gomez
CPE 202
"""
import unittest
from ordered_list import *

class TestLab4(unittest.TestCase):

    def test_simple(self):
        """
        Trivial demonstration of Ordered List methods
        """
        t_list = OrderedList()
        t_list.add(10)
        self.assertEqual(t_list.python_list(), [10])
        self.assertEqual(t_list.size(), 1)
        self.assertEqual(t_list.index(10), 0)
        self.assertTrue(t_list.search(10))
        self.assertFalse(t_list.is_empty())
        self.assertEqual(t_list.python_list_reversed(), [10])
        self.assertTrue(t_list.remove(10))
        self.assertTrue(t_list.is_empty())
        with self.assertRaises(IndexError):
            t_list.python_list()
        t_list.add(10)
        self.assertEqual(t_list.pop(0), 10)

    def test_is_empty(self):
        """
        Here I load and unload values into the Ordered List and execute various methods, 
        showing how is_empty() consistently provides a valid result.
        """
        t_list = OrderedList()
        self.assertTrue(t_list.is_empty())
        t_list.add(3.14)
        self.assertFalse(t_list.is_empty())
        self.assertEqual(t_list.python_list_reversed(), [3.14])
        self.assertTrue(t_list.remove(3.14))
        self.assertTrue(t_list.is_empty())
        t_list.add(5.0)
        self.assertFalse(t_list.is_empty())
        self.assertEqual(t_list.pop(0), 5.0)
        self.assertTrue(t_list.is_empty())

    def test_add(self):
        """
        Here, I add values to the Ordered List.
        The user need not add values in a natural order, 
        the Ordered List will sort items during the add() method. Redundant values are not added
        """
        t_list = OrderedList()
        with self.assertRaises(ValueError):
            t_list.add(None)
        t_list.add(3.14)
        self.assertEqual(t_list.python_list(), [3.14])
        t_list.add(1.0)
        self.assertEqual(t_list.python_list(), [1.0, 3.14])
        t_list.add(2.785)
        self.assertEqual(t_list.python_list(), [1.0, 2.785, 3.14])
        t_list.add(2.785)
        self.assertEqual(t_list.python_list(), [1.0, 2.785, 3.14])
        t_list.add(3)
        self.assertEqual(t_list.python_list(), [1.0, 2.785, 3, 3.14])

    def test_remove(self):
        """
        Here I removed items from a populated Ordered List.
        The Ordered List preserves natural ordering despite removing items in random order.
        """
        t_list = OrderedList()
        with self.assertRaises(IndexError):
            t_list.remove(None)
        t_list.add(99.9)
        t_list.add(28)
        t_list.add(55.31)
        t_list.add(42.1)
        self.assertEqual(t_list.python_list(), [28, 42.1, 55.31, 99.9])
        self.assertFalse(t_list.remove(100))
        self.assertEqual(t_list.python_list(), [28, 42.1, 55.31, 99.9])
        self.assertTrue(t_list.remove(28))
        self.assertEqual(t_list.python_list(), [42.1, 55.31, 99.9])
        self.assertTrue(t_list.remove(55.31))
        self.assertEqual(t_list.python_list(), [42.1, 99.9])
        self.assertTrue(t_list.remove(99.9))
        self.assertEqual(t_list.python_list(), [42.1])

    def test_index(self):
        """
        Here I populate an Ordered List in random fashion. 
        I then show that index() returns the correct index according to natural ordering.
        I then remove a single item and show that index() continues to work effectively
        """
        t_list = OrderedList()
        with self.assertRaises(IndexError):
            t_list.index(0)
        t_list.add(39.6)
        with self.assertRaises(ValueError):
            t_list.index(None)
        t_list.add(99.9)
        t_list.add(28)
        t_list.add(55.31)
        t_list.add(42.1)
        self.assertEqual(t_list.python_list(), [28, 39.6, 42.1, 55.31, 99.9])
        self.assertEqual(t_list.index(39.6), 1)
        self.assertEqual(t_list.index(99.9), 4)
        self.assertEqual(t_list.index(28), 0)
        self.assertEqual(t_list.index(55.31), 3)
        self.assertEqual(t_list.index(42.1), 2)
        t_list.remove(39.6)
        self.assertEqual(t_list.index(99.9), 3)
        self.assertEqual(t_list.index(55.31), 2)
        self.assertEqual(t_list.index(42.1), 1)

    def test_pop(self):
        """
        Here randomly pop the items of an Ordered List. Natural Ordering is presevered and the Ordered List removes the popped item.
        """
        t_list = OrderedList()
        with self.assertRaises(IndexError):
            t_list.pop(0)
        t_list.add(39.6)
        t_list.add(1)
        t_list.add(30)
        t_list.add(.5)
        self.assertEqual(t_list.python_list(), [.5, 1, 30, 39.6])
        with self.assertRaises(ValueError):
            t_list.pop(None)
        with self.assertRaises(IndexError):
            t_list.pop(-1)
        with self.assertRaises(IndexError):
            t_list.pop(4)
        self.assertEqual(t_list.pop(2), 30)
        self.assertEqual(t_list.python_list(), [.5, 1, 39.6])
        self.assertEqual(t_list.pop(0), .5)
        self.assertEqual(t_list.python_list(), [1, 39.6])
        self.assertEqual(t_list.pop(1), 39.6)
        self.assertEqual(t_list.python_list(), [1])
        self.assertEqual(t_list.pop(0), 1)
        self.assertTrue(t_list.is_empty())

    def test_search(self):
        """
        Here I show that the search() method effectively detects the presence of an item in the Ordered List. If the item is not present, then the method returns False.
        """
        t_list = OrderedList()
        with self.assertRaises(IndexError):
            t_list.search(0)
        t_list.add(39.6)
        t_list.add(1)
        t_list.add(30)
        t_list.add(.5)
        with self.assertRaises(ValueError):
            t_list.search(None)
        self.assertTrue(t_list.search(1))
        self.assertTrue(t_list.search(.5))
        self.assertTrue(t_list.search(39.6))
        self.assertTrue(t_list.search(30))
        self.assertFalse(t_list.search(30.1))

    def test_python_list(self):
        """
        Here I incrementally add and remove items from  an Ordered List. 
        With each step I shoe the python list representation with natural ordering preserved
        """
        t_list = OrderedList()
        t_list.add(99.9)
        self.assertEqual(t_list.python_list(), [99.9])
        t_list.add(28)
        self.assertEqual(t_list.python_list(), [28, 99.9])
        t_list.add(55.31)
        self.assertEqual(t_list.python_list(), [28, 55.31, 99.9])
        t_list.add(42.1)
        self.assertEqual(t_list.python_list(), [28, 42.1, 55.31, 99.9])
        self.assertFalse(t_list.remove(100))
        self.assertEqual(t_list.python_list(), [28, 42.1, 55.31, 99.9])
        self.assertTrue(t_list.remove(28))
        self.assertEqual(t_list.python_list(), [42.1, 55.31, 99.9])
        self.assertTrue(t_list.remove(55.31))
        self.assertEqual(t_list.python_list(), [42.1, 99.9])
        self.assertTrue(t_list.remove(99.9))
        self.assertEqual(t_list.python_list(), [42.1])

    def test_size(self):
        """
        Here I randomly populate an Ordered List, printing out the size with each step.
        I then randomly depopulate the Ordered List and show that the size is correctly calculated too.
        """
        t_list = OrderedList()
        with self.assertRaises(IndexError):
            t_list.size()
        t_list.add(99.9)
        self.assertEqual(t_list.size(), 1)
        t_list.add(28)
        self.assertEqual(t_list.size(), 2)
        t_list.add(55.31)
        self.assertEqual(t_list.size(), 3)
        t_list.add(42.1)
        self.assertEqual(t_list.size(), 4)
        self.assertTrue(t_list.remove(28))
        self.assertEqual(t_list.size(), 3)
        self.assertTrue(t_list.remove(42.1))
        self.assertEqual(t_list.size(), 2)
        self.assertTrue(t_list.remove(55.31))
        self.assertEqual(t_list.size(), 1)
        self.assertTrue(t_list.remove(99.9))
        self.assertTrue(t_list.is_empty())

    def test_reverse_rec(self):
        """
        Here I randomly populate an Ordered List and show that python_list_reversed() works.
        I then randomly depopulate the Ordered List and test the reversed list
        """
        t_list = OrderedList()
        with self.assertRaises(IndexError):
            t_list.python_list_reversed()
        t_list.add(99.9)
        self.assertEqual(t_list.python_list_reversed(), [99.9])
        t_list.add(28)
        self.assertEqual(t_list.python_list_reversed(), [99.9, 28])
        t_list.add(55.31)
        self.assertEqual(t_list.python_list_reversed(), [99.9, 55.31, 28])
        t_list.add(42.1)
        self.assertEqual(t_list.python_list_reversed(), [99.9, 55.31, 42.1, 28])
        self.assertTrue(t_list.remove(28))
        self.assertEqual(t_list.python_list_reversed(), [99.9, 55.31, 42.1])
        self.assertTrue(t_list.remove(55.31))
        self.assertEqual(t_list.python_list_reversed(), [99.9, 42.1])
        self.assertTrue(t_list.remove(99.9))
        self.assertEqual(t_list.python_list(), [42.1])
        self.assertTrue(t_list.remove(42.1))
        self.assertTrue(t_list.is_empty())

if __name__ == '__main__': 
    unittest.main()
