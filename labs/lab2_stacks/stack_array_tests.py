# Luis Gomez
# CPE 202

import unittest
from stack_array import Stack
        
class TestLab2(unittest.TestCase):

    def test_init(self):
        stack = Stack(5)
        self.assertEqual(stack.items, [None]*5)
        self.assertEqual(stack.capacity, 5)

        stack = Stack(5, [1, 2])
        self.assertEqual(stack.items[0:2], [1, 2])
        self.assertEqual(stack.capacity, 5)

        with self.assertRaises(IndexError):
            Stack(5, [1, 2, 3, 4, 5, 6])

    def test_eq(self):
        stack1 = Stack(5)
        stack2 = Stack(5)
        stack3 = Stack(10)
        stack4 = Stack(5,[1, 2])
        self.assertEqual(stack1, stack2)
        self.assertNotEqual(stack1, stack3)
        self.assertNotEqual(stack1, stack4)

    def test_repr(self):
        stack = Stack(5, [1, 2])
        self.assertEqual(stack.__repr__(), "Stack(5, [1, 2])")

    def test_is_empty(self):
        """Creating and testing empty stack"""
        stack = Stack(5)
        self.assertEquals(stack.is_empty(), True)
        """Testing non-empty stack"""
        stack2 = Stack(5, [5, 4, 3, 2])
        self.assertEquals(stack2.is_empty(), False)

    def test_is_full(self):
        """Creating and testing full stack"""
        stack = Stack(6, [5, 4, 3, 2, 1, 0])
        self.assertEquals(stack.is_full(), True)
        """Testing non-full stacks"""
        stack2 = Stack(6)
        self.assertEquals(stack2.is_full(), False)
        stack3 = Stack(6, [1])
        self.assertEquals(stack3.is_full(), False)

    def test_push(self):
        """Creating non-full stack"""
        stack = Stack(5, [1, 2, 4])
        """Pushing 5 then -1 on non-full stack"""
        stack.push(5)
        self.assertEqual(stack.__repr__(), "Stack(5, [1, 2, 4, 5])")
        self.assertEqual(stack.items[0:4], [1, 2, 4, 5])
        self.assertEqual(stack.capacity, 5)
        
        stack.push(-1)
        self.assertEqual(stack.__repr__(), "Stack(5, [1, 2, 4, 5, -1])")
        self.assertEqual(stack.items[0:5], [1, 2, 4, 5, -1])
        self.assertEqual(stack.capacity, 5)
        """Stack is full, now testing indexError when calling push"""
        with self.assertRaises(IndexError):
            stack.push(0)

    def test_pop(self):
        """Empty stack will return indexError when popping"""
        stack = Stack(5, [])
        with self.assertRaises(IndexError):
            stack.pop()
        """Testing non-empty stacks, item is removed from the stack"""
        stack.push(-1000)
        self.assertEqual(stack.__repr__(), "Stack(5, [-1000])")
        self.assertEqual(stack.pop(), -1000)
        self.assertEqual(stack.__repr__(), "Stack(5, [])")
        
        stack2 = Stack(5, [1, 2, 3, 4, 5])
        self.assertEqual(stack2.__repr__(), "Stack(5, [1, 2, 3, 4, 5])")
        self.assertEqual(stack2.pop(), 5)
        self.assertEqual(stack2.__repr__(), "Stack(5, [1, 2, 3, 4])")

    def test_peek(self):
        """Cant peek if you're empty *points finger at own head*, peek returns index error"""
        stack = Stack(5, [])
        with self.assertRaises(IndexError):
            stack.peek()
        """Testing non-empty stacks. Peek returns the item & does not remove item from stack"""
        stack.push(-1000)
        self.assertEqual(stack.__repr__(), "Stack(5, [-1000])")
        self.assertEqual(stack.peek(), -1000)
        self.assertEqual(stack.__repr__(), "Stack(5, [-1000])")
        
        stack2 = Stack(5, [1, 2, 3, 4, 5])
        self.assertEqual(stack2.__repr__(), "Stack(5, [1, 2, 3, 4, 5])")
        self.assertEqual(stack2.peek(), 5)
        self.assertEqual(stack2.__repr__(), "Stack(5, [1, 2, 3, 4, 5])")

    def test_size(self):
        """Testing empty stack"""
        stack = Stack(3, [])
        self.assertEqual(stack.size(), 0)
        """testing non-empty stack"""
        stack.push(2)
        self.assertEqual(stack.size(), 1)
        self.assertNotEqual(stack.size(), stack.capacity)

if __name__ == '__main__': 
    unittest.main()
