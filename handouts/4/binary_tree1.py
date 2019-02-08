# Binary Tree code with examples of access to children
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
print("Root val:", r.getRootKey())
print("Left Child of Root:",r.getLeftChild())
print("Right Child of Root:",r.getRightChild())

r.insertLeft('b') # insert left child 'b'
print("\nLeft Child after insert:",r.getLeftChild())
print("Left Child val:", r.getLeftChild().getRootKey())

r.insertRight('c') # insert right child 'c'
print("\nRight Child after insert:",r.getRightChild())
print("Right Child val:", r.getRightChild().getRootKey())

lc = r.getLeftChild()
lc.insertRight('d') # insert right child of 'b' -> 'd'
print("\nRight Child of Left Child:", r.getLeftChild().getRightChild().getRootKey())

rc = r.getRightChild()
rc.insertLeft('e') # insert left child of 'c' -> 'e'
print("\nLeft Child of Right Child:", r.getRightChild().getLeftChild().getRootKey())
rc.insertRight('f') # insert right child of 'c' -> 'f'
print("Right Child of Left Child:", r.getRightChild().getRightChild().getRootKey())
