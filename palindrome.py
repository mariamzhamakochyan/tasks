def palindrome(string):
    res = "".join(reversed(string))
    if string == res:
        return True
    else:
        return False


string = input("Enter the string: ")
print(palindrome(string))
