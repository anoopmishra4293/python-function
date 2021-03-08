n = input("Enter a number to check that is is prime or not :")
n = int(n)

def prime_num(n):
    if n>1:
        for divisor in range(2,n//2+1):
            if n % divisor == 0 :
                return False
            else:
                return True
    else:
        ("Entered number is not a prime number.")

print(prime_num(n))