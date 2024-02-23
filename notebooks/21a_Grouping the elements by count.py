"""
The most_common() method returns a list of tuples. 
We want to return a dictionary where they keys are the counts and 
the values are lists that contain the elements with that count.

Example:

Input data:
["apple", "apple", "grapes", "grapes", "watermelon"]

Output:
{2: ["apple", "grapes"], 1: ["watermelon"]}
"""

from collections import Counter

def find_counts(list_of_elements):
    counts = Counter(list_of_elements)
    output = {}

    for element, count in counts.items():
        output[count] = output.setdefault(count, []) + [element]
    return output

list_of_elements = ["apple", "apple", "grapes", "grapes", "watermelon"]

find_counts(list_of_elements)

