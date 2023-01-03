# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:

# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


# функция, создающая список (create_list_coefficients_polynominal) коэффециентов многочлена заданной
# степени (degree_num) в заданном диапазоне (от begin_item до end_item)
def create_list_coefficients_polynominal(degree_num, begin_item = 0, end_item = 100):
    import random
    coefficients_polynominal = sorted(degree_num * list(range(begin_item, end_item + 1)))
    random.shuffle(coefficients_polynominal)
    coefficients_polynominal = random.sample(coefficients_polynominal, degree_num + 1)
    if coefficients_polynominal[0] == 0:
        return create_list_coefficients_polynominal(degree_num, begin_item, end_item)
    return coefficients_polynominal


def create_polynominal(degree_num, coefficient_list):
    result_polynominal = ''
    for c in coefficient_list:
        if degree_num > 1 and c != 0:
            result_polynominal += str(c) + '*x^' + str(degree_num) + ' + '
            degree_num -= 1
        elif degree_num == 1 and c != 0:
            result_polynominal += str(c) + '*x' + ' + '
            degree_num -= 1
        elif degree_num == 0 and c != 0:
            result_polynominal += str(c) + ' = 0'
    
    return result_polynominal



# временный вывод

degree_num = int(input('введите натуральное число '))
print(create_polynominal(degree_num, create_list_coefficients_polynominal(degree_num)))  

