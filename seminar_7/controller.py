import data_processing as dp
import view as vw

def show_directory():
    vw.show(dp.browse())


def show_search_result():
    vw.show(dp.find())


def write_data():
    dp.writing()