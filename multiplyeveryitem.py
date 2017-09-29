# Write a Python program to multiplies all the items in a list. ?

import time
def multiply_list(item):
    multiply =1
    for x in item:
        multiply*=x

    print("After multiplication every item",multiply)

multiply_list([1,2,3])