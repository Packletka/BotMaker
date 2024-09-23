from sympy import sympify


with open('input.txt', 'r', encoding='utf-8') as file_2_read:
    with open('output.txt', 'w', encoding='utf-8') as file_2_write:
        file_2_write.writelines([f"{float(sympify(i).evalf())}\n" for i in file_2_read.readlines()])
        file_2_write.close()
