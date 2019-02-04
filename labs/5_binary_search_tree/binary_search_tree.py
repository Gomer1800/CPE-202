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
        pass

    def search(self, key): # returns True if key is in a node of the tree, else False
        pass

    def insert(self, key, data=None): # inserts new node w/ key and data
        # If an item with the given key is already in the BST, 
        # the data in the tree will be replaced with the new data
        # Example creation of node: temp = TreeNode(key, data)
        pass

    def find_min(self): # returns a tuple with min key and data in the BST
        # returns None if the tree is empty
        pass

    def find_max(self): # returns a tuple with max key and data in the BST
        # returns None if the tree is empty
        pass

    def tree_height(self): # return the height of the tree
        # returns None if tree is empty
        pass

    def inorder_list(self): # return Python list of BST keys representing in-order traversal of BST
        pass

    def preorder_list(self):  # return Python list of BST keys representing pre-order traversal of BST
        pass
        
    def level_order_list(self):  # return Python list of BST keys representing level-order traversal of BST
        # You MUST use your queue_array data structure from lab 3 to implement this method
        q = Queue(25000) # Don't change this!
        pass
        

