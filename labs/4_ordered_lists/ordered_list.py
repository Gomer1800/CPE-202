# Luis Gomez
# CPE 202

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

    def is_empty(self): # DONE
        """
        Returns back True if OrderedList is empty
        """
        return self.sentinel.next == self.sentinel and self.sentinel.prev == self.sentinel

    def add(self, item): # DONE
        """
        Adds an item to OrderedList, in the proper location based on ordering of items
        from lowest (at head of list) to highest (at tail of list)
        If item is already in list, do not add again (no duplicate items)
        """
        if item is None: raise ValueError
        current = Node(item)

        if self.is_empty(): # 1) empty list, add anywhere, assign head and tail
            self.sentinel.next, self.sentinel.prev = current, current
            return

        item_list = self.python_list()
        result = self.binary_search_add( item, 0, item_list.len()-1, item_list)
        if result is not None:
            if result is (int, None): # larger than Tail
                print(100)
                self.sentinel.prev.next, current.prev = current, self.sentinel.prev
                self.sentinel.prev = current
            elif result is (None, int): # smaller than Head
                print(200)
                self.sentinel.next.prev, current.next = current, self.sentinel.next
                self.sentinel.next = current
            elif result is (int, int):
                print(300)
                nodes = self.node_list()
                nodes[result[0]].next, current.prev = current, nodes[result[0]]
                nodes[result[1]].prev, current.next = current, nodes[result[1]]
        return

    def remove(self, item): # DONE
        """
        Removes an item from OrderedList. If item is removed (was in the list) returns True
        If item was not removed (was not in the list) returns False
        """ 
        if self.is_empty(): raise IndexError
        if item is None: raise ValueError
        
        items = self.python_list() 
        item_index = self.bin_search(item, 0, len(items)-1, items)

        if item_index is None: return False # 0) : item not in list
        
        current = self.node_list()[item_index] # copy of item's Node
        if len(items) == 1:                # 1) removing creates empty list
            self.sentinel.next, self.sentinel.prev = self.sentinel, self.sentinel
            return True
        elif item_index == 0:               # 2) removing HEAD
            self.sentinel.next = current.next
            return True
        elif item_index == len(nodes)-1:   # 3) removing TAIL
            self.sentinel.prev =  current.prev
            return True
        else:                               # 4) removing item between HEAD and TAIL 
            current.prev.next, current.next.prev =  current.next, current.prev 
            return True

    def index(self, item): # DONE
        """Returns index of an item in OrderedList (assuming head of list is index 0).
        If item is not in list, return None"""
        # is list empty?
        if self.is_empty(): raise IndexError
        if item is None: raise ValueError
        
        item_list = self.python_list()
        return self.bin_search(item, 0, len(item_list)-1, item_list)

    def pop(self, index): # DONE
        """
        Removes and returns item at index (assuming head of list is index 0).
        If index is negative or >= size of list, raises IndexError
        """
        if self.is_empty(): raise IndexError
        if index is None: raise ValueError

        nodes = self.node_list()
        if index < len(nodes) and index >= 0: # is index valid?
            current = nodes[index]
            self.remove(current.item)
            return current.item
        else: raise IndexError

    def search(self, item): # RECURSIVE, DONE
        """
        Searches OrderedList for item, returns True if item is in list, False otherwise
        """
        if self.is_empty(): raise IndexError
        if item is None: raise ValueError

        if self.index(item) is not None: return True
        else: return False

    def python_list(self): # DONE
        """Return a Python list representation of OrderedList, from head to tail
        For example, list with integers 1, 2, and 3 would return [1, 2, 3]"""
        # Empty list?
        if self.is_empty(): raise IndexError
        nodes = self.node_list()
        return [node.item for node in nodes]

    def python_list_reversed(self): # RECURSIVE, DONE
        """Return a Python list representation of OrderedList, from tail to head, using recursion
        For example, list with integers 1, 2, and 3 would return [3, 2, 1]"""
        if self.is_empty(): raise IndexError
        items = self.python_list()
        return self.reverse_rec(items)

    def size(self): # RECURSIVE, DONE
        """
        Returns number of items in the OrderedList
        """
        if self.is_empty(): raise IndexError
        return self.count_sandwich(self.sentinel)
    
    def reverse_rec(self, int_list): # HELPER FUNCTION
        """
        recursively reverses a list of numbers and returns the reversed list
        If list is None, raises ValueError
        """
        if int_list is None : raise ValueError # base case
        
        if len(int_list) == 1 : return int_list # base case
        
        new_list = int_list
        new_list = [ int_list.pop(-1) ] # pops last element to the front
        new_list.extend( reverse_rec(int_list) )
        return new_list
    
    def node_list(self): # HELPER FUNCTION
        """Return a Python list representation of OrderedList, from head to tail
        For example, list with integers 1, 2, and 3 would return [1, 2, 3]"""
        # Empty list?
        if self.is_empty(): raise IndexError
        node_list = [self.sentinel.next]
        for node in node_list:
            if node.next is not None:
                node_list.append(node.next)
        return node_list

    def count_sandwich(self, sentinel, count=0): # RECURSIVE HELPER FUNCTION
        """
        Recursive function that utilizes a copy of a sentinel node to count the size of a linked list. Counts faster than starting from one end. Think sandwich... Outwards to in
        """
        if sentinel is None: raise ValueError
        
        current = sentinel

        if current.next == self.sentinel and current.prev == self.sentinel: return count # base case
        else: count += 1

        if current.next == current.prev: return count # reached center
        else: current.next, current.prev = current.next.next, current.prev.prev # shift inward
        return self.count_sandwhich(current, count) # recursive call

    def bin_search(self, target, low, high, item_list): # RECURSIVE HELPER FUNCTION
        """
        Recursively searches for target in item_list. Returns index if found, None if not found. If item_list is empty, raises IndexError
        """
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

    def bin_search_add(self, target, low, high, item_list): # HELPER FUNCTION
        """Recursively checks for redundancy and an available position for target in item_list. Returns index tuple (low, high) if position available, None if redundant. 
        If item_list is empty, raises IndexError"""
        # EMPTY LIST
        if item_list is None: raise IndexError

        mid = (low + high) // 2 # determines mid index
        # BASE CASES
        if item_list[mid] == target: return None
        if item_list[high] == target: return None
        elif target > high: return (high, None)
        if item_list[low] == target: return None
        elif target < low: return (None, low)
        if low == high-1: 
            return (low, high) # return index tuple

        # check upper half
        if target > item_list[mid]:
            result  = bin_search(target, mid, high, item_list)
            return result
        # check lower half
        elif target < item_list[mid]:
            result = bin_search(target, low, mid, item_list)
            return result
