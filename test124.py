import numpy as np


def Find(List):
    n = Max(len(List), np.max(List))
    a = np.zeros(n)
    for i in List:
        if i > 0:
            a[i-1] = 1
    for i in range(len(List)):
        if a[i] == 0:
            return i+1


def Max(a, b):
    if a > b:
        return a
    else:
        return b


List = [-11, 1, 2, 4, 5, 9]
print(Find(List))
