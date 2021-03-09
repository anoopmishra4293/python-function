a = "green-red-yellow-black-white"

def dict_order(a):
    b = a.split("-")
    b.sort()
    return "-".join(b)

print(dict_order(a))