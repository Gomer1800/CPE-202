# Luis Gomez
# CPE 202
import unittest

from queue_linked import Queue

class TestLab1(unittest.TestCase):
    def test_queue(self):
        '''Trivial test to ensure method names and parameters are correct'''
        q = Queue(5)
        q.is_empty()
        q.is_full()
        q.enqueue('thing')
        q.dequeue()
        q.size()
    
    def test_repr(self):
        """Creating empty queue"""
        my_q = Queue(4)
        """enqueueing node"""
        my_q.enqueue('Luis')
        my_q.enqueue('Gomez')
        my_q.enqueue('is')
        my_q.enqueue('chill')
        self.assertEqual(my_q.__repr__(), "Queue(4, Node('Luis', Node('Gomez', Node('is', Node('chill', None)))))")

    def test_eq(self):
        c = 'WHAT'
        my_q = Queue(2)
        my_q.enqueue(c)
        my_q2 = Queue(2)
        my_q2.enqueue(c)
        self.assertEquals(my_q.__eq__(my_q2), True)

    def test_is_empty(self): # DONE
        """Created and testing empty queue"""
        my_q = Queue(5)
        self.assertTrue(my_q.is_empty())
        self.assertEqual(my_q.__repr__(), "Queue(5, None)")
        """Testing non-empty queue"""
        my_q.enqueue(3)
        self.assertFalse(my_q.is_empty())

    def test_is_full(self): # DONE
        """Creating full queue"""
        my_q = Queue(5)
        my_q.enqueue(100)
        my_q.enqueue(-100)
        my_q.enqueue(-95)
        my_q.enqueue(100.5)
        my_q.enqueue(0)
        self.assertTrue(my_q.is_full())
        """Testing empty queue"""
        my_q2 = Queue(5)
        self.assertFalse(my_q2.is_full()) 
    
    def test_enqueue(self):
        """Creating empty queue"""
        my_q = Queue(4)
        """enqueueing node"""
        my_q.enqueue('Luis')
        my_q.enqueue('Gomez')
        my_q.enqueue('is')
        my_q.enqueue('chill')
        """queue is full, enqueue returns index error"""
        with self.assertRaises(IndexError):
            my_q.enqueue(4)

    def test_dequeue(self):
        """Create full queue"""
        my_q = Queue(5)
        my_q.enqueue('C')
        my_q.enqueue('-')
        my_q.enqueue(3)
        my_q.enqueue('P')
        my_q.enqueue('O')
        self.assertEqual(my_q.__repr__(), "Queue(5, Node('C', Node('-', Node(3, Node('P', Node('O', None))))))")
        """Testing if dequeue returns Node with empty next pointer"""
        self.assertEqual(my_q.dequeue(), 'C')
        """queue should now have 1 less item, good!"""
        self.assertEqual(my_q.__repr__(), "Queue(5, Node('-', Node(3, Node('P', Node('O', None)))))")
        """Testing empty queue"""
        my_q2 = Queue(4)
        with self.assertRaises(IndexError):
            my_q2.dequeue()

    def test_size(self):
        my_q = Queue(5)
        my_q.enqueue('C')
        my_q.enqueue('-')
        my_q.enqueue(3)
        self.assertTrue(my_q.size(), 3)

if __name__ == '__main__': 
    unittest.main()
