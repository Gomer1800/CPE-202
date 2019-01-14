import unittest
from stack_linked import *
        
class TestLab2(unittest.TestCase):

    def test_node_init(self):
        node1 = Node(1)
        self.assertEqual(node1.data, 1)
        self.assertEqual(node1.next, None)

        node2 = Node(2, node1)
        self.assertEqual(node2.data, 2)
        self.assertEqual(node2.next, node1)

    def test_node_eq(self):
        node1a = Node(1)
        node1b = Node(1)
        node2a = Node(2, node1a)
        node2b = Node(2, node1b)

        self.assertEqual(node1a, node1b)
        self.assertNotEqual(node1a, node2a)
        self.assertEqual(node2a, node2b)
        node1a = Node(3)
        self.assertNotEqual(node1a, node1b)

    def test_node_repr(self):
        node = Node(2, Node(1, None))
        self.assertEqual(node.__repr__(), "Node(2, Node(1, None))")

    def test_stack_init(self):
        stack = Stack(5)
        self.assertEqual(stack.top, None)
        self.assertEqual(stack.capacity, 5)

        init_stack = Node(2, Node(1, None))
        stack = Stack(5, init_stack)
        self.assertEqual(stack.top, init_stack)
        self.assertEqual(stack.capacity, 5)

        with self.assertRaises(IndexError):
            Stack(5, Node(6, Node(5, Node(4, Node(3, Node(2, Node(1, None)))))))

    def test_stack_eq(self):
        stack1 = Stack(5)
        stack2 = Stack(5)
        stack3 = Stack(10)
        init_stack = Node(2, Node(1, None))
        stack4 = Stack(5, init_stack)
        self.assertEqual(stack1, stack2)
        self.assertNotEqual(stack1, stack3)
        self.assertNotEqual(stack1, stack4)

    def test_stack_repr(self):
        init_stack = Node(2, Node(1, None))
        stack = Stack(5, init_stack)
        self.assertEqual(stack.__repr__(), "Stack(5, Node(2, Node(1, None)))")

if __name__ == '__main__': 
    unittest.main()
