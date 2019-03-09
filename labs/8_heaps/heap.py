"""
Luis Gomez
Python implementation of the Binary Heap ADT, using the MaxHeap approach.
Largest key value is always at front.
This heap contains integers that represent both the priority and name of the object
"""
class MaxHeap:

    def __init__(self, capacity=50):
        """Constructor creating an empty heap with default capacity = 50 but allows heaps of other capacities to be created."""
        self.heap_size = capacity + 1
        self.heap_list = []*self.heap_size
        self.num_items = 0

    def enqueue(self, item):
        """inserts "item" into the heap, returns true if successful, false if there is no room in the heap"""
        if item is None: raise ValueError
        if self.is_full(): return False
        self.num_items+=1
        self.heap_list.insert(self.num_items, item)
        self.perc_up(self.num_items)

    def peek(self):
        """returns max without changing the heap, returns None if the heap is empty"""
        if self.is_empty(): return None
        return self.heap_list[1]

    def dequeue(self):
        """returns max and removes it from the heap and restores the heap property
           returns None if the heap is empty"""
        if self.is_empty(): return None
        max, self.heap_list[1] = self.heap_list.pop(0), self.heap_list[self.num_items]
        self.num_items-=1
        self.perc_down(1)
        return max

    def contents(self):
        """returns a list of contents of the heap in the order it is stored internal to the heap.
        (This may be useful for in testing your implementation.)"""
        return self.heap_list

    def build_heap(self, alist):
        """Discards the items in the current heap and builds a heap from 
        the items in alist using the bottom up method.  
        If the capacity of the current heap is less than the number of 
        items in alist, the capacity of the heap will be increased to accommodate the items in alist"""
        if alist is None: raise ValueError
        self.num_items = len(alist)
        # Case, current heap is too small
        if self.heap_size-1 < len(alist):
            self.heap_list = [None].extend(alist)
            self.heap_size = len(self.heap_list)
        # Case, current heap is large enough
        else:
            alist.insert(0,None)
            self.heap_list = alist.extend([]*(self.heap_size-len(alist)))
        i = self.num_items
        while i > 0:
            perc_up(i)

    def is_empty(self):
        """returns True if the heap is empty, false otherwise"""
        if self.get_size() == 0: return True
        return False

    def is_full(self):
        """returns True if the heap is full, false otherwise"""
        if self.num_items == self.heap_size-1: return True
        return False
        
    def get_capacity(self):
        """this is the maximum number of a entries the heap can hold
        1 less than the number of entries that the array allocated to hold the heap can hold""" 
        return self.heap_size-1

    def get_size(self):
        """the actual number of elements in the heap, not the capacity"""
        return self.num_items

    def perc_down(self, i):
        """where the parameter i is an index in the heap and perc_down moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes."""
        if i is None: raise ValueError  # edge case, invalid index
        if i <= 0: raise ValueError
        if i > self.num_items: raise ValueError
        if i == 1: return               # edge case, index is top of tree
        child = i*2
        # iterate through child nodes
        while child < self.num_items:
            # current value < left child?
            if self.heap_list[i] < self.heap_list[child]:
                # swap positions if true
                self.heap_list[i], self.heap_list[child] = self.heap_list[child], self.heap_list[i]
                # change current index, change child index
                i, child = child, child*2
                continue
            if child+1 > num_items: break
            child = child+1
            # current value < right child?
            if self.heap_list[i] < self.heap_list[child]:
                # swap positions if true
                self.heap_list[i], self.heap_list[child] = self.heap_list[child], self.heap_list[i]
                # change current index, change child index
                i, child = child, child*2
                continue
            else: break

    def perc_up(self, i):
        """where the parameter i is an index in the heap and perc_up moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes."""
        if i is None: raise ValueError  # edge case, invalid index
        if i <= 0: raise ValueError
        if i > self.num_items: raise ValueError
        if i == 1: return               # edge case, index is top of tree

        parent = i//2
        # iterate through parent nodes
        while parent > 1:
            # current value > parent?
            if heap_list[i] > heap_list[parent]:
                # swap positions if true
                heap_list[i], heap_list[parent] = heap_list[parent], heap_list[i]
                # change current index, change parent index
                i, parent = parent, parent//2
            # cannot perc up further
            else: break

    def heap_sort_ascending(self, alist):
        """perform heap sort on input alist in ascending order
        This method will discard the current contents of the heap, build a new heap using
        the items in alist, and mutate alist to put the items in ascending order"""


