x = input("Enter first number: ")
x = int(x)

y = input("Enter second number: ")
y = int(y)

z = input("Enter third number: ")
z = int(z)

l = [x, y, z]

def max1(x,y,z):
    if x >= y and x >= z:
        largest = x
    elif y >= x and y >= z:
        largest = y
    else:
        largest = z

    return largest

print(max1(x,y,z))