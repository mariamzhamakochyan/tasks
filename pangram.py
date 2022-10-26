def pangram(string):
    list = []
    if len(string) < 26:
        return False
    for i in string:
        for j in i:
            if j not in list:
                list.append(j)
            else:
                list.remove(j)
    if len(list) == len(string):
        return True
    else:
        return False


string = 'qwertyuioplkjhgfdsazxcvbnm'
print(pangram(string))
