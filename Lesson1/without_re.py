with open("input.txt", 'r', encoding='utf-8') as file_2_read:
    operations = file_2_read.readlines()
    with open("output.txt", 'w', encoding='utf-8') as file_2_write:
        [file_2_write.write(str(eval(oper)) + "\n") for oper in operations]
        file_2_write.close()
