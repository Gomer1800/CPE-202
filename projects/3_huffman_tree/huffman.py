class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char   # stored as an integer - the ASCII character code value
        self.freq = freq   # the frequency count associated with the node
        self.left = None   # Huffman tree (node) to the left
        self.right = None  # Huffman tree (node) to the right

    def __lt__(self, other):
        return comes_before(self, other) # Allows use of Python List sorting

    def set_left(self, node):
        self.left = node

    def set_right(self, node):
        self.right = node
    
    def __repr__(self):
        return ("HuffmanNode({!r}, {!r}, {!r}, {!r})".format(self.char, self.freq, self.left, self.right))

def comes_before(a, b):
    """Returns True if node a comes before node b, False otherwise"""
    if a.freq == b.freq:
        return ord(a) < ord(b)
    else:
        return a.freq < b.freq

#def combine(a, b):
    """Creates and returns a new Huffman node with children a and b, with the "lesser node" on the left
    The new node's frequency value will be the sum of the a and b frequencies
    The new node's char value will be the lesser of the a and b char ASCII values"""

def cnt_freq(filename):
    """Opens a text file with a given file name (passed as a string) and counts the 
    frequency of occurrences of all the characters within that file
    Returns a Python List with 256 entries - counts are initialized to zero.
    The ASCII value of the characters are used to index into this list for the frequency counts"""
    # initialize list of size 256 with counts initialized to 0
    freq_list = [0]*256
    # read file line by line
    # split line into chars and increment respective element in freq list
    try:
        with open(filename) as file_object: # with ... will close the file for us later
            try:
                line_list = file_object.readlines()
                for line in line_list:
                    for char in list(line):
                        i = ord(char)
                        freq_list[i] += 1
            except EOFError: print("End of file hit without reading data")
            except ValueError: print("Wrong argument -> line or char")
    except IOError: print("Filename can't be opened")
    except ValueError: print("Bad argument -> Filename")
    except Exception: print("Generic Exception")
    finally: return freq_list

def create_huff_tree(freq_list):
    """
    Input is the list of frequencies (provided by cnt_freq()).
    Create a Huffman tree for characters with non-zero frequency
    Returns the root node of the Huffman tree. Returns None if all counts are zero.
    """
    # if all counts are zero, return None
    if max(freq_list) == 0: return None
    # create list of (index, freq) tuples, filtering out zero-occuring chars
    valid_chars = [(index, freq) for index ,freq in enumerate(freq_list) if freq > 0]
    print (valid_chars)
    # sort tuple list by freq, and index value if tied
    valid_chars.sort(key=lambda tup: tup[1])
    print (valid_chars)
    # create sorted list of huffman nodes
    tree_list = [HuffmanNode(chr(index), freq) for (index, freq) in valid_chars]
    print(tree_list)
    # create huffman tree

def create_huff_tree_helper(tree_list):
    """ Recursive method for building a huffman tree
    param tree_list: list of HuffmanNodes from which to build tree
    base cases:
    - node list is empty: return None
    - single node in list: node is root node, tree is complete
    - more than one node:
        * remove two nodes from beginning of list
        * create new none with these two as children, left is lesser
        * insert new node to sorted list
        * recursive call
    """
    pass

#def create_code(node):
    """Returns an array (Python list) of Huffman codes. For each character, use the integer ASCII representation 
    as the index into the array, with the resulting Huffman code for that character stored at that location.
    Characters that are unused should have an empty string at that location"""

#def create_header(freq_list):
    """Input is the list of frequencies (provided by cnt_freq()).
    Creates and returns a header for the output file
    Example: For the frequency list asscoaied with "aaabbbbcc, would return “97 3 98 4 99 2” """

#def huffman_encode(in_file, out_file):
    """Takes inout file name and output file name as parameters
    Uses the Huffman coding process on the text from the input file and writes encoded text to output file
    Take not of special cases - empty file and file with only one unique character"""
