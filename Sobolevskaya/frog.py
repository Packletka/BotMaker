n = int(input())
ls = list(map(int, input().split()))

dc = {0: ls[0]}
for i in range(n):
    if i == 1:
        continue
    else:
        if i + 2 in dc:
            dc[i + 2] = max(dc[i + 2], dc[i] + ls[i + 2])
        elif i + 2 < n:
            dc[i + 2] = dc[i] + ls[i + 2]
        if i + 3 in dc:
            dc[i + 3] = max(dc[i + 3], dc[i] + ls[i + 3])
        elif i + 3 < n:
            dc[i + 3] = dc[i] + ls[i + 3]
print(dc[n - 1] if n > 2 else -1)
