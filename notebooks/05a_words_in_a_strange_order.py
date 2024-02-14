"""
One of your friends wants to learn new English words, 
but wants to do it in a certain order. 
First, he chooses short words, and if the words are the same length, 
he chooses them in lexicographical order when reading from right to left (he is Arab!). 
Write a function that receives as an argument a list of words, 
and returns a list in the order specified.

Here is an example:

Input data:
["west", "tax", "size", "sea", "use", "think", "yard", "word", "town"]
 
Program output:
["sea", "use", "tax", "yard", "word", "size", "town", "west", "think"]
"""


def learning_words(list_of_words):
    sorted_words = sorted(list_of_words, key=lambda word: (len(word), word[::-1]))
    return sorted_words

list_of_words = ["west", "tax", "size", "sea", "use", "think", "yard", "word", "town"]
print(learning_words(list_of_words))
