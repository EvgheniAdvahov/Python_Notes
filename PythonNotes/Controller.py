from Data import write_data, search_data, search_data_for_change, write_new_dict, delete_note, print_all_notes
from View import user_input, input_data, input_search, input_del


def start():
    while True:
        userInput = user_input()
        match userInput:
            case 1:
                data = input_data()
                write_data(data)
                print("Успешно записано \n")
            case 2:
                data = input_search()
                search_data(data)
            case 3:
                data = input_search()
                dictionary = search_data_for_change(data)
                write_new_dict(dictionary)
                print("Успешно изменена")
            case 4:
                data = input_del()
                dictionary = delete_note(data)
                write_new_dict(dictionary)
            case 5:
                print_all_notes()
            case 6:
                print("Выход")
                return()

