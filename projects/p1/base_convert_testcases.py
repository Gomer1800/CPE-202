"""
Luis Gomez
CPE 202
"""
import unittest
from  base_convert import *

class TestBaseConvert(unittest.TestCase):

    def test_base2(self):
        self.assertEqual(convert(45,2),"101101")
        self.assertEqual(convert(255,2),"11111111")

    def test_base4(self):
        self.assertEqual(convert(30,4),"132")
        self.assertEqual(convert(255,4),"3333")

    def test_base16(self):
        self.assertEqual(convert(316,16),"13C")
        self.assertEqual(convert(255,16),"FF")

    def test_base_EdgeCases(self):
        self.assertEqual(convert(0,2),"0")
        self.assertEqual(convert(0,8),"0")
        self.assertEqual(convert(0,16),"0")

if __name__ == "__main__":
        unittest.main()
