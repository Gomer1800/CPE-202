"""
Luis Gomez
Data Structures
"""
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
    """
    Returns True if node a comes before node b, False otherwise
    """
    if a.freq == b.freq:
        return a.char < b.char
    else:
        return a.freq < b.freq

def combine(a, b):
    """
    Creates and returns a new Huffman node with children a and b, with the "lesser node" on the left
    The new node's frequency value will be the sum of the a and b frequencies
    The new node's char value will be the lesser of the a and b char ASCII values
    """
    char_rep = min([a.char, b.char])
    new_root = HuffmanNode(char_rep, a.freq + b.freq)
    new_root.left, new_root.right = a, b
    return new_root

def cnt_freq(filename):
    """
    Opens a text file with a given file name (passed as a string) and counts the 
    frequency of occurrences of all the characters within that file
    Returns a Python List with 256 entries - counts are initialized to zero.
    The ASCII value of the characters are used to index into this list for the frequency counts
    """
    # initialize list of size 256 with counts initialized to 0
    freq_list = [0]*256
    # read file line by line
    # split line into chars and increment respective element in freq list
    try:
        with open(filename) as file_object: # with ... will close the file for us later
            line_list = file_object.readlines()
            for line in line_list:
                for char in list(line):
                    i = ord(char)
                    freq_list[i] += 1
    except FileNotFoundError: 
        raise FileNotFoundError("Filename can't be opened")
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
    valid_chars = [(index, freq) for index, freq in enumerate(freq_list) if freq > 0]
    # sort tuple list by freq, and index value if tied
    valid_chars.sort(key=lambda tup: tup[1])
    #print (valid_chars)
    # create sorted list of huffman nodes
    tree_list = [HuffmanNode(index, freq) for (index, freq) in valid_chars]
    #print(tree_list)
    # create huffman tree, return root node
    return create_huff_tree_helper(tree_list)[0]

def create_huff_tree_helper(tree_list):
    """ 
    Recursive function for building a huffman tree
    param tree_list: list of HuffmanNodes from which to build tree
    base cases:
    - node list is empty: return None
    - single node in list: node is root node, tree is complete
    - more than one node:
        * remove two nodes from beginning of list
        * create new none with these two as children, left is lesser freq, 
          freq equal to sum, char being the lesser in ASCII value of the two
        * insert new node to sorted list
        * recursive call
    """
    if len(tree_list) == 0: return None
    elif len(tree_list) == 1:
        # print("elif ",tree_list)
        return tree_list
    else:
        # print("else",tree_list)
        left = tree_list.pop(0)
        right = tree_list.pop(0)
        # create new HuffmanNode
        new_root = combine(left, right)
        for i in range(len(tree_list)):
            # print("i = ",i)
            if comes_before(new_root, tree_list[i]):
                tree_list.insert(i, new_root)
                # print("Break")
                break
            elif i == len(tree_list)-1:
                tree_list.append(new_root)
        if len(tree_list) == 0:
            tree_list.append(new_root)
        """ Debug print statements"""
        # print("length ", len(tree_list))
        # print("else ",tree_list)
        # print("return")
        return create_huff_tree_helper(tree_list)

def create_code(node):
    """
    Returns an array (Python list) of Huffman codes. For each character, use the integer ASCII representation 
    as the index into the array, with the resulting Huffman code for that character stored at that location.
    Characters that are unused should have an empty string at that location"""
    if node is None: return None # ASK PROF about exception here?
    code_array = [""]*256
    return create_code_helper(node, code_array, "")

def create_code_helper(node, code_array, char_code):
    """
    Recursive function that generates an array of huffcodes for 256 characters
    param node: Huffman root node from which to traverse
    param code_array: array of 256 Huffman codes whose indeces are the ASCII codes for chars
    param char_code: string representation for current character
    base cases:
        * if leaf node reached, populate code_array using current char as index and char_code
        * recursive left, right hand concatenation of 1 or 0 to char_code
        * recursive right, same as above
        * all leaves exhausted, return code_array
    """
    # leaf node reached
    if node.left is None and node.right is None:
        code_array[node.char] = char_code
        return code_array
    # traverse left
    code_array = create_code_helper( node.left, code_array, char_code+'0')
    # traverse right
    code_array = create_code_helper( node.right, code_array, char_code+'1')
    # all leaves exhausted
    return code_array

def create_header(freq_list):
    """
    Input is the list of frequencies (provided by cnt_freq()).
    Creates and returns a header for the output file
    Example: For the frequency list asscoaied with "aaabbbbcc, would return “97 3 98 4 99 2”
    """
    # if all counts are zero, return None
    if max(freq_list) == 0: return None
    # create list of (index, freq) tuples, filtering out zero-occuring chars
    valid_chars = [(index, freq) for index, freq in enumerate(freq_list) if freq > 0]
    header_str = ""
    for (index, freq) in valid_chars:
        header_str+= str(index) + " " + str(freq) + " "
    return header_str[0:-1]

def huffman_encode(in_file, out_file):
    """
    Takes inout file name and output file name as parameters
    Uses the Huffman coding process on the text from the input file and writes encoded text to output file
    Take not of special cases - empty file and file with only one unique character
    """
    try:
        char_list = []
        huff_code = ""
        # generate character list
        with open(in_file) as file_object:
            line_list = file_object.readlines()
            for line in line_list:
                char_list.extend(list(line))
        # generate frequency list
        freq_list = cnt_freq( in_file)
        # generate huff tree, returns None if in file was empty
        root_node = create_huff_tree( freq_list)
        if root_node != None:
            # generate out file
            code_array = create_code( root_node)
            for char in char_list:
                huff_code += code_array[ord(char)]
            with open(out_file, 'w', newline='') as file_object:
                file_object.write( create_header(freq_list) + '\n')
                file_object.write( huff_code)
        else:
            # generate empty out file
            file_object = open(out_file, 'w', newline='')
            file_object.close()
    except FileNotFoundError:
        raise FileNotFoundError("File Not Found")
        with open(out_file, 'w', newline='') as file_object:
            file_object.write("")
