# Write a Python program to clone or copy a list ?

def clone_list(list):
    copy_list=[]
    for items in list:
        copy_list.append(items)

    print("This is the cloned copy of the list",copy_list)


clone_list([1,2,3,6,5,4,7,8,9])
        