

# вывод на экран вложенного списка "data"
def show(data):
    if data:
        data.sort()
        print('______________________________________')
        print('Фамилия     Имя         Номер телефона')
        print('--------------------------------------')
        for row in data:
            for item in row:
                print(item.ljust(12), end='')
            print()
        print('______________________________________')