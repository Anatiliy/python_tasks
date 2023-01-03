# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:

# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# функция, создающая список (coefficients_polynominal) коэффециентов многочлена заданной
# степени (degree_num) в заданном диапазоне (от begin_item до end_item)
def create_polynominal(degree_num, begin_item = 0, end_item = 100):
    import random
    coefficients_polynominal = sorted(10 * list(range(begin_item, end_item + 1)))
    random.shuffle(coefficients_polynominal)
    coefficients_polynominal = random.sample(coefficients_polynominal, degree_num + 1)
    return coefficients_polynominal


# временный вывод
print(create_polynominal(int(input('введите натуральное число '))))    

