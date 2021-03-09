def square_list(n):
    list2 = []
    for i in range(1,n+1):
        a = i*i
        list2.append(a)
    return list2

print(square_list(30))