# Luis Gomez
# CPE 202 Location Class Test Cases, Lab 1

import unittest
from location import *

class TestLocation(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")

    def test_repr2(self):
        loc2 = Location("Burbank", 34.2, -118.3)
        self.assertEqual(repr(loc2),"Location('Burbank', 34.2, -118.3)")

    # Add more tests!
    
    def test_eq(self):
        loc = Location("SLO", 35.3, -120.7)
        loc2 = Location("SLO", 35.3, -120.7) 
        self.assertTrue(loc == loc2)
    
    def test_eq2(self):
        loc = Location("SLO", 35.3, -120.7)
        loc2 = Location("Burbank", 34.2, -118.3) 
        self.assertFalse(loc == loc2)

if __name__ == "__main__":
        unittest.main()
