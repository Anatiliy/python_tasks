

# запись информации из переменной "data" в файл
def write_line(data):
    with open('telephone_directory.csv', 'a', encoding='utf-8') as output_file:
        print(*data, sep=';', file=output_file)


# считывание всей информации из файла в переменную "data"
def read_file():
    with open('telephone_directory.csv', 'r', encoding='utf-8') as input_file:
        data = list(map(lambda item: item.strip().split(';'), input_file.readlines()))
    return data


# перезапись файла информацией из переменной "data"
def overwrite(data):
    with open('telephone_directory.csv', 'w', encoding='utf-8') as output_file:
        output_file.writelines(list(map(lambda item: ';'.join(item) + '\n', data)))


# поиск информации в файле по ключу "key" с последующей записью в переменную "result_data"
def find(key):
    with open('telephone_directory.csv', 'r', encoding='utf-8') as input_file:
        data = input_file.readline()
        result_data = []
        while data != '':
            data = data.strip().split(';')
            if key.lower() in list(map(lambda item: item.lower(), data)):
                result_data.append(data)
            data = input_file.readline()
    return result_data
    
