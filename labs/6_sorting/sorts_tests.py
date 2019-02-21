import unittest
from sorts import *
import time

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

    def test_sel_02(self):
        nums = [26]
        comps = selection_sort(nums)
        self.assertEqual(nums, [26])

    def test_sel_03(self):
        nums = [54, 54]
        comps = selection_sort(nums)
        self.assertEqual(nums, [54, 54])

    def test_insert_01(self):
        nums = [54, 26, 93, 17, 77, 31, 44, 55, 20]
        comps = insertion_sort(nums)
        self.assertEqual(nums, [17, 20, 26, 31, 44, 54, 55, 77, 93])

    def test_insert_02(self):
        nums = [54]
        comps = insertion_sort(nums)
        self.assertEqual(nums, [54])

    def test_insert_03(self):
        nums = [54, 54]
        comps = insertion_sort(nums)
        self.assertEqual(nums, [54, 54])

if __name__ == '__main__': 
    unittest.main()
