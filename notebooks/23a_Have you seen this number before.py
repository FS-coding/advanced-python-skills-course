"""
Write a function that receives as an argument a list of numbers. 
For each number, append to an empty list the word "YES" 
if this number was previously encountered in the sequence, 
or "NO" if it was not.

Example:

Input data:
[1,2,1,2,4,5]
Output:
["NO", "NO", "YES", "YES", "NO", "NO"]
"""
import random
from textwrap import wrap
import time

def create_list(length):
    result = []
    for i in range(length):
        result.append(random.randint(1, 10))
    return result


def wrapper(f):
    def inner(*args, **kwargs):
        start = time.time()
        f(*args, **kwargs)
        end = time.time()
        execution_time = end-start
        print(f"This function took {execution_time} seconds")
    return inner

@wrapper
def number_seen(list_of_numbers):
    result = []
    for i in range(len(list_of_numbers)):
        look = list_of_numbers[i]
        previous = set(list_of_numbers[:i])
        if look in previous:
            result.append("YES")
        else:
            result.append("NO")
    # return result
    print(result)

@wrapper
def number_seen_simpler(list_of_numbers):
    result_set = set()
    result = []
    for x in list_of_numbers:
        if x not in result_set:
            result_set.add(x)
            result.append("NO")
        else:
            result.append("YES")
    # return result
    print(result)

# list_of_numbers = [1,2,1,2,4,5]
list_of_numbers = create_list(1000)

# print(number_seen(list_of_numbers))
# print(number_seen_simpler(list_of_numbers))

wrapper(number_seen(list_of_numbers))  # This function took 0.007970809936523438 seconds
print()
wrapper(number_seen_simpler(list_of_numbers))  # This function took 0.004003763198852539 seconds

