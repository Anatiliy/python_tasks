# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# aaaaabbbcccc -> 5a3b4c
# 5a3b4c -> aaaaabbbcccc


def extract_from_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as input_file:
        data_from_file = input_file.readline()
    return data_from_file


def writing_to_file(text_of_entry, file_name):
    with open(file_name, 'w', encoding='utf-8') as output_file:
        output_file.write(text_of_entry)


def file_compression(source_file, result_file):
    source_data = extract_from_file(source_file)
    intermediate_result = [[0, source_data[0]]]
    index = 0
    for char in source_data:
        if char in intermediate_result[index]:
            intermediate_result[index][0] += 1
        else:
            index += 1
            intermediate_result.append([1, char])
    result = ''.join(tuple(map(lambda item: str(item[0]) + item[1], intermediate_result)))
    writing_to_file(result, result_file)
    

def file_expantion(source_file, result_file):
    compressed_data = extract_from_file(source_file)
    intermediate_result = ''.join(map(lambda char: char + ' ' if not char.isdigit() else char, compressed_data)).split()
    result = ''.join(map(lambda item: item[-1] * int(item[:-1]), intermediate_result))
    writing_to_file(result, result_file)


def main_program():
    key = input('введите "С", если нужно сжать файл, введите "P", если нужно расжать файл ')
    if key in 'cCсС':
        file_compression(input('введите имя сжимаемого файла ') + '.txt', input('введите имя файла для хранения сжатых данных ') + '.txt')
    elif key in 'PpРр':
        file_expantion(input('введите имя расжимаемого файла ') + '.txt', input('введите имя файла для хранения расжатых данных ') + '.txt')
    else:
        print('ввод не верный')
        return main_program()


#основная программа
data = 'dddddkjfkja;;;ddddkkkkkkkjjgaeeeeioiamdnnnnnnnnnnnnnnlalalakddddddddddddddd'
writing_to_file(data, 'f1.txt')

main_program()
