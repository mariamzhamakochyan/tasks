def rev(str):
    res = str.split()
    result = [i[::-1] for i in res]
    rev_ = ' '.join(result)
    return rev_


str = input("Enter the string")
print(rev(str))
