# Luis Gomez
# CPE 202
# Node class for use with Stack implemented with linked list
class Node:
    def __init__(self, data, next=None):
        self.data = data    # data held by Node
        self.next = next    # reference to next Node

    def __eq__(self, other):
        return ((type(other) == Node)
          and self.data == other.data
          and self.next == other.next
        )

    def __repr__(self):
        return ("Node({!r}, {!r})".format(self.data, self.next))

class Stack:
    """Implements an efficient last-in first-out Abstract Data Type using a linked list of Nodes"""

    # capacity is max number of Nodes, top is top Node of stack
    def __init__(self, capacity, top=None):
        self.capacity = capacity    # capacity of stack
        self.top = top              # top node of stack
        self.num_items = 0          # number of items in stack
        node = top                  # set number of items based on input
        while node is not None:
            self.num_items += 1
            node = node.next
            if self.num_items > capacity:
                raise IndexError

    def __eq__(self, other):
        return ((type(other) == Stack)
          and self.capacity == other.capacity
          and self.top == other.top
        )

    def __repr__(self):
        return ("Stack({!r}, {!r})".format(self.capacity, self.top))

    def is_empty(self):
        '''Returns True if the stack is empty, and False otherwise
           MUST have O(1) performance'''
        return self.num_items  == 0

    def is_full(self):
        '''Returns True if the stack is full, and False otherwise
           MUST have O(1) performance'''
        return self.num_items == self.capacity

    def push(self, item):
        '''If stack is not full, pushes item on stack. 
           If stack is full when push is attempted, raises IndexError
           MUST have O(1) performance'''
        if self.is_full() is False :
            self.num_items += 1
            item.next = self.top
            self.top = item

        else : raise IndexError

    def pop(self): 
        '''If stack is not empty, pops item from stack and returns item.
           If stack is empty when pop is attempted, raises IndexError
           MUST have O(1) performance'''
        if self.is_empty() is False :
            self.num_items -= 1 
            popped_item = self.top
            self.top = popped_item.next
            popped_item.next = None
            return popped_item

        else : raise IndexError

    def peek(self):
        '''If stack is not empty, returns next item to be popped (but does not pop the item)
           If stack is empty, raises IndexError
           MUST have O(1) performance'''
        if self.is_empty() is False :
            return self.top

        else : raise IndexError

    def size(self):
        '''Returns the number of elements currently in the stack, not the capacity
           MUST have O(1) performance'''
        return self.num_items
 
