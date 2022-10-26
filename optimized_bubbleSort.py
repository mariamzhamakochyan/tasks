def optimized_bubbleSort(list):
    for i in range(0, len(list)):
        swap = False
        for j in range(0, len(list) - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                swap = True
        if not swap:
            return list


list = [1, 5, 3, 8, 9, 12]
print(optimized_bubbleSort(list))
