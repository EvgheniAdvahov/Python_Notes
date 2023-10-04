import json
from View import input_data


def write_data(new_data, filename='Note.json', encoding="UTF-8"):
    with open(filename, 'r+') as file:
        file_data = json.load(file)
        print("This is data from json", file_data)
        print(type(file_data))
        file_data["Notes"].append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent=4)


def search_data(searchData, filename='Note.json'):
    flag = False
    with open(filename, 'r+', encoding="UTF-8") as file:
        file_data = json.load(file)
        for dict in file_data.values():
            for item in dict:
                for key, value in item.items():
                    if value == searchData:
                        print("Успешно найдено")
                        pretty = json.dumps(item, indent=4)
                        print(pretty)
                        flag = True
        if (flag == False):
            print("Заметка не найдена")

def search_data_for_change(searchData, filename='Note.json'):
    flag = False
    with open(filename, 'r+', encoding="UTF-8") as file:
        file_data = json.load(file)
        for list in file_data.values():
            for i in range(len(list)):
                for key,value in list[i].items():
                    if key == "idNote" and value ==searchData:
                        print("Заметка с id ", searchData, "найдена")
                        print("Введите данные для замены")
                        list[i] = input_data()
                        flag = True
        if(flag == False):
            print("Заметка не найдена")
        return file_data

def delete_note(searchData, filename='Note.json'):
    flag = False
    with open(filename, 'r+', encoding="UTF-8") as file:
        file_data = json.load(file)
        for my_list in file_data.values():
            for i in range(len(my_list)):
                for key, value in my_list[i].items():
                    if key == "idNote" and value == searchData:
                        print("Заметка с id ", searchData, "найдена")
                        index_element_de = i
                        flag = True
        if (flag == False):
            print("Заметка не найдена")
            return file_data
        else:
            del (my_list[index_element_de])
            print("Заметка с id ", searchData, "удаленна")
        return file_data

def write_new_dict(dictionary, filename='Note.json'):
    with open(filename, 'w') as file:
        json.dump(dictionary, file, indent=4)

def print_all_notes(filename='Note.json'):
    with open(filename, 'r+', encoding="UTF-8") as file:
        file_data = json.load(file)
        for dict in file_data.values():
            for item in dict:
                pretty = json.dumps(item, indent=4)
                print(pretty)



