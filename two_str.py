def str(str1, str2):
    if str1 == str2:
        return 0
    elif len(str1) != len(str2):
        return -1
    elif len(str1) == len(str2):
        count = 0
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                count += 1
        return count

