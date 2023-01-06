# A. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# B. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать
# файл, содержащий сумму многочленов.

# НЕОБЯЗАТЕЛЬНОЕ, ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ:
# Расширить значение коэффициентов до [-100..100]






# функция, создающая список коэффециентов многочлена "create_list_coefficients_polynominal"
# заданной степени "degree_num" в заданном диапазоне от "begin_item" до "end_item"

def create_list_coefficients_polynominal(degree_num, begin_item = 0, end_item = 100):
    import random
    coefficients_polynominal = sorted(degree_num * list(range(begin_item, end_item + 1)))
    random.shuffle(coefficients_polynominal)
    coefficients_polynominal = random.sample(coefficients_polynominal, degree_num + 1)
    if coefficients_polynominal[-1] == 0:
        return create_list_coefficients_polynominal(degree_num, begin_item, end_item)
    else:
        coefficients_polynominal = {i:coefficients_polynominal[i] for i in range(degree_num, -1, -1)}
        return coefficients_polynominal


# функция, создающая многочлен строкового типа "result_polynominal" из списка
# коэффициентов "coefficient_list"

def create_polynominal(coefficient_list):
    result_polynominal = ''
    for key, value in coefficient_list.items():
        result_polynominal += str(value) + '*x^' + str(key) + ' + '
    result_polynominal = result_polynominal.replace('+ -', '- ').replace('^1', '').replace('*x^0', '')[:-2] + '= 0'
    
    return result_polynominal


# функция, записывающая заданный текст "text_of_entry" в файл с заданным именем "file_name"

def writing_to_file(text_of_entry, file_name):
    with open(file_name, 'w', encoding='utf-8') as output_file:
        output_file.write(text_of_entry)


# функция, извлекающая список коэффициентов "coefficients_polynominal" из заданного
# многочлена строкового типа "polynominal"

def separation_of_coefficients_of_polynomial(polynominal):
    polynominal = polynominal.replace('- ', '+ -').rstrip(' = 0').split(' + ')
    coefficients_polynominal = [0 for _ in range(int(polynominal[0].split('*x^')[1]) + 1)]
    for item in polynominal:
        if '*x^' in item:
            item = item.split('*x^')
            coefficients_polynominal[int(item[1])] = int(item[0])
        elif '*x' in item:
            item = item.rstrip('*x')
            coefficients_polynominal[1] = int(item)
        else:
            coefficients_polynominal[0] = int(item)
    coefficients_polynominal = {i:coefficients_polynominal[i] for i in range(len(coefficients_polynominal) - 1,-1,-1)}
    
    return coefficients_polynominal


# функция, извлекающая строку "coefficients_polynominal" из файла заданного имени "file_name"

def extract_from_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as input_file:
        coefficients_polynominal = input_file.readline()
    return coefficients_polynominal    


# функция, создающая список коэффициентов многочлена "result_coefficients_polynominal" из
# заданных списков коэффициентов многочлена "coefficients_polynominal1" и
# "coefficients_polynominal2", путём сложения коэффициентов одноимённых степеней

def addition_of_polynominals(coefficients_polynominal1, coefficients_polynominal2):
    if max(coefficients_polynominal1) > max(coefficients_polynominal2):
        result_coefficients_polynominal = {}
        for key in  range(max(coefficients_polynominal1), -1, -1):
            result_coefficients_polynominal[key] = coefficients_polynominal1.get(key, 0) + coefficients_polynominal2.get(key, 0)
    else:
        result_coefficients_polynominal = {}
        for key in range(max(coefficients_polynominal2), -1, -1):
            result_coefficients_polynominal[key] = coefficients_polynominal1.get(key, 0) + coefficients_polynominal2.get(key, 0)

    return result_coefficients_polynominal

    

# основная программа

for _ in range(int(input('введите количество создаваемых файлов '))):
    degree_num = int(input('задайте степень многочлена в виде натурального числа '))
    begin_item = int(input('задайте начало диапазона многочленов в виде натурального числа '))
    end_item = int(input('задайте конец диапазона многочленов в виде натурального числа '))

    polynominal = create_polynominal(create_list_coefficients_polynominal(degree_num, begin_item, end_item))
    print(polynominal)
    writing_to_file(polynominal, input('введите имя файла, используя латинские буквы и цифры ') + '.txt')


polynominal = create_polynominal(addition_of_polynominals(separation_of_coefficients_of_polynomial(extract_from_file(input('введите имя файла 1, используя латинские буквы и цифры ') + '.txt')), separation_of_coefficients_of_polynomial(extract_from_file(input('введите имя файла 2, используя латинские буквы и цифры ') + '.txt'))))
print(polynominal)
writing_to_file(polynominal, input('введите имя файла, используя латинские буквы и цифры ') + '.txt')
