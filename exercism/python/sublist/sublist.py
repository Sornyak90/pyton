"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = "sublist"
SUPERLIST = "superlist"
EQUAL = "equal"
UNEQUAL = "unequal"

def sublist(A, B):
    if A == B:
        return EQUAL
    if not A:
        return SUBLIST
    if not B:
        return SUPERLIST
    # Проверяем, является ли A подсписком B
    if len(A) <= len(B):
        for i in range(len(B) - len(A) + 1):
            if B[i:i+len(A)] == A:
                return SUBLIST
    # Проверяем, является ли B подсписком A
    if len(B) <= len(A):
        for i in range(len(A) - len(B) + 1):
            if A[i:i+len(B)] == B:
                return SUPERLIST
    return UNEQUAL    
    
   



