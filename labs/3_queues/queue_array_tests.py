import unittest
from queue_array import Queue

class TestLab3(unittest.TestCase):
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
        self.assertEqual(my_q.__repr__(), "Queue(4, ['Luis', 'Gomez', 'is', 'chill'])")

    def test_eq(self):
        my_q = Queue(2)
        my_q.enqueue('T')
        my_q2 = Queue(2)
        my_q2.enqueue('T')
        self.assertTrue(my_q.__eq__(my_q2))

    def test_is_empty(self): # DONE
        """Created and testing empty queue"""
        my_q = Queue(5)
        self.assertTrue(my_q.is_empty())
        self.assertEqual(my_q.__repr__(), "Queue(5, [])")
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

if __name__ == '__main__': 
    unittest.main()
