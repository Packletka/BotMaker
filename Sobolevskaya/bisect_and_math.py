from datetime import datetime
from bisect import bisect_left
from math import log2, ceil

a = datetime.now()
n = 300000
ls1 = [_ for _ in range(1, n)]
k = 300000
ls2 = [_ for _ in range(1, k)]

for elem in ls2:
    # b
    i = bisect_left(ls1, elem)
    if i != len(ls1) and ls1[i] == elem:
        print(1, end=' ')
    else:
        print(0, end=' ')
    # l
    left, right = 0, len(ls1) - 1
    for i in range(ceil(log2(len(ls1))) + 1):
        mid = (left + right) // 2
        if ls1[mid] < elem:
            left = mid + 1
        else:
            right = mid
    print(n if left == n else left, end=' ')
    # r
    left, right = 0, len(ls1) - 1
    for i in range(ceil(log2(len(ls1))) + 1):
        mid = (left + right) // 2
        if ls1[mid] <= elem:
            left = mid + 1
        else:
            right = mid - 1
    print(n if left == n else left)
b = datetime.now()
print(b - a)
