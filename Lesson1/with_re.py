import re


with open('input.txt', 'r', encoding='utf-8') as file_2_read:
    if not all(re.match(r"[\d\-+%/*]+", expression) for expression in file_2_read.readlines()):
        raise ValueError("Выражение не является корректным")
    with open('output.txt', 'r', encoding='utf-8') as file_2_write:
        file_2_write.writelines(str(eval(i)) + '\n' for i in file_2_read.readlines())
