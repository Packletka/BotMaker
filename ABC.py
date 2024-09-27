with open('input.txt', 'r', encoding='utf-8') as file_1:
    with open('output.txt', 'w', encoding='utf-8') as file_2:
        N = int(file_1.readline())
        A = file_1.readline().split()
        B = file_1.readline().split()
        C = file_1.readline().split()

        summa = 0
        for i in range(N):
            if (B.count(A[i]) == 0 or C.count(A[i]) == 0) or (B.count(B[i]) > 1 or C.count(B[i]) == 0) or (
                    C.count(C[i]) > 1 or B.count(C[i]) == 0):
                summa += 1
                A[i], B[i], C[i] = "*" * 3

        file_2.write(str(summa))
