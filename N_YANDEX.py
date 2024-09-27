with open('input.txt', 'r', encoding='utf-8') as file_1:
    with open('output.txt', 'w', encoding='utf-8') as file_2:
        N, B = map(int, file_1.readline().split())
        ls = list(map(int, file_1.readline().split()))
        summa = 0
        for i in range(0, N, 2):
            for j in range(N - i):
                srt_massive = ls[j:j + i + 1]
                summa += 1 if sorted(srt_massive)[i // 2] == B else 0
        file_2.write(str(summa))
