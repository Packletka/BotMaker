def count_valid_sequences(N, sequence):
    max_open = N // 2 + 1
    dp = [[0] * max_open for _ in range(N + 1)]
    dp[0][0] = 1

    for i in range(N):
        for j in range(max_open):
            if dp[i][j] == 0:
                continue

            char = sequence[i]
            if char in '([{':
                if j + 1 < max_open:
                    dp[i + 1][j + 1] = (dp[i + 1][j + 1] + dp[i][j]) % MOD
            elif char in ')]}':
                if j > 0:
                    dp[i + 1][j - 1] = (dp[i + 1][j - 1] + dp[i][j]) % MOD
            elif char == '?':
                if j + 1 < max_open:
                    dp[i + 1][j + 1] = (dp[i + 1][j + 1] + dp[i][j]) % MOD
                if j > 0:
                    dp[i + 1][j - 1] = (dp[i + 1][j - 1] + dp[i][j]) % MOD

    return dp[N][0]


with open('input.txt', 'r', encoding='utf-8') as file_1:
    with open('output.txt', 'w', encoding='utf-8') as file_2:
        MOD = 10 ** 9 + 7
        N = int(file_1.readline())
        sequence = file_1.readline()

        result = count_valid_sequences(N, sequence)
        file_2.write(str(result))
