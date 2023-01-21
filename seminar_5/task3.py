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


def file_compression(original_data):
    intermediate_result = list([])
    index = 0
    for char in original_data:
        if char in intermediate_result[index]:
            intermediate_result[index][0] += 1
        else:
            intermediate_result[index] = [1, char]
            intermediate_result.append([])
            index += 1
    result = ''.join(tuple(map(lambda item: str(item[0]) + item[1]), intermediate_result))
    return result


def file_expantion(compressed_file):
    intermediate_result = str(map(lambda char: char + ' ' if char.isalpha() else char, compressed_file)).split()
    result = ''.join(map(lambda item: item[-1] * int(item[:-1]), intermediate_result))
    return result


 


