list1 = [1,2,2,5,4,5,9,7,8,7,7,5,8,9,]

# Methode 1
def unique_no(list1):
    list2 = []
    for i in list1:
        if i not in list2:
            list2.append(i)
    return list2


print("unique list is",unique_no(list1))




# Methode 2

# def unique_no(list1):
     
#     set1 = set(list1)

#     list2 = (list(set1))

#     return list2

# print(unique_no(list1))