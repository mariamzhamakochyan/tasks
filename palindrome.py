def palindrome(string):
    s1 = string.replace(' ', '')
    s1 = s1.lower()
    s2 = s1[::-1]
    if s1 == s2:
        return True
    else:
        return False


string = input("Enter the string: ")
print(palindrome(string))
