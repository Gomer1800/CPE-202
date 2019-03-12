"""
Luis Gomez
Python Data Structures

Concordance Generator. Uses a Quadratic Probing hash table to generate a 
stop words table and concordance table. Stop words table MUST be loaded prior to
building concordance table.

This was a crazy project, so relieved
"""
from hash_quad import *
import string

class Concordance:

    def __init__(self):
        self.stop_table = None          # hash table for stop words
        self.concordance_table = None   # hash table for concordance

    def load_stop_table(self, filename):
        """ Read stop words from input file (filename) and insert each word as a key into the stop words hash table.
        Starting size of hash table should be 191: self.stop_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""
        self.stop_table = HashTable(191)
        try:
            with open(filename) as file_object:
                line_list = file_object.readlines()
                for line in line_list:
                    key = line.strip()  # remove leading, trailing whitespace
                    """Case, stop word is not in stop_table yet"""
                    if self.stop_table.in_table(key) is False:
                        #print("stop table key: ", key)
                        self.stop_table.insert(key)
            
            #stop_words = self.stop_table.get_all_keys()
            #stop_words.sort()
            #print("Load Stop, stop words: ", stop_words)

        except FileNotFoundError:
            raise FileNotFoundError("Load-stop-table: File not found")
        except Exception:
            # print("Stop Table Ex 2: ",self.stop_table.hash_table)
            raise Exception("Load-stop-table: unknown exception")
        

    def load_concordance_table(self, filename):
        """ 
        1)  Read words from input text file (filename) and insert them into the concordance hash table, 
            after processing for punctuation, numbers and filtering out words that are in the stop words hash table.
        
        2)  Do not include duplicate line numbers (word appearing on same line more than once, just one entry for that line)
        
        3)  Starting size of hash table should be 191: self.concordance_table = HashTable(191)
            -If file does not exist, raise FileNotFoundError
        """
        self.concordance_table = HashTable(191)
        i = 1
        try:
            stop_words = self.stop_table.get_all_keys()
            stop_words.sort()
            #print("Load Con, stop words: ", stop_words)

            with open(filename) as file_object:
                line_list = file_object.readlines()
                for line in line_list:
                    keys = line.replace('-',' ')                                    # replace hyphen with space
                    keys = keys.translate(str.maketrans('','', string.punctuation)) # This is getting ridiculuous
                    #print("Con table keys: ",keys)
                    keys = keys.split()
                    for key in keys:
                        if not key.isdigit():
                            if key.lower() not in stop_words: # OMG LOWER CASE DUH!
                                #print("Con table key: ", key, i)
                                self.concordance_table.insert(key, i)
                    i+=1
            
            #keys = self.concordance_table.get_all_keys()
            #keys.sort()
            #print("Load Con, key words: ", keys)
        except FileNotFoundError:
            raise FileNotFoundError("Load-concordance-table: File not found")

    def write_concordance(self, filename):
        """ Write the concordance entries to the output file(filename)
        See sample output files for format."""
        try:
            stop_words = self.stop_table.get_all_keys()
            stop_words.sort()
            #print("Write, stop words: ", stop_words)
            keys = self.concordance_table.get_all_keys()

            keys.sort()
            #print("Write, keys: ", keys)
            #print("Write, keys sorted: ", keys)
            with open(filename, 'w', newline='') as file_object:
                #print("Write filename: ", filename)
                for i in range(len(keys)):
                    #print("Write iter: ",i)
                    index = self.concordance_table.get_index(keys[i])
                    #print("write, index & key: ", index, key)
                    values = self.concordance_table.hash_table[index][1]
                    #print("Write, values: ", values)
                    if i != len(keys)-1:
                        file_object.write(keys[i] +': '+" ".join(str(value) for value in values)+'\n')
                    else:
                        file_object.write(keys[i] +': '+" ".join(str(value) for value in values))

        except Exception:
            print("Write to: Unknown Exception")
