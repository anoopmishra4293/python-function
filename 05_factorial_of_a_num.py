a = 5

def factorial(a):
    # if a == 1:
    #    return a
    # else:
    #    return a*factorial(a-1)
    fact = a*factorial(a-1)

    return (fact)

print(factorial(a))
