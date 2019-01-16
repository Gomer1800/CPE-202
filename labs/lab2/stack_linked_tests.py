# Luis Gomez
# CPE 202

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

    def test_is_empty(self):
        """Creating and testing empty stack"""
        stack = Stack(5)
        self.assertEqual(stack.is_empty(), True)
        """Testing non-empty stack"""
        node1 = Node(1)
        stack = Stack(5, node1)
        self.assertEqual(stack.is_empty(), False)

    def test_is_full(self):
        """Creating full stack"""
        nodes = Node( 1, Node( 2, Node(3, Node(4, Node(5)))))
        stack = Stack(5, nodes) 
        self.assertEqual(stack.is_full(), True)
        """Testing empty stack"""
        stack2 = Stack(5)
        self.assertEqual(stack2.is_full(), False) 

    def test_push(self):
        """Creating half-empty stack"""
        nodes = Node(3, Node (2, Node(1)))
        stack = Stack(4, nodes)
        """Pushing node"""
        stack.push(Node(4))
        self.assertEqual(stack.__repr__(), "Stack(4, Node(4, Node(3, Node(2, Node(1, None)))))")
        """Stack is full, push returns index error"""
        with self.assertRaises(IndexError):
            stack.push( Node(5) )

    def test_pop(self):
        """Create full stack"""
        nodes = Node(4, Node(3, Node (2, Node(1))))
        stack = Stack(4, nodes)
        self.assertEqual(stack.__repr__(), "Stack(4, Node(4, Node(3, Node(2, Node(1, None)))))")
        """Testing if pop returns Node with empty next pointer"""
        self.assertEqual(stack.pop(), Node(4, None) )
        """Stack should now have 1 less item, good!"""
        self.assertEqual(stack.__repr__(), "Stack(4, Node(3, Node(2, Node(1, None))))")
        """Testing empty stack"""
        stack2 = Stack(4)
        with self.assertRaises(IndexError):
            stack2.pop()

    def test_peek(self):
        """Create full stack"""
        nodes = Node(4, Node(3, Node (2, Node(1))))
        stack = Stack(4, nodes)
        self.assertEqual(stack.__repr__(), "Stack(4, Node(4, Node(3, Node(2, Node(1, None)))))")
        """Peek returns Node but next pointer is not affected"""
        self.assertEqual(stack.peek(), Node(4, Node(3, Node (2, Node(1)))))
        """Testing empty stack"""
        stack2 = Stack(4)
        with self.assertRaises(IndexError):
            stack2.peek()

    def test_size(self):
        """Create full stack"""
        four_patties = Node(4, Node(3, Node (2, Node(1))))
        quadruple_big_mac = Stack(4, four_patties)
        self.assertEqual(quadruple_big_mac.__repr__(), "Stack(4, Node(4, Node(3, Node(2, Node(1, None)))))")
        """Testing non-empty stack"""
        self.assertEqual(quadruple_big_mac.size(), 4)
        dumpster_Fire = quadruple_big_mac.pop()
        self.assertEqual(quadruple_big_mac.size(), 3)

        """Testing empty stack"""
        donut_hole = Stack(4)
        self.assertEqual(donut_hole.size(), 0)

if __name__ == '__main__': 
    unittest.main()
