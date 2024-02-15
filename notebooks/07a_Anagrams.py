"""
You will write a function that receives two arguments: a word and a list of words and stay with all of those words in the list that are anagrams of the word passed. If you don't remember what an anagram is, look at this article: Anagram

Input:
First argument: "code"
Second argument: ["code", "deco", "ecod", "first", "strif", "frist"]
Output:
["code", "deco", "ecod"]
HINT: You should clearly use the filter function and the sorted function.
"""


def find_anagrams(word, list_of_words):
    # return list(filter(lambda anagram: ''.join(sorted(anagram)) == ''.join(sorted(word)), list_of_words))
    return list(filter(lambda anagram: sorted(anagram) == sorted(word), list_of_words))

filtered_list = find_anagrams("code", ["code", "deco", "ecod", "first", "strif", "frist"])
print(filtered_list)