def binary_search(arr, x):
    n = len(arr)

    # Поиск индекса первого элемента, большего или равного x
    def find_first_ge(arr, x):
        low, high = 0, n
        while low < high:
            mid = (low + high) // 2
            if arr[mid] < x:
                low = mid + 1
            else:
                high = mid
        return low

    # Поиск индекса первого элемента, большего x
    def find_first_gt(arr, x):
        low, high = 0, n
        while low < high:
            mid = (low + high) // 2
            if arr[mid] <= x:
                low = mid + 1
            else:
                high = mid
        return low

    l = find_first_ge(arr, x)
    r = find_first_gt(arr, x)

    b = 1 if l < n and arr[l] == x else 0

    return b, l, r


# Чтение входных данных
n = int(input().strip())
if n > 0:
    arr = list(map(int, input().strip().split()))
else:
    arr = []

k = int(input().strip())
if k > 0:
    queries = list(map(int, input().strip().split()))
else:
    queries = []

# Обработка запросов
results = []
for query in queries:
    result = binary_search(arr, query)
    results.append(result)

# Вывод результатов
for b, l, r in results:
    print(b, l, r)
