# Write a Python program to remove duplicates from a list ?

def remove_duplicate(list):
    dup_ele=set()
    single_ele=[]
    for items in list:
        if items not in dup_ele:
            single_ele.append(items)
            dup_ele.add(items)

    print(dup_ele)


remove_duplicate([10,20,30,20,10,50,60,40,80,50,40])
