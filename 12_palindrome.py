str1 = "nurses run"

def palindrome(str1):
    str2=str1.replace(" ", "")
    if str2 == str2[::-1]:
        return True
    else:
        return False

print(palindrome(str1))