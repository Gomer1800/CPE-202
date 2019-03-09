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
        print("End enqueue: ",self.heap_list)
        return True

    def peek(self):
        """returns max without changing the heap, returns None if the heap is empty"""
        if self.is_empty(): return None
        return self.heap_list[1]

    def dequeue(self):
        """returns max and removes it from the heap and restores the heap property
           returns None if the heap is empty"""
        if self.is_empty(): return None
        max, self.heap_list[1] = self.heap_list[1], self.heap_list.pop(self.num_items)
        self.num_items-=1
        self.perc_down(1)
        return max

    def contents(self):
        """returns a list of contents of the heap in the order it is stored internal to the heap.
        (This may be useful for in testing your implementation.)"""
        return self.heap_list[1:self.num_items+1]

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
            print("Case small: ",self.heap_list)
        # Case, current heap is large enough
        else:
            alist.insert(0,None)
            # print(alist)
            alist.extend([None]*(self.heap_size-len(alist))) 
            self.heap_list = alist
            print("Case big: ",self.heap_list)
        i = self.num_items//2
        while i >= 1:
            self.perc_down(i)
            i-=1
        print("End Build: ",self.heap_list)

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
        if i == self.num_items: return               # edge case, index is top of tree
        left = 0
        right = 0
        # starting right most child
        child = self.find_child( i )
        # iterate through child nodes
        while child >= self.num_items//2:
            print("perc down: ", child, self.contents())
            left, right = 0, 0
            # Case, even child
            if child % 2 == 0:
                if self.heap_list[i] < self.heap_list[child]:
                    # swap positions if true
                    self.heap_list[i], self.heap_list[child] = self.heap_list[child], self.heap_list[i]
                    # change current index, change child index
                    new_child = self.find_child( child )
                    i, child = child, new_child
                    continue
            # Case, odd chid
            if child % 2 == 1:
                # which child is greater?
                if self.heap_list[i] < self.heap_list[child]: right = child
                if self.heap_list[i] < self.heap_list[child-1]: left = child-1
                if self.heap_list[child] < self.heap_list[child-1]:
                    child = child-1
                # current value < left child?
                if child != 0:
                    if self.heap_list[i] < self.heap_list[child]:
                        # swap positions if true
                        self.heap_list[i], self.heap_list[child] = self.heap_list[child], self.heap_list[i]
                # change current index, change child index
                new_child = self.find_child( child )
                i, child = child, new_child
                continue
            break

    def find_child(self,i):
        print("find i = ",i)
        child = 0
        try:
            child = self.heap_list.index(self.contents()[i*2])
            print("try " , child)
        except Exception:
            child = self.heap_list.index(self.contents()[i*2-1])
            print("except " ,child)
        finally:
            print("finally " ,child)
            return child

    def perc_up(self, i):
        """where the parameter i is an index in the heap and perc_up moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes."""
        if i is None: raise ValueError  # edge case, invalid index
        if i <= 0: raise ValueError
        if i > self.num_items: raise ValueError
        if i == 1: return               # edge case, index is top of tree
        parent = i//2
        # iterate through parent nodes
        while parent > 0:
            print("perc up: ", parent, self.contents())
            # current value > parent?
            if self.heap_list[i] > self.heap_list[parent]:
                # swap positions if true
                self.heap_list[i], self.heap_list[parent] = self.heap_list[parent], self.heap_list[i]
                # change current index, change parent index
                i, parent = parent, parent//2
            # cannot perc up further
            else: break

    def heap_sort_ascending(self, alist):
        """perform heap sort on input alist in ascending order
        This method will discard the current contents of the heap, build a new heap using
        the items in alist, and mutate alist to put the items in ascending order"""


