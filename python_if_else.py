



def is_weird(n):

    if n % 2 != 0:
        return "weird"
    elif (n % 2 == 0) and (2<=n<=5):
        return "not weird"
    elif (n % 2 == 0) and (6<=n<=20):
        return "weird"
    elif (n % 2 == 0) and (20<n):
        return "not weird"
    else:
        return "not weird"

print(is_weird(5))
assert is_weird(5)== "weird", '5 must be weird'
assert is_weird(30)== "not weird", '7 must be not weird'