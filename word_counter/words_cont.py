file = open('words.txt', 'r')
file = file.read()
file = file.split()
count = 0
for i in file:
    count += 1
print(count)
