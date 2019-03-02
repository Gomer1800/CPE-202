"""
Luis Gomez
Python Data Structures Practice
"""
class MyHashTable:

    def __init__(self, table_size=11):
        self.table_size = table_size
        self.hash_table = [[] for _ in range(table_size)] # List of lists implementation
        self.num_items = 0
        self.num_collisions = 0

    def insert(self, key, value):
        "Takes a key, and an item.  Keys are valid Python non-negative integers. \
        The function will insert the key-item pair into the hash table based on the \
        hash value of the key mod the table size (hash_value = key % table_size)"
        if key is None: raise ValueError
        if key < 0: raise ValueError
        if isinstance( key, int) == False: raise ValueError

        hash_value = key % self.table_size
        # case 1: empty list at index
        if len(self.hash_table[ hash_value ]) == 0:
            self.num_items += 1
            self.hash_table[ hash_value ].append( (key, value) )
        else:
            for i in range(len(self.hash_table[hash_value])):
                print(self.hash_table[hash_value])
                # case 2: duplicate key
                if self.hash_table[hash_value][i][0] == key:
                    self.hash_table[hash_value][i] = (key, value)
                    break
                # case 3: unique key
                if i == len(self.hash_table[hash_value])-1:
                    self.num_collisions += 1
                    self.num_items += 1
                    self.hash_table[hash_value].insert(-1, (key, value))

        # check load factor
        if self.load_factor() > 1.5:
            self.increase_table_size()

    def increase_table_size(self):
        """
        This method is used to increase the size of the hash_table
        The new hash table is of size 2*previous_size+1
        """
        # initialize new hash table and new size
        new_table = MyHashTable( 2*self.table_size+1 )
        # populate new hash table with previous values
        for i in range( self.table_size ), len(self.hash_table[i]) != 0:
            for (k,v) in self.hash_table[i]:
                new_table.insert( k, v )

        # reassign self hash table and self size
        self.table_size = new_table.table_size
        self.hash_table = new_table.hash_table

    def get_item(self, key):
        "Takes a key and returns the item from the hash table associated with the key. \
        If no key-item pair is associated with the key, the function raises a LookupError exception."
        if key == None: raise ValueError
        if isinstance(key, int) == False: raise ValueError

        hash_value = key % self.table_size
        for i in range(len(self.hash_table[hash_value])):
            if self.hash_table[hash_value][i][0] == key:
                print(self.hash_table[hash_value][i][1])
                return self.hash_table[hash_value][i][1]
        raise LookupError

    def remove(self, key):
        "Takes a key, removes the key-item pair from the hash table and returns the key-item pair. \
        If no key-item pair is associated with the key, the function raises a LookupError exception. \
        (The key-item pair should be returned as a tuple)"
        if key == None: raise ValueError
        if isinstance(key, int) == False: raise ValueError

        hash_value = key % self.table_size
        for i in range(len(self.hash_table[hash_value])):
            if self.hash_table[hash_value][i][0] == key:
                self.num_items -= 1
                return self.hash_table[hash_value].pop(i)
        raise LookupError

    def load_factor(self):
        "Returns the current load factor of the hash table"
        return (self.num_items/self.table_size)

    def size(self):
        "Returns the number of key-item pairs currently stored in the hash table"
        return self.num_items

    def collisions(self):
        "Returns the number of collisions that have occurred during insertions into the hash table"
        return self.num_collisions
