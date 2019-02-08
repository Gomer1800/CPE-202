"""
Author: Luis Gomez
CPE 202
"""
from queue_array import Queue

class TreeNode:
    def __init__(self, key, data, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right

    def __eq__(self, other):
        return ((type(other) == TreeNode)
                and self.key == other.key
                and self.data == other.data
                and self.left == other.left
                and self.right == other.right
                )

    def __repr__(self):
        return ("TreeNode({!r}, {!r}, {!r}, {!r})".format(self.key, self.data, self.left, self.right))

class BinarySearchTree:

    def __init__(self): # Returns empty BST
        self.root = None

    def is_empty(self): # returns True if tree is empty, else False
        return self.root == None # if there is no root, then the tree must be empty

    def search(self, key): # returns True if key is in a node of the tree, else False
        if self.is_empty(): raise IndexError("Cannot search an empty binary tree")
        else: return self.search_helper(key, self.root)
    
    def search_helper(self, key, parent):
        """
        recursive helper method for BST search(), returns boolean. 
        Returns True if key is found in binary Tree, returns False if not found. Raises Exception otherwise...
        """
        # base case, key = parent
        if key == parent.key: return True
        # is key < parent
        elif key < parent.key:
            # base case, is left empty?
            if parent.left == None: return False
            # recursive left
            return self.search_helper(key, parent.left)
        # is key > parent
        elif key > parent.key:
            # base case, is right empty?
            if parent.right == None: return False
            # recursive right
            return self.search_helper(key, parent.right)
        else: raise Exception("search_helper error")

    def insert(self, key, data=None): # inserts new node w/ key and data
        # If an item with the given key is already in the BST, 
        # the data in the tree will be replaced with the new data
        # Example creation of node: temp = TreeNode(key, data)
        if data == None: raise ValueError("Cant insert. data = None")
        elif self.is_empty(): self.root = TreeNode(key, data)
        else: self.insert_helper(key, data, self.root)

    def insert_helper(self, key, data, parent):
        """
        recursive helper method for BST insert(), returns nothing.
        Searches through binary tree for available position for (key, data), 
        creates new leaf if key available, if key already exists replaces data
        """
        # base case, key = parent
        if key == parent.key: 
            # replace current node data
            parent.data = data
        # is key < parent
        elif key < parent.key:
            # base case, left is empty
            if parent.left == None:
                # create new node(key, data) = left
                parent.left = TreeNode(key, data)
            # recursive left
            self.insert_helper(key, data, parent.left)
        # is key > parent
        elif key > parent.key:
            # base case, right is empty
            if parent.right == None:
                # create new node(key, data) = right
                parent.right =  TreeNode(key, data)
            # recursive right
            self.insert_helper(key, data, parent.right)
        else: raise Exception("insert_helper error")

    def find_min(self): # returns a tuple with min key and data in the BST
        # returns None if the tree is empty
        if self.is_empty(): return None
        else: return self.find_min_helper(self.root)

    def find_min_helper(self, parent):
        # does left node exist?
        if parent.left != None:
            # recursive left
            return self.find_min_helper(parent.left)
        # base case, leftmost leaf reached
        return (parent.key, parent.data)

    def find_max(self): # returns a tuple with max key and data in the BST
        # returns None if the tree is empty
        if self.is_empty(): return None
        else: return self.find_max_helper(self.root)

    def find_max_helper(self, parent):
        # does right node exist?
        if parent.right != None:
            # recursive right 
            return self.find_max_helper(parent.right)
        # base case, rightmost leaf reached
        return (parent.key, parent.data)

    def tree_height(self): # return the height of the tree
        # returns None if tree is empty
        if self.is_empty(): return None
        else: return self.tree_height_helper(self.root)

    def tree_height_helper(self, parent, count=0):
        """
        recursive method, returns int
        Explores left and right branches of existing nodes
        returns largest running count after branches/leaves are exhausted
        """
        height = count
        # left node exist?
        if parent.left != None:
            # increment count
            # recursive left
            left_count = self.tree_height_helper(parent.left, count+1)
            if left_count > count: height = left_count
        # right node exist?
        if parent.right != None:
            # increment count
            # recursive right
            right_count = self.tree_height_helper(parent.right, count+1)
            if right_count > count: height = right_count
        # base case, parent is leaf
        return height

    def inorder_list(self): # (smallest to largest key)
        # return Python list of BST keys representing in-order traversal of BST (
        if self.is_empty(): raise IndexError("Inorder not possible, empty tree")
        key_list = []
        return self.inorder_list_helper(self.root, key_list)

    def inorder_list_helper(self, parent, key_list):
        # is left empty?
        if parent.left != None:
            # False, recursive call left
            key_list = self.inorder_list_helper(parent.left, key_list)
        # add self key to list
        key_list.append(parent.key)
        # is right empty?
        if parent.right != None:
            # False, recursive call right
            key_list = self.inorder_list_helper(parent.right, key_list)
        # base case, return list
        return key_list

    def preorder_list(self): # Explores in following order (CURRENT, LEFT, RIGHT)
        # return Python list of BST keys representing pre-order traversal of BST
        if self.is_empty(): raise IndexError("Preorder not possible, empty tree")
        key_list = []
        return self.preorder_list_helper(self.root, key_list)

    def preorder_list_helper(self, parent, key_list):
        # add self key to list
        key_list.append(parent.key)
        # is left empty?
        if parent.left != None:
            # False, recursive left
            key_list = self.preorder_list_helper(parent.left, key_list)
        # is right empty?
        if parent.right != None:
            # False, recursive right
            key_list = self.preorder_list_helper(parent.right, key_list)
        # base case, return list
        return key_list

    def level_order_list(self):  # (breadth first search)
        # return Python list of BST keys representing level-order traversal of BST
        # You MUST use your queue_array data structure from lab 3 to implement this method
        if self.is_empty(): raise IndexError("levelorder not possible, empty tree")
        key_list = []
        q = Queue(25000) # Don't change this!
        HEIGHT = self.tree_height_helper(self.root)
        for desired_level in range(HEIGHT+1):
            q = self.level_order_list_helper(q, self.root, HEIGHT, desired_level)
        while q.size() != 0:
            key_list.append(q.dequeue())
        return key_list

    def level_order_list_helper(self, q, parent, tree_height, count):
        # is tree height - parent height = count ?
        if tree_height -  self.tree_height_helper(parent) == count:
            # True, base case, reached desired level
            q.enqueue(parent.key)
            return q
        # is left empty?
        if parent.left != None:
            # False, recursive left
            q = self.level_order_list_helper(q, parent.left, tree_height, count)
        # is right empty?
        if parent.right != None:
            # False, recursive right
            q = self.level_order_list_helper(q, parent.right, tree_height, count)
        # base case, all branches exhausted
        return q
