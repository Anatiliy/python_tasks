


def calculating_expression(expression):
    if '(' in expression:
        begin_index = expression.index('(') + 1
        end_index = len(expression) - expression[::-1].index(')') - 1
        expression = expression[:begin_index - 1] + calculating_expression(expression[begin_index:end_index]) + expression[end_index + 1:]



st = '(26 + 9 * 2 - 4 * (5 - 7)) / 3'
lst = ''.join(map(lambda item: ' ' + item + ' ' if not item.isdigit() else item, st)).split()
print(lst)
print(lst.index('('), len(lst) - lst[::-1].index(')') - 1)
b = lst.index('(') + 1
e = len(lst) - lst[::-1].index(')') - 1
print(lst[b:e])
print(sum((b, -e)))