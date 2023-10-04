from datetime import datetime


def user_input():
    ask = int(input("Выберите действие: \n "
                    "1 - Создать новую заметку \n "
                    "2 - Поиск заметки\n "
                    "3 - Изменить заметку \n "
                    "4 - Удалить заметку \n "
                    "5 - Распечатать все заметки \n "
                    "6 - Выход \n"))
    return ask

def input_data():
    dict = {}
    dict["idNote"] = input("Введите id заметки - ")
    dict["titleNote"] = input("Введите заголовок заметки - ")
    dict["textNote"] = input("Введите текст заметки - ")
    dict["dateTime"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return dict;

def input_search():
    data = input("Введите id для поиска заметки - ")
    return data

def input_del():
    data = input('Введите id заметки, которую хотите удалить ')
    return data

def input_for_del():
    data = int(input('введите номер строки которую хотите удалить '))
    return data
