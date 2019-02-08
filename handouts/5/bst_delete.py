# Code for delete operation - based on Lab 5 implementation

def delete(self, key):  # deletes node containing key, return True if deleted, False otherwise
    return self.delete_helper(key, self.root, None)

def delete_helper(self, key, node, parent):
    found = False
    cur = node
    while cur is not None and not found:
        if key < cur.key:
            parent = cur
            cur = cur.left
        elif key > cur.key:
            parent = cur
            cur = cur.right
        else:
            found = True
    if not found:
        return False
    # cur is node to delete
    if cur.left is None and cur.right is None:  # leaf node
        if parent == None:  # root Node with no children
            self.root = None
        elif cur == parent.left:
            parent.left = None
        else:
            parent.right = None
    elif cur.left is not None and cur.right is not None:  # node has both children
        min = self.find_min_node(cur.right)
        cur.key = min.key
        cur.data = min.data
        self.delete_helper(cur.key, cur.right, cur)
    elif cur.left is not None:  # has just a left child
        if parent is None:  # is the root
            self.root = cur.left
        elif parent.left == cur:  # is a left child
            parent.left = cur.left
        else:  # is a right child
            parent.right = cur.left

    else:  # has just a right child
        if parent is None:  # is the root
            self.root = cur.right
        elif parent.left == cur:  # is a left child
            parent.left = cur.right
        else:  # is a right child
            parent.right = cur.right
    return True
