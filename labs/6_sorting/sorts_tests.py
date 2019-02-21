import unittest
from sorts import *

class TestLab4(unittest.TestCase):

    def test_simple(self):
        nums = [23, 10]
        comps = selection_sort(nums)
        self.assertEqual(comps, 1)
        self.assertEqual(nums, [10, 23])

    def test_sel_01(self):
        nums = [26, 54, 93, 17, 77, 31, 44, 55, 20]
        comps = selection_sort(nums)
        self.assertEqual(nums, [17, 20, 26, 31, 44, 54, 55, 77, 93])

if __name__ == '__main__': 
    unittest.main()
