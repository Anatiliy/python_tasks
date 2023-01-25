import controller as ct

def viewing():
    ct.show_directory()
    print()
    main_menu()


def search():
    ct.show_search_result()
    print()
    main_menu()


def record():
    ct.write_data()
    print()
    main_menu()


def exit():
    print('до свидания!!!')


def main_menu():
    menu_dict = {1:viewing, 2:search, 3:record, 0:exit}
    print('1. Для просмотра телефонного справочника введите "1"')
    print('2. Для поиска контакта введите "2"')
    print('3. Для записи нового контакта введите "3"')
    print('4. Для выхода из программы введите "0"')
    menu_dict[int(input())]()
