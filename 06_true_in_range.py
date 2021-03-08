a = input("Enter a number to check that it is in range or not : ")
a = int(a)

def num(a):
    if a in range(5,10):
        return True
    else:
        return False

print(num(a))
