"""
Problem:

    'I before E except after C' is a helpful mnemonic to remind
    people how to spell words where the letters i and e are
    present together.

    For instance, in the word believe - the e follows the i.
    In the word ceiling - the i follows the e because its after c.

    The function 'spell_check' should take a string input,
    which will be a single word, and check whether this rule
    is being followed.  If it is, it should print "Correct",
    otherwise it should print "False".

    All words will be in lowercase, and there will only
    be one instance of "ie" or "ei" present.

Tests:

    >>> spell_check("believe")
    Correct
    >>> spell_check("feirce")
    False
    >>> spell_check("friend")
    Correct
    >>> spell_check("ceiling")
    Correct
    >>> spell_check("reciept")
    False
    >>> spell_check("decieve")
    False

"""

# Use this to test your solution. Don't edit it!
import doctest
def run_tests():
    doctest.testmod(verbose=True)


# Edit this code
def spell_check(word):
    check = 0

    word.lower()

    if "i" in word and "e" in word and "c" in word:
        if "c" > "e" and "e" > "i":
            print ("Correct")

        else:
            print ("False")

    elif "i" in word and "e" in word:
        if "i" > "e":
            print ("Correct")

        else:
            print ("False")
        
        
        

