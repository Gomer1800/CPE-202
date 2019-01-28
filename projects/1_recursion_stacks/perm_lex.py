"""
Luis Gomez
CPE 202
"""
def perm_gen_lex(my_string=None):
    """
    Recursive script that generates all permutations of the characters in a string.

    For each char in the input string:
        Form a simpler string by removing the char from the input string
        Generate all permutations of the simpler string recursively
        Add the removed char to the front of each permutation of the simpler string
        Add resulting permutaion to the list
    """
    permutations = []

    """ Base Cases """
    if my_string is None: raise ValueError
    if my_string is '': return permutations
    if len(my_string) == 1: return [my_string]

    """ Traverse my_string """
    for i in range(len(my_string)):
        temp_list = list(my_string)
        """ Pop i'th char from string """
        char = temp_list.pop(i)
        temp_string = ''.join(temp_list)
        """ Recursive call """
        temp_permutations = perm_gen_lex(temp_string)
        """ Extend list of permutations using List Comprehension syntax"""
        permutations.extend([char + perm for perm in temp_permutations])

    #print("permutations",permutations)
    """ Base Case """
    return permutations

