# Binary Tree code with traversal and height functions external to class
class BinaryTree:
    def __init__(self,key):
        self.key = key
        self.leftChild = None
        self.rightChild = None

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootKey(self,obj):
        self.key = obj

    def getRootKey(self):
        return self.key

    def insertLeft(self,key):
        if self.leftChild == None:
            self.leftChild = BinaryTree(key)
        else:
            t = BinaryTree(key)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,key):
        if self.rightChild == None:
            self.rightChild = BinaryTree(key)
        else:
            t = BinaryTree(key)
            t.rightChild = self.rightChild
            self.rightChild = t

r = BinaryTree('a')

r.insertLeft('b') # insert left child 'b'
r.insertRight('c') # insert right child 'c'

lc = r.getLeftChild()
lc.insertRight('d') # insert right child of 'b' -> 'd'

rc = r.getRightChild()
rc.insertLeft('e') # insert left child of 'c' -> 'e'
rc.insertRight('f') # insert right child of 'c' -> 'f'

def preorder(tree):
    if tree:
        print(tree.getRootKey(), end=" ")
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

def inorder(tree):
    if tree:
        inorder(tree.getLeftChild())
        print(tree.getRootKey(), end=" ")
        inorder(tree.getRightChild())

def postorder(tree):
    if tree:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootKey(), end=" ")

print("\npreorder:  ", end="")
preorder(r)

print("\ninorder:   ", end="")
inorder(r)

print("\npostorder: ", end="")
postorder(r)

def height(tree):
    if tree is None:
        return -1
    else:
        return 1 + max(height(tree.getLeftChild()), height(tree.getRightChild()))

print("\nheight: ", height(r))