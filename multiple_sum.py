"""
Problem:

    The function 'multi_sum' takes an integer, n.

    It should add all of the multiples of 7 from 7 to n (inclusive),
    EXCEPT those which are also multiples of 5.

    e.g. multi_sum(50) = 7 + 14 + 21 + 28 + 42 + 49 = 161

    Notice that 35 wasn't included in the sum because it's a multiple
    of 5.


Tests:

    >>> multi_sum(50)
    161
    >>> multi_sum(21)
    42
    >>> multi_sum(111)
    630
    >>> multi_sum(161)
    1582
    >>> multi_sum(5000)
    1431430

"""


# Use this to test your solution. Don't edit it!
import doctest
def run_tests():
    doctest.testmod(verbose=True)


# Edit this code
def multi_sum(n):
    add = 0

    for i in range (1, n+1, 7):
        add = i * n 

    print (add)

        

