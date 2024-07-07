# def merge(x, y):
#     if x == []: return y
#     if y == []: return x
#     return [x[0]] + merge(x[1:], y) if x[0] < y[0] else [y[0]] + merge(x, y[1:])
from heapq import merge
def sort(a):
    n = len(a)
    m = n//2
    return a if n <= 1 else list(merge(sort(a[:m]), sort(a[m:])))
print(sort([5, 4, 7, 3, 3, 2]))
