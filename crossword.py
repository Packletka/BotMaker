def find_words(crossword, R, C):
    words = []

    for row in crossword:
        for word in row.split('#'):
            if len(word) >= 2:
                words.append(word)

    for col in range(C):
        column_word = ''
        for row in range(R):
            column_word += crossword[row][col]
        for word in column_word.split('#'):
            if len(word) >= 2:
                words.append(word)

    return words


def main():
    R, C = map(int, file_1.readline().split())
    crossword = [file_1.readline().strip() for _ in range(R)]
    words = find_words(crossword, R, C)
    result = min(words)

    return result


with open('input.txt', 'r', encoding='utf-8') as file_1:
    with open('output.txt', 'w', encoding='utf-8') as file_2:
        file_2.write(main())
