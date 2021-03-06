list1=[]
element = int(input("Enter the number of elements in list :  "))
print("Enter elements in list")

for i in range(element):
    x=int(input())
    list1.append(x)
print(list1)

def multiplication(list1):
    product = 1
    for j in list1:
        product = product*j

    return(product)

print("multiplication of all elements of list is : ", multiplication(list1))
