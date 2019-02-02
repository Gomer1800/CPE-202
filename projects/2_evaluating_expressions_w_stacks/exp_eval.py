from stack_array import Stack

# You should not change this Exception class
class PostfixFormatException(Exception):
    pass

def calculate(A, B, operator): # HELPER
        base_dict = {
                '+' : float(A) + float(B),
                '-' : float(A) - float(B),
                '*' : float(A) * float(B),
                '/' : float(A) / float(B), 
                '**': float(A) **float(B), 
                '<<': 0, # TO DO
                '>>': 0} # TO DO
        return base_dict[operator]

def postfix_eval(input_str):
    """Evaluates a postfix expression"""

    """Input argument:  a string containing a postfix expression where tokens 
    are space separated.  Tokens are either operators + - * / ** << >> or numbers (integers or floats)
    Returns the result of the expression evaluation. 
    Raises an PostfixFormatException if the input is not well-formed"""
    if input_str is None: raise PostfixFormatException
    # create list of operands and operators
    term_list = input_str.split()
    # initialize stack large enough to contain all operands
    operand_stack = Stack(2*len(term_list)//3+1)
    # iterate over term_list
    for term in term_list:
        print("TERMS SIZE ", term_list)
        # check for operator
        if operator_present(term) is True:
            if operand_stack.size()<2: raise PostfixFormatException("Insufficient operands")
            B = operand_stack.pop()
            A = operand_stack.pop()
            operand_stack.push(
                    calculate(
                        A,      # A
                        B,      # B
                        term)   # operator
                    )
        # check for operand
        elif operand_present(term) is True:
            operand_stack.push(term)
        else: raise PostfixFormatException("Invalid token")
    if len(term_list) % 3 != 0: raise PostfixFormatException("Too many operands")
    return operand_stack.pop()

def infix_to_postfix(input_str): # postfix requires that all operators proceed after the two operands that they work on
    """Converts an infix expression to an equivalent postfix expression"""

    """Input argument:  a string containing an infix expression where tokens are 
    space separated.  Tokens are either operators + - * / ** << >> or numbers (integers or floats)
    Returns a String containing a postfix expression """
    pass


def prefix_to_postfix(input_str): # prefix requires that all operators precede the two operands that they work on
    """Converts a prefix expression to an equivalent postfix expression"""

    """Input argument: a string containing a prefix expression where tokens are 
    space separated.  Tokens are either operators + - * / ** << >> or numbers (integers or floats)
    Returns a String containing a postfix expression(tokens are space separated)"""
    pass

def operator_present(input_str): # HELPER
    """Checks if input_str is a valid operator from a predefined list"""
    operator_list = ['+','-','*','/','**','<<','>>']

    if input_str in operator_list:
        return True
    else: return False

def operand_present(input_str): # HELPER
    """Checks if input_str is a valid operand"""
    try:
        float(input_str)
        return True
    except ValueError:
        return False


def convert(num, base): # HELPER, INCORPORATE SHIFT? NO CREATE SHIFT FUNCTION
    """
    Recursive function that returns a string representing num in the base b
    
    """
    quotient = num // base
    remainder = num % base

    """ Used a dictionary to map numbers > 9 to hex letters """
    if base > 10 and remainder > 9:
        base_dict = {
                10 : "A",
                11 : "B",
                12 : "C",
                13 : "D",
                14 : "E",
                15 : "F"}
        base_num = base_dict[remainder]
    else : base_num = str(remainder)

    """ Base case """
    if quotient == 0: return base_num

    """ Recursive call & concatinates strings to form converted number"""
    base_num = convert(quotient,base) + base_num
    
    """ Base case, returns converted number string"""
    return base_num

