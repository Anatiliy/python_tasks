

def writing():
    with open('telephone_directory.csv', 'a', encoding='utf-8') as output_file:
        print(input('введите фамилию '), input('введите имя '), input('введите номер телефона '), sep=';', file=output_file)


def browse():
    with open('telephone_directory.csv', 'r', encoding='utf-8') as input_file:
        data = list(map(lambda item: item.strip().split(';'), input_file.readlines()))
    return data


def find():
    key = input('введите фамилию, имя или номер телефона ')
    print()
    with open('telephone_directory.csv', 'r', encoding='utf-8') as input_file:
        data = input_file.readline()
        result = []
        while data != '':
            data = data.strip().split(';')
            if key.lower() in list(map(lambda item: item.lower(), data)):
                result.append(data)
            data = input_file.readline()
    if result:
        return result
    else:
        print('контакт не найден')