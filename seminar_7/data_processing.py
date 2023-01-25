

def writing():
    data = input('введите фамилию ') + ';' + input('введите имя ') + ';' + input('введите номер телефона ') + '\n'
    with open('telephone_directory.csv', 'a', encoding='utf-8') as output_file:
        output_file.write(data)


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
    return result