class Node:
    """Node for use with doubly-linked list"""
    def __init__(self, item, next=None, prev=None):
        self.item = item  # item held by Node
        self.next = next  # reference to next Node
        self.prev = prev  # reference to previous Node

class OrderedList:
    """A doubly-linked ordered list of integers, 
    from lowest (head of list, sentinel.next) to highest (tail of list, sentinel.prev)"""
    def __init__(self, sentinel=None):
        """Use only a sentinel Node. No other instance variables"""
        self.sentinel = Node(None)
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel

    def is_empty(self):
        """Returns back True if OrderedList is empty"""
        return sentinel.next == self.sentinel and sentinel.prev == self.sentinel

    def add(self, item):
        """Adds an item to OrderedList, in the proper location based on ordering of items
        from lowest (at head of list) to highest (at tail of list)
        If item is already in list, do not add again (no duplicate items)"""
        # is the head self.sentinel? add item anywhere
        if self.is_empty():
            self.sentinel.next, self.sentinel.prev = item, item
            return
        # compare item to head and tail, place accordingly

    def remove(self, item):
        """Removes an item from OrderedList. If item is removed (was in the list) returns True
        If item was not removed (was not in the list) returns False"""

    def index(self, item):
        """Returns index of an item in OrderedList (assuming head of list is index 0).
        If item is not in list, return None"""
        # is list empty?
        if self.is_empty(): return
        # is item duplicate?

    def pop(self, index):
        """Removes and returns item at index (assuming head of list is index 0).
        If index is negative or >= size of list, raises IndexError"""

    def search(self, item): # RECURSIVE, DONE
        """Searches OrderedList for item, returns True if item is in list, False otherwise"""
        if self.is_empty(): raise IndexError
        temp = self.python_list()
        result = self.bin_search(item, 0, temp.len()-1, temp)
        if result is not None: return True
        else: return False

    def python_list(self): # DONE
        """Return a Python list representation of OrderedList, from head to tail
        For example, list with integers 1, 2, and 3 would return [1, 2, 3]"""
        # Empty list?
        if self.is_empty(): raise Value
        node_list = [self.sentinel.head]
        for node in node_list:
            if node.next is not None:
                node_list.append(node.next)
        return [node.item for node in node_list]

    def python_list_reversed(self): # RECURSIVE
        """Return a Python list representation of OrderedList, from tail to head, using recursion
        For example, list with integers 1, 2, and 3 would return [3, 2, 1]"""

    def size(self): # RECURSIVE, NOT DONE YET
        """Returns number of items in the OrderedList"""
        if self.is_empty(): raise IndexError
        return self.python_list().len()

    def bin_search(target, low, high, item_list): # HELPER FUNCTION
        """Recursively searches for target in item_list. Returns index if found, None if not found. If item_list is empty, raises IndexError"""
        # EMPTY LIST
        if item_list is None: raise IndexError

        mid = (low + high) // 2 # determines mid index
        # BASE CASES
        if item_list[mid] == target: return mid
        if item_list[high] == target: return high
        if item_list[low] == target: return low
        if low == high-2: return None

        # check upper half
        if target > item_list[mid]:
            result  = bin_search(target, mid, high, item_list)
            return result
        # check lower half
        elif target < item_list[mid]:
            result = bin_search(target, low, mid, item_list)
            return result
