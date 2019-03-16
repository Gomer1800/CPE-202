"""
Luis Gomez
Python Data Structures

Useful protip for this project, used diff file1.txt file2.txt. Saved my life when
comparing the declarationg of independance Concordance results
"""
import unittest
import filecmp
from concordance import *

class TestList(unittest.TestCase):

   def test_01(self):
       conc = Concordance()
       conc.load_stop_table("stop_words.txt")
       # print("Test stop table: ",conc.stop_table.hash_table)
       conc.load_concordance_table("file1.txt")
       # print("Test con table: ",conc.concordance_table.hash_table)
       conc.write_concordance("file1_con.txt")
       self.assertTrue(filecmp.cmp("file1_con.txt", "file1_sol.txt"))

   def test_02(self):
       conc = Concordance()
       conc.load_stop_table("stop_words.txt")
       conc.load_concordance_table("file2.txt")
       conc.write_concordance("file2_con.txt")
       self.assertTrue(filecmp.cmp("file2_con.txt", "file2_sol.txt"))

   def test_03(self):
       conc = Concordance()
       conc.load_stop_table("stop_words.txt")
       conc.load_concordance_table("declaration.txt")
       conc.write_concordance("declaration_con.txt")
       self.assertTrue(filecmp.cmp("declaration_con.txt", "declaration_sol.txt"))

if __name__ == '__main__':
   unittest.main()