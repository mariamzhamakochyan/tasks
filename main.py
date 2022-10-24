# class Stack:
#     def __init__(self):
#         self.top = -1
#         self.size = 0
#         self.lst = []
#
#     def top(self):
#         return self.lst[self.top]
#
#     def size(self):
#         return self.size
#
#     def push(self, ele):
#         self.lst.append(ele)
#         self.size += 1
#         self.top += 1
#
#     def pop(self):
#         if not self.isEmpty:
#             self.remove(self.top)
#             self.size -= 1
#             self.top -= 1
#         else:
#             raise 'Your stack is empty'
#
#     def isEmpty(self):
#         return self.size == 0
#
#     def clear(self):
#         while not self.isEmpty:
#             self.remove(self.pop)
#
#     def peek(self):
#         return self.lst[0]
#
#     def show(self):
#         return self.lst
#
# mylist = Stack()
# mylist.push(2)
# mylist.push(3)
# mylist.push(5)


item = []


def Stack(func):
    def st(*args):
        print("Func is starting " + func.__name__)
        func(*args)

    return st


@Stack
def push(it):
    item.append(it)


@Stack
def top():
    print(item[0])


@Stack
def peek():
    print(item[-1])


@Stack
def isEmpty():
    if len(item) == 0:
        print("Empty")
    else:
        print("Full")


@Stack
def clear():
    global item
    item = []
    print(item)


@Stack
def show():
    for x in item:
        print(x, end=' ')


@Stack
def size():
    print(len(item))


@Stack
def pop():
    if len(item) == 0:
        print("List is empty:")
    else:
        item.pop()


push(1)
push(2)
show()
