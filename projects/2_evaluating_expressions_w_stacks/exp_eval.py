"""
Luis Gomez

postfix_eval( string ) : 
    evaluates a given post fix expression and returns the mathematical result
infix_to_postfix( string ) :
    evaluates a given infix expression and returns the postfix equivalent
prefix_to_postfix( string ) :
    evaluates a given prefix expression and returns the postfix equivalent
"""

from stack_array import Stack

# You should not change this Exception class
class PostfixFormatException(Exception):
    pass

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
        # check for operatorm, evaluate operators on A & B if True
        if operator_present(term) is True:
            if operand_stack.size()<2: 
                raise PostfixFormatException("Insufficient operands")
            B = operand_stack.pop()
            A = operand_stack.pop()
            operand_stack.push(
                    calculate(
                        A,      # A
                        B,      # B
                        term)   # operator
                    )
        # check for operand, push to stack if True
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
    if input_str is None: raise ValueError
    # Split input string
    term_list = input_str.split()
    #print("TERM LIST ",term_list) 
    # Create output list, will be fed to postfix_eval() at end
    output_list = []
    # initialize stack large enough to contain all operators
    operator_stack = Stack(len(term_list)//3+1)
    for term in term_list:
        # check for operand, if present append to output list
        if operand_present(term) is True:
            output_list.append(term)
        # check for operator
        elif operator_present(term) or term == '(' or term == ')':
            #if operand_stack.size()<2: 
            #    raise PostfixFormatException("Insufficient operands")
            # Check for open parentheses
            if term == '(': operator_stack.push(term)
            # Check for closing parentheses, pop stack until open parentheses found
            elif term == ')':
                while 1:
                    token = operator_stack.pop()
                    if token != '(': 
                        output_list.append(token)
                    else: break
            # Otherwise push to stack but pop any higher/equal order operators
            else:
                sort_operators(term, operator_stack, output_list)
                #print(operator_stack.peek())
        #else: raise PostfixFormatException("Invalid token")
    #if len(term_list) % 3 != 0: raise PostfixFormatException("Too many operands")
    while operator_stack.size() != 0:
        output_list.append(operator_stack.pop())
    new_str = (" ".join(output_list))
    #print("NEW STR ", new_str)
    return new_str

def prefix_to_postfix(input_str): # prefix requires that all operators precede the two operands that they work on
    """Converts a prefix expression to an equivalent postfix expression"""

    """Input argument: a string containing a prefix expression where tokens are 
    space separated.  Tokens are either operators + - * / ** << >> or numbers (integers or floats)
    Returns a String containing a postfix expression(tokens are space separated)"""
    if input_str is None: raise ValueError
    # split input string into list
    term_list = input_str.split()
    #print("TERM LIST ",term_list) 
    # initialize output list
    output_list = []
    #print("OUT SIZE ", len(output_list))
    # initialize operator stack
    operator_stack = Stack(len(term_list)//3+1)
    for i in range(len(term_list)):
        term = term_list[i]
        # prefix should begin with an operator otherwise raise Exception
        if i == 0:
            if operator_present(term) is True: operator_stack.push(term)
            else: raise PostfixFormatException()
        # Check for operator
        elif operator_present(term): 
            operator_stack.push(term)
        # check for operand
        elif operand_present(term):
            output_list.append(term)
            # if previous two terms in output list were operands, pop operator stack to output list once
            if operand_present(term_list[i-1]):
                    output_list.append(operator_stack.pop())
                    # for every three operands there should be an additional operator
                    if operand_present(term_list[i-3]) and operator_stack.size() != 0:
                        output_list.append(operator_stack.pop())
    while operator_stack.size() != 0:
        output_list.append(operator_stack.pop())
    new_str = (" ".join(output_list))
    #print("NEW STR ", new_str)
    return new_str

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

def sort_operators(current_operator, operator_stack, output_list): # HELPER
    """Sorts an incoming operator stack according to current_operator, 
    and pops higher precedence operators to an output list"""
    #print("SORT ", current_operator)
    # order of operations represented as a list
    order = ['*','<<','**','/','>>','+','-']
    i = order.index(current_operator)

    for elem in range(operator_stack.size()):
        if operator_stack.peek() != '(':
            # numeral representation of precedence of TOP of stack
            j = order.index(operator_stack.peek())
            # if top of stack is of 'higher' or equal precendence, add to output list
            if j >= i:
                output_list.append(operator_stack.pop())
    # Finally, push current operator to stack
    operator_stack.push(current_operator)

def calculate(A, B, operator): # HELPER
    """Evaluates a mathematical operation using the operands A & B, and the incoming operator"""
    base_dict = {
            '+' : float(A) + float(B),
            '-' : float(A) - float(B),
            '*' : float(A) * float(B),
            '/' : float(A) / float(B), 
            '**': float(A) **float(B), 
            '<<': float(A) * (2**float(B)), # left shift
            '>>': float(A) / (2**float(B))  # right shift
            }
    return base_dict[operator]
