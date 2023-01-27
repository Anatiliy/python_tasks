import data_processing as dp
import user_interface as ui


# вывод справочника на экран
def view_directory():
    ui.show(dp.read_file())
    main_program()


# поиск контакта и вывод найденого контакта на экран
def find_contact():
    key = ui.enter_data('введите фамилию, имя или номер телефона ')
    data = dp.find(key)
    if data:
        ui.show(data)
    else:
        ui.show_message('контакт не найден')
    main_program()


# запись контакта в справочник
def write_contact():
    contact = ui.enter_data('введите фамилию '), ui.enter_data('введите имя '), ui.enter_data('введите номер телефона ')
    dp.write_line(contact)
    main_program()


# удаление контакта из справочника
def delete_contact():
    key = ui.enter_data('введите номер телефона ')
    data = dp.read_file()
    for item in data:
        if key == item[2]:
            data.pop(data.index(item))
            ui.show_message('контакт удалён')
            dp.overwrite(data)
            break
    else:
        ui.show_message('контакт не найден')
    main_program()


# изменение существующего контакта
def change_contact():
    key = ui.enter_data('введите номер телефона изменяемого контакта ')
    data = dp.read_file()
    for item in data:
        if key == item[2]:
            ui.show([item])
            number = int(ui.change_contact_menu())
            while number in (1, 2, 3):
                item[number - 1] = ui.enter_data('введите новые данные ')
                dp.overwrite(data)
                ui.show_message('контакт изменён')
                ui.show([item])
                number = int(ui.change_contact_menu())
            break
    else:
        ui.show_message('контакт не найден')
    main_program()


# выход из программы
def exit():
    ui.show_message('До свидания!!!')

# логика основного меню
def main_program():
    menu_dict = {1:view_directory, 2:find_contact, 3:write_contact, 4:delete_contact, 5:change_contact, 0:exit}
    menu_dict[int(ui.main_menu())]()