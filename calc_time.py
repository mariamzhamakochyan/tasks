import time
import math


def calc_time(func):
    def inner1(*args, **kwargs):
        begin = time.time()
        func(*args, **kwargs)
        end = time.time()
        print("Total time taken in: ", func.__name__, end - begin)

        return inner1
