str1 = "The quick Brow Fox"

def num_of_char(str1):
    lower_count = 0
    upper_count = 0
    for i in str1[0:]:
        if (ord(i) >= 97 and ord(i) <= 122):
            lower_count = lower_count+1
        
        elif (ord(i) >= 65 and ord(i) <= 90):
            upper_count = upper_count+1

    return upper_count, lower_count
    # print("lower case letters count is :",lower_count)
    # print("upper case letters count is :",upper_count)

uc,lc = num_of_char(str1)
print("upper count = ",uc,"\nlower count =",lc)