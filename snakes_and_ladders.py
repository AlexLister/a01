"""
Problem:

    Whilst playing a game of snakes and ladders, Sam lands on
    square 11. On square 14, there is a ladder to square 29. On
    square 17, there is a snake to square 4.

    The function 'move' takes an input, representing the next dice
    roll, and should output the square that Sam ends up at next.

Tests:

    >>> move(1)
    12
    >>> move(2)
    13
    >>> move(3)
    29
    >>> move(4)
    15
    >>> move(5)
    16
    >>> move(6)
    4

"""


# Use this to test your solution. Don't edit it!
import doctest
def run_tests():
    doctest.testmod(verbose=True)


# Edit this code
def move(roll):
    tile = 11
    plus1 = +1

    
    if roll == 3:
        tile = tile + roll + 15 
        print (tile)

    elif roll == 6:
        tile = tile + roll - 13
        print (tile)

    else:
        tile = tile + roll
        print (tile)

