# The first way of calling the module
import math_utils
print("The first way of calling modules")
print(math_utils.add(9,2))
print(math_utils.subtract(9,2))
print(math_utils.sqr(3))



# The second way of calling the module

from math_utils import add,subtract,sqr
print("The second way of calling modules")
print(add(6,7))
print(subtract(7,3))
print(sqr(7))

#Task 2

import string_utils

print(string_utils.capitalize_words("tutedude"))

print(string_utils.reverse_string("tutedude"))

print(string_utils.word_count("tutedude"))



from string_utils import capitalize_words,reverse_string,word_count

print(capitalize_words("tutedude"))

print(reverse_string("tutedude"))

print(word_count("tutedude"))



# Task 4 
import shop_package.discount as disc
import shop_package.billing as bil
from shop_package.billing import calculate_total 

print(disc.apply_discount(500, 20))
print(disc.flat_discount(500))


amount = (bil.calculate_total([34,54,23,11]))
print("Total bill: ", amount)

print("calculate total: ", calculate_total([1,2,3,4,5]))

print(f"Total amount after tax : {bil.apply_tax(amount)}")




