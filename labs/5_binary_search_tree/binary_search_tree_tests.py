"""
Author: Luis Gomez
CPE 202
"""
import unittest
from binary_search_tree import *

class TestLab4(unittest.TestCase):

    def test_simple(self):
        bst = BinarySearchTree()
        self.assertTrue(bst.is_empty())
        bst.insert(10, 'stuff')
        self.assertTrue(bst.search(10))
        self.assertEqual(bst.find_min(), (10, 'stuff'))
        bst.insert(10, 'other')
        self.assertEqual(bst.find_max(), (10, 'other'))
        self.assertEqual(bst.tree_height(), 0)
        self.assertEqual(bst.inorder_list(), [10])
        self.assertEqual(bst.preorder_list(), [10])
        self.assertEqual(bst.level_order_list(), [10])

    def test_height_1(self):
        bst = BinarySearchTree()
        self.assertTrue(bst.is_empty())
        bst.insert(50, 'root')
        bst.insert(25, 'left')
        bst.insert(75, 'right')
        self.assertTrue(bst.search(25))
        self.assertTrue(bst.search(75))
        self.assertEqual(bst.find_min(), (25, 'left'))
        self.assertEqual(bst.find_max(), (75, 'right'))
        self.assertEqual(bst.tree_height(), 1)
        self.assertEqual(bst.inorder_list(), [25, 50, 75])
        self.assertEqual(bst.preorder_list(), [50, 25, 75])
        self.assertEqual(bst.level_order_list(), [50, 25, 75])
    
    def test_height_2(self):
        bst = BinarySearchTree()
        self.assertTrue(bst.is_empty())
        bst.insert(50, 'root')
        bst.insert(25, 'l1')
        bst.insert(75, 'r1')
        bst.insert(89, 'r2')
        bst.insert(12, 'l2')
        bst.insert(26, 'r2')
        bst.insert(67, 'l2')
        self.assertTrue(bst.search(25))
        self.assertTrue(bst.search(75))
        self.assertTrue(bst.search(67))
        self.assertTrue(bst.search(26))
        self.assertTrue(bst.search(12))
        self.assertTrue(bst.search(89))
        self.assertEqual(bst.find_min(), (12, 'l2'))
        self.assertEqual(bst.find_max(), (89, 'r2'))
        self.assertEqual(bst.tree_height(), 2)
        self.assertEqual(bst.inorder_list(), [12, 25, 26, 50, 67, 75, 89])
        self.assertEqual(bst.preorder_list(), [50, 25, 12, 26, 75, 67, 89])
        self.assertEqual(bst.level_order_list(), [50, 25, 75, 12, 26, 67, 89])

if __name__ == '__main__': 
    unittest.main()
