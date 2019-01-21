"""
Luis Gomez
CPE 202
"""
def convert(num, base):
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
