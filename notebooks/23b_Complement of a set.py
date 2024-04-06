"""
The complement of a set is everything not in the set, but part of the "universal set". 
Without a definition of the universal set, you can't really give a standard-library definition 
of the complement of a set.

Thus, the purpose of this task is to define a function that calculates the complement of a set.
Your function will receive two arguments: the universal set and the set you want to calculate its complement.

If you can't calculate the complement (because the set is not a subset of the universal set), 
your function should return None.
"""

def complement(universal_set, A):
    if A.issubset(universal_set):
        return universal_set - A
    else:
        return None