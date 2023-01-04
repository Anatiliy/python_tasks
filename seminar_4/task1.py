# A. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# B. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать
# файл, содержащий сумму многочленов.

# НЕОБЯЗАТЕЛЬНОЕ, ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ:
# Расширить значение коэффициентов до [-100..100]






# функция, создающая список (create_list_coefficients_polynominal) коэффециентов многочлена заданной
# степени (degree_num) в заданном диапазоне (от begin_item до end_item)
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


# функция, создающая многочлен степени degree_num с коэффициентами coefficient_list,
# записанный в виде строки

def create_polynominal(degree_num, coefficient_list):
    result_polynominal = ''
    for key, value in coefficient_list.items():
        result_polynominal += str(value) + '*x^' + str(key) + ' + '
    result_polynominal = result_polynominal.replace('+ -', '- ').replace('^1', '').replace('*x^0', '')[:-2] + '= 0'
    
    return result_polynominal


def writing_to_file(text_of_entry, file_name):
    with open(file_name, 'w', encoding='utf-8') as output_file:
        output_file.write(text_of_entry)


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




def addition_of_polynominals(file1_name, file2_name):
    with open(file1_name, 'r', encoding='utf-8') as input_file1, open(file2_name, 'r', encoding='utf-8') as input_file2:
        coefficients_polynominal1 = separation_of_coefficients_of_polynomial(input_file1.readline())
        coefficients_polynominal2 = separation_of_coefficients_of_polynomial(input_file2.readline())

    if max(coefficients_polynominal1) > max(coefficients_polynominal2):
        result_coefficients_polynominal = {}
        for key in  range(max(coefficients_polynominal1), -1, -1):
            result_coefficients_polynominal[key] = coefficients_polynominal1.get(key, 0) + coefficients_polynominal2.get(key, 0)
    else:
        result_coefficients_polynominal = {}
        for key in range(max(coefficients_polynominal1), -1, -1):
            result_coefficients_polynominal[key] = coefficients_polynominal1.get(key, 0) + coefficients_polynominal2.get(key, 0)

    return result_coefficients_polynominal

    

# временный вывод

#degree_num = int(input('введите натуральное число '))

#polynominal = create_polynominal(degree_num, create_list_coefficients_polynominal(degree_num, begin_item = -100))
#print(polynominal)
#print(separation_of_coefficients_of_polynomial(polynominal))
#writing_to_file(polynominal, input('введите имя файла, используя латинские буквы и цифры ') + '.txt')
addition_of_polynominals(input('введите имя файла 1, используя латинские буквы и цифры ') + '.txt',input('введите имя файла 2, используя латинские буквы и цифры ') + '.txt')