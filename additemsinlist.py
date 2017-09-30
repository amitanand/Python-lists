# Write a Python program to sum all the items in a list?

def sum_List(items):
    sum=0
    for x in items:
        sum+=x

    print("Sum :",sum)

sum_List([1,2,3,4,5,6])