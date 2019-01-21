"""
Luis Gomez
CPE 202

    Rules of Game:
    1. if n % 2 == 0, you may give back n / 2 bears
    2. if (n % 3 or n % 4) == 0, you may multiply last two digits of n and give back this many bears
    3. if n % 5 == 0 you may give back 42 bears
    GOAL: end up with exactly 42 bears
"""
def bears(n):
    """
    Reachability Problem: Given a computational (possibly infinite) system with a  set of allowed rules or transformations, decide whether a certain state of a system is reachable from
    a given initial state...
    True return: is possible to win the bear game by starting with n bears.
    False return: not possible to win the the bear game by starting with n bears 
    """
    winnable = False
    """ Base cases """
    if n == 42: return True
    if n < 0: return False

    """ Check rule 1 """
    if (winnable is False) and (n % 2 == 0): winnable = bears(n - n//2)

    """ Check rule 2 """
    if (winnable is False)  and ((n % 3 == 0) or (n % 4 == 0)):
        if n > 10 : 
            # second term in the subtraction produces the product of the last two digits
            winnable = bears( n - 
                    (int(''.join(list(str(n))[-2])) * int(''.join(list(str(n))[-1]))) )
    
    """ Check rule 3 """
    if (winnable is False) and (n % 5 == 0):
        if n == 42: return True
        elif n > 42: winnable = bears(n - 42)
   
    """ Base case, eliminates stack frame """
    return winnable


