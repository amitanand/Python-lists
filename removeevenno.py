#  Write a Python program to print the numbers of a specified list after removing even numbers from it.?


import time
def remove_even(list):
    for i in list:
        if i%2 ==  0:
            list.remove(i)

    print("Removing even numbers from the list ... :")
    time.sleep(1)
    print(list)

remove_even([1,2,3,4,5,6,7,8,9])
remove_even([7,8, 120, 25, 44, 20, 27])