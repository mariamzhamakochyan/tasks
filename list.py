def cases(string):

    c = string[0] + string[1].upper() + string[2]
    c1 = string[0] + string[1] + string[2].upper()
    lst = [string.capitalize(), c, c1]
    return lst


string = "cat"
print(cases(string))
