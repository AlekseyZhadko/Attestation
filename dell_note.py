import json

import menu


def dell():
    print("Просмотреть все записки - all")
    print("Редактировать записку с id - dellid")
    print("Вернуться в меню: menu")
    command = input("Введите команду: ")

    with open('notes.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    if command.lower().__eq__("all"):
        for item in data['notes']['items']:
            print(item['id'], item['header'] + ";", item['text'] + ";", item['create_date'])
    elif command.lower().__eq__("dellid"):
        id_note = input("Введите id записки: ")
        if id_note.isdigit():
            for item in data['notes']['items']:
                if (item['id']) == int(id_note):
                    position = data['notes']['items'].index(item)
                    del data['notes']['items'][position]
                    save = input("Подтвердить удаление заметки? yes/no: ")
                    if save.lower().__eq__("yes"):
                        with open('notes.json', 'w', encoding='utf-8') as file:
                            json.dump(data, file, indent=3)
                    elif save.lower().__eq__("no"):
                        menu.menu()
                    else:
                        print("Введена не верная команда!")
        else:
            print("Введен некорректный id")
            dell()
    elif command.lower().__eq__("menu"):
        menu.menu()
