def func(end):
    return 3/4 if end == 2 else (1 - 1/end**2) * func(end - 1)


[print(func(i)) for i in range(2, 73, 10)]
