
def sum_multiple(*args):
    sum=0
    for key in args:
        sum=sum+key
    return sum

print(sum_multiple(1,2,3,4,5,6,7,8,9,10,23))