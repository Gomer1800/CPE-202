"""
Author: Luis Gomez
"""
import unittest
from ordered_list import *

class TestLab4(unittest.TestCase):

    def test_simple(self):
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
        t_list = OrderedList()
        with self.assertRaises(IndexError):
            t_list.reverse_rec()

if __name__ == '__main__': 
    unittest.main()
