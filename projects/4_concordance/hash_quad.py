class HashTable:

    def __init__(self, table_size):         # can add additional attributes
        self.table_size = table_size        # initial table size
        self.hash_table = [None]*table_size # hash table
        self.num_items = 0                  # empty hash table

    def insert(self, key, value):
        """ 
        1)  Inserts an entry into the hash table (using Horner hash function to determine index, and quadratic probing to resolve collisions).
            -The key is a string (a word) to be entered, and value is the line number that the word appears on. 
	2a) If the key is not already in the table, then the key is inserted, and the value is used as the first line number in the list of line numbers.
        2b) If the key is in the table, then the value is appended to that key’s list of line numbers. 
            -If value is not used for a particular hash table (e.g. the stop words hash table), can use the default of 0 for value and just call the insert function with the key.
        3)  If load factor is greater than 0.5 after an insertion, hash table size should be increased (doubled + 1).
        """
        """1, generate hash value"""
        key = key.lower()
        hash_value = self.horner_hash(key)
        """2, insert key and resolve collisions"""
        i = 0
        index = 0
        while 1:
            try:
                index = hash_value + i**2
                # print("Insert: ", index)
                tup = self.hash_table[index]
                """Case 1, no collision"""
                if tup is None:             # unique key
                    self.hash_table[index] = (key, [value])
                    self.num_items+=1
                    break
                """Case 2, collision"""
                if tup[0] == key:         # key matched
                    self.hash_table[index][1].append(value)
                    break
                i+=1                        # key does not match, quadratic probe
            except Exception:
                index = (hash_value + i**2) % self.table_size
        """3, check load factor, increase table if needed"""
        if self.get_load_factor() > .5:
            self.increase_table_size()
    
    def increase_table_size(self):
        # initialize new table with increased size
        new_table  = HashTable(self.table_size*2 + 1)
        # populate new hash table with previous values
        for i in range(self.table_size), self.hash_table[i] is not None:
            tup = self.hash_table[i]
            # for each line number in list, insert the key. Insert checks load factor
            for j in range(len(tup[1])):
                new_table.insert(tup[0], tup[1][j])
        # reassign self.hash_table and self.table_size
        self.table_size = new_table.table_size
        self.hash_table = new_table.hash_table

    def horner_hash(self, key):
        """
        Compute and return an integer from 0 to the (size of the hash table) - 1
        Compute the hash value by using Horner’s rule, as described in project specification.
        input: string key
        """
        hash_value = 0
        """determine minimum between len(key) and 8"""
        if len(key) > 8: min = 8
        else: min = len(key)
        # print("horner min: ", min)
        """compute the horner sum"""
        for i in range(min):
            # print(" horner i: ",i)
            # print(" horner  : ",list(key)[i], ord(list(key)[i]))
            hash_value += ord(list(key)[i])*31**(min-1-i)
        # print("Horner hash value: ", hash_value)
        # print("Horner table size: ", self.table_size)
        # print("Horner mod: ", hash_value % self.table_size)
        return hash_value % self.table_size

    def quadratic_probe(self, index):
        pass

    def in_table(self, key):
        """ Returns True if key is in an entry of the hash table, False otherwise."""
        index = self.get_index(key)
        if index is not None:
            return True
        else:
            return False

    def get_index(self, key): # BUG, quadratic probing needs fixing
        """ Returns the index of the hash table entry containing the provided key. 
        If there is not an entry with the provided key, returns None."""
        while 1:
        try:
            key = key.lower() # render key all lower case, to ease comparison
            hash_value = self.horner_hash(key)
            i = 0
            """Checks default hash value index, otherwise begins quadratic probing"""
            while 1:
                value == self.hash_table[hash_value + i**2]
                if value[0] == key:
                    return hash_value + i**2
                i+=1
        except Exception:
            """Key not in hash table"""
            return None

    def get_all_keys(self):
        """ Returns a Python list of all keys in the hash table."""
        key_list = []
        # print("Get keys, current table: ", self.hash_table)
        for tup in self.hash_table:
            if tup is not None:
                key_list.append(tup[0])
        return key_list

    def get_value(self, key):
        """ Returns the value (list of line numbers) associated with the key. 
        If key is not in hash table, returns None."""
        index = self.get_index(key)
        if index is not None:
            return self.hash_table[index][1]
        else:
            return None

    def get_num_items(self):
        """ Returns the number of entries (words) in the table."""
        return self.num_items

    def get_table_size(self):
        """ Returns the size of the hash table."""
        return self.table_size

    def get_load_factor(self):
        """ Returns the load factor of the hash table (entries / table_size)."""
        return self.num_items/self.table_size
