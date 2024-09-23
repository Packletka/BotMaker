def genf():
    for i in [1, 2, 3]:
        yield i

s = genf()
for j in genf():
    print(j)
