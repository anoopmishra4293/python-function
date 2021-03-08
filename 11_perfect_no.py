n = 28
list1 =[]

def perfect_num(n):
    for i in range(1,n//2+1):
        if n%i==0:
            list1.append(i)
    return list1


def add(list1):
    a = 0
    for i in list1:
        a = a+i
    return a

perfect_num(n)
# add(list1)
if n==add(list1):
    print(n,"is a perfect number")
else:
    print(n,"is not a perfect number")