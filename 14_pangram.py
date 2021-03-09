str1 = "The quick brown fox jumps over the lazy dog"

# Methode 1
list1=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
list2=[]

def pangram(str1):
    str2=str1.upper()

    for i in str2:
        for j in list1:
            if i==j:
                list1.remove(j)
    if list1==list2:
        return True
    else:
        return False

print(pangram(str1))



# Methode 2
# def fncn(str1):
#     l = [0]*26
#     for x in str1.lower():
#         if ord(x)>=ord('a') and ord(x)<=ord('z'):
#             l[ord(x)-ord('a')]+=1

#     if min(l)>0:
#         return True
#     else:
#         return False

# print(fncn(str1))