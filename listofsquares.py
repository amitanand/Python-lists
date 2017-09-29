'''Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between
 1 and 30 included ?'''

def print_square():
    list_ele=[]
    for i in range(1,21):
        list_ele.append(i**2)

    print(list_ele[:5])


print_square()