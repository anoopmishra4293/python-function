list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = []

def even_no(list1):
    for i in list1:
        if i%2==0:
            list2.append(i)
    return list2

print("Even number in given list are :",even_no(list1)) 