# Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.?

import time
def remove_ele(list):
    print("Removing 0th,4th & 5th element ...")
    time.sleep(1)
    list.pop(0)
    list.pop(4)
    list.pop(5)
    print("Resulting list :",list)

remove_ele([1,2,3,4,5,6,7,8,9,10])
remove_ele(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow','Blue','Magenta'])