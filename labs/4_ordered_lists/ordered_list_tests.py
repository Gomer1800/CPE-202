import unittest
from ordered_list import *

class TestLab4(unittest.TestCase):

    def test_simple(self):
        t_list = OrderedList()
        t_list.add(10)
        self.assertEquals(t_list.python_list(), [10])
        self.assertEquals(t_list.size(), 1)
        self.assertEquals(t_list.index(10), 0)
        self.assertTrue(t_list.search(10))
        self.assertFalse(t_list.is_empty())
        self.assertEquals(t_list.python_list_reversed(), [10])
        self.assertTrue(t_list.remove(10))
        self.assertTrue(t_list.is_empty())
        with self.assertRaises(IndexError):
            t_list.python_list()
        t_list.add(10)
        self.assertEquals(t_list.pop(0), 10)

if __name__ == '__main__': 
    unittest.main()
