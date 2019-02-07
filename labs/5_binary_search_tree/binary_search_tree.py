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
            if parent.left is None: return False
            # recursive left
            return self.search_helper(key, parent.left)
        # is key > parent
        elif key > parent.key:
            # base case, is right empty?
            if parent.right is None: return False
            # recursive right
            return self.search_helper(key, parent.right)
        else: raise Exception("search_helper error")

    def insert(self, key, data=None): # inserts new node w/ key and data
        # If an item with the given key is already in the BST, 
        # the data in the tree will be replaced with the new data
        # Example creation of node: temp = TreeNode(key, data)
        if data is None: raise ValueError("Cant insert. data = None")
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
            if parent.left is None:
                # create new node(key, data) = left
                parent.left = TreeNode(key, data)
            # recursive left
            self.insert_helper(key, data, parent.left)
        # is key > parent
        elif key > parent.key:
            # base case, right is empty
            if parent.right is None:
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
        if parent.left is not None:
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
        if parent.right is not None:
            # recursive right 
            return self.find_min_helper(parent.right)
        # base case, rightmost leaf reached
        return (parent.key, parent.data)

    def tree_height(self): # return the height of the tree
        # returns None if tree is empty
        if self.is_empty(): return None
        else: return self.tree_height(self.root)

    def tree_height_helper(self, parent, count=0):
        """
        recursive method, returns int
        Explores left and right branches of existing nodes
        returns largest running count after branches/leaves are exhausted
        """
        # left node exist?
        if parent.left is not None:
            # increment count
            # recursive left
            left_count = self.tree_height_helper(count+1, parent.left)
            if left_count > count: count = left_count
        # right node exist?
        if parent.right is not None:
            # increment count
            # recursive right
            right_count = self.tree_height_helper(count+1, parent.right)
            if right_count > count: count = right_count
        # base case, parent is leaf
        else: return count

    def inorder_list(self): # (smallest to largest key)
        # return Python list of BST keys representing in-order traversal of BST (
        pass

    def preorder_list(self): # Explores in following order (CURRENT, LEFT, RIGHT)
        # return Python list of BST keys representing pre-order traversal of BST
        pass
        
    def level_order_list(self):  # (breadth first search)
        # return Python list of BST keys representing level-order traversal of BST
        # You MUST use your queue_array data structure from lab 3 to implement this method
        q = Queue(25000) # Don't change this!
        pass
