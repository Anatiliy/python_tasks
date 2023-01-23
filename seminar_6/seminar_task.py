


def adding(a, b):
    return a + b


def subtracting(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def dividing(a, b):
    return a / b


def exponentiation(a, b):
    return a ** b

def calculating_expression(expression):
    math_operations = {'^': exponentiation, '*': multiplication, '/': dividing, '+': adding, '-': subtracting}
    if '(' in expression:
        begin_index = expression.index('(') + 1
        end_index = len(expression) - expression[::-1].index(')') - 1
        expression = expression[:begin_index - 1] + [calculating_expression(expression[begin_index:end_index])] + expression[end_index + 1:]
    for key in math_operations:
        while key in expression:
            index = expression.index(key)
            a = expression[index - 1]
            b = expression[index + 1]
            expression = expression[:index - 1] + [math_operations[key](a, b)] + expression[index + 2:]
    return expression[0]




st = '(26 + 9 ** 2 - 4 * (5 - 7)) : 3'
st = st.replace('**', '^').replace(':', '/')
lst = list(map(lambda item: int(item) if item.isdigit() else item, ''.join(map(lambda item: ' ' + item + ' ' if not item.isdigit() else item, st)).split()))
print(lst)
print(calculating_expression(lst))