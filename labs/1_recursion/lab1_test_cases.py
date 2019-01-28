# Luis Gomez
# CPE 202 Lab 1 Test Cases

import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """add description here"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
    
    def test_max_list_iter_2(self):
        """Tests function with an array of ints and floats with no ordering"""
        tlist = [10, 9, 11, 0, 100.1, 100]
        self.assertEqual(max_list_iter(tlist), 100.1)

    def test_reverse_rec(self):
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
    
    def test_reverse_rec_2(self):
        """Tests function using an array of numbers, chars, and strings"""
        self.assertEqual(reverse_rec([1,'A', 1.0, "0x10", -5]),[-5,"0x10",1.0,'A',1])

    def test_bin_search(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )

    def test_bin_search_2(self):
        """Tests function with array of negative and postive ints, searching for value 7 @ index 3"""
        list_val =[-5, -1, 3, 7, 100]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(7, 0, len(list_val)-1, list_val), 3 )
        self.assertEqual(bin_search(-1, 0, len(list_val)-1, list_val), 1 )

    def test_bin_search_3(self):
        """Tests function with targets not found in list, expects None"""
        list_val =[-5, -1, 3, 3.9, 4.1, 7, 100]
        low = 0
        high = len(list_val)-1
        with self.assertRaises(ValueError):
            bin_search(4, 0, len(list_val)-1, list_val)
        with self.assertRaises(ValueError):
            bin_search(-6, 0, len(list_val)-1, list_val)

    def test_bin_search_4(self):
        """Tests boundary conditions"""
        list_val =[-5, -1, 3, 3.9, 4.1, 7, 100, 100.5]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(100.5, 0, len(list_val)-1, list_val), len(list_val)-1)
        self.assertEqual(bin_search(-5, 0, len(list_val)-1, list_val), 0)

if __name__ == "__main__":
        unittest.main()

    
