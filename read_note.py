import json

import menu


def read():
    print("Просмотреть все записки - all")
    print("Просмотреть записку по id - readid")
    print("Просмотреть записки по дате - readdate")
    print("Вернуться в меню - menu")
    command = input("Введите команду: ")

    with open('notes.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    if command.lower().__eq__("all"):
        for item in data['notes']['items']:
            print(item['id'], item['header'] + ";", item['text'] + ";", item['create_date'])
        read()
    elif command.lower().__eq__("readdate"):
        create_date_note = input("Введите дату в формате dd.mm.yy: ")
        for item in data['notes']['items']:
            if (create_date_note == ("".join(item['create_date']).split())[0]):
                print(item['id'], item['header'] + ";", item['text'] + ";", item['create_date'])
        print("Выборка завершена! (Если данные отсутсвуют, то заметок нет или некорректная дата!)")
        read()
    elif command.lower().__eq__("readid"):
        id_note = input("Введите id записки: ")
        if id_note.isdigit():
            for item in data['notes']['items']:
                if (item['id']) == int(id_note):
                    print(item['id'], item['header'] + ";", item['text'] + ";", item['create_date'])
        else:
            print("Введен некорректный id")
            read()
    elif command.lower().__eq__("menu"):
        menu.menu()
