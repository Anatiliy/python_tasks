import data_processing as dp
import view as vw


# вывод справочника на экран
def show_directory():
    vw.show(dp.browse())


# вывод найденого контакта на экран
def show_search_result():
    vw.show(dp.find())


# запись контакта в справочник
def write_data():
    dp.writing()


# удаление контакта из справочника
def delete_data():
    dp.delete()