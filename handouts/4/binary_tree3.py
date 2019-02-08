# Binary Tree code with traversal and height functions internal to class
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

    def preorder(self):
        print(self.key, end=" ")
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()

    def inorder(self):
        if self.leftChild:
            self.leftChild.inorder()
        print(self.key, end=" ")
        if self.rightChild:
            self.rightChild.inorder()

    def postorder(self):
        if self.leftChild:
            self.leftChild.postorder()
        if self.rightChild:
            self.rightChild.postorder()
        print(self.key, end=" ")

    def height(self):
        if self.leftChild is not None:
            lch = 1 + self.leftChild.height()
        else:
            lch = 0
        if self.rightChild is not None:
            rch = 1 + self.rightChild.height()
        else:
            rch = 0
        return max(lch, rch)

r = BinaryTree('a')

r.insertLeft('b') # insert left child 'b'

r.insertRight('c') # insert right child 'c'

lc = r.getLeftChild()
lc.insertRight('d') # insert right child of 'b' -> 'd'

rc = r.getRightChild()
rc.insertLeft('e') # insert left child of 'c' -> 'e'
rc.insertRight('f') # insert right child of 'c' -> 'f'

print("\npreorder:  ", end="")
r.preorder()

print("\ninorder:   ", end="")
r.inorder()

print("\npostorder: ", end="")
r.postorder()

print("\nheight: ", r.height())