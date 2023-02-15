import json
from datetime import datetime

import menu


def edit():
    print("Просмотреть все записки - all")
    print("Редактировать записку с id - editid")
    print("Вернуться в меню: menu")
    command = input("Введите команду: ")

    with open('notes.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    if command.lower().__eq__("all"):
        for item in data['notes']['items']:
            print(item['id'], item['header'] + ";", item['text'] + ";", item['create_date'])
    elif command.lower().__eq__("editid"):
        id_note = input("Введите id записки: ")
        if id_note.isdigit():
            for item in data['notes']['items']:
                if (item['id']) == int(id_note):
                    position = data['notes']['items'].index(item)
                    item = {"id": item['id'],
                            "header": input("Введите заголовок заметки: "),
                            "text": input("Введите текст заметки: "),
                            "create_date": item['create_date'],
                            "change_date": datetime.now().strftime('%d.%m.%y %H:%M:%S')}
                    print(item['id'], item['header'] + ";", item['text'] + ";", item['create_date'])
                    data['notes']['items'][position] = item
                    save = input("Сохранить заметку? yes/no: ")
                    if save.lower().__eq__("yes"):
                        with open('notes.json', 'w', encoding='utf-8') as file:
                            json.dump(data, file, indent=3)
                    elif save.lower().__eq__("no"):
                        menu.menu()
                    else:
                        print("Введена не верная команда!")
        else:
            print("Введен некорректный id")
            edit()
    elif command.lower().__eq__("menu"):
        menu.menu()
