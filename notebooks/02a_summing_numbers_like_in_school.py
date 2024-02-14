"""Write a function that sums two numbers like in school. 
This means, that you should sum digits from right to left and 
carry 1 if the sum of two digits is greater than or equal to 10. 
HINT: you should use the zip_longest function and the modulo operator (%)
"""

from itertools import zip_longest


def sum_like_in_school(number_1, number_2, base=10):
    reverse_numer_1 = reversed(str(number_1))
    reverse_numer_2 = reversed(str(number_2))
    sum_list = zip_longest(reverse_numer_1, reverse_numer_2, fillvalue="0")
    
    result = ""
    carry = 0
    for digit_1, digit_2 in sum_list:
        digits_sum = int(digit_1) + int(digit_2) + carry
        
        if digits_sum >= base:
            carry = 1
            digits_sum = digits_sum % base
        else:
            carry = 0
        
        result = str(digits_sum) + result
    if carry:
        result = str(carry) + result
    return int(result)

print(sum_like_in_school(9, 1))

# Test
import random
for i in range(10):
    digit1=random.randint(1, 1000000)
    digit2=random.randint(1, 1000000)

    simple_sum = digit1 + digit2
    school_ab = sum_like_in_school(digit1, digit2)
    school_ba = sum_like_in_school(digit1, digit2)

    print(simple_sum == school_ab == school_ba)

