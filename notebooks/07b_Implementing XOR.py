"""
XOR (exclusive or) is a boolean operator with the following truth table:

XOR(0,0)=0

XOR(0,1)=1

XOR(1,0)=1

XOR(1, 1) = 0

You must write a function that receives two lists as the arguments. 
These lists must consist of zeros and ones. Let's call them A and B.

The function should return a list where the i-th element is XOR(A[i], B[i]).

Example:

Input data:
First argument: [0, 0, 1, 1]
Second argument: [0, 1, 0, 1]
Output:
[0, 1, 1, 0]

Please, use the map and zip functions.
"""


def xor(A, B):
    
    def analyse(pairs):
        if pairs[0] == pairs[1]:
            return 0
        else:
            return 1

    pairs = zip(A, B)
    result = list(map(analyse, pairs))

    return result

    # Sure, this is better: 
    # return list(map(lambda x: x[0] ^ x[1], zip(A, B)))

first = [0, 0, 1, 1]
second = [0, 1, 0, 1]

print(xor(first, second))

