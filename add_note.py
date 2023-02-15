import json
from datetime import datetime

import menu


def add():
    with open('notes.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    if (data['notes']['items'][-1]['id']).__eq__(0):
        note = {"id": 1,
                "header": input("Введите заголовок заметки: "),
                "text": input("Введите текст заметки: "),
                "create_date": datetime.now().strftime('%d.%m.%y %H:%M:%S'),
                "change_date": datetime.now().strftime('%d.%m.%y %H:%M:%S')}
        data['notes']['items'][0] = note
    else:
        note = {"id": data['notes']['items'][-1]['id'] + 1,
                "header": input("Введите заголовок заметки: "),
                "text": input("Введите текст заметки: "),
                "create_date": datetime.now().strftime('%d.%m.%y %H:%M:%S'),
                "change_date": datetime.now().strftime('%d.%m.%y %H:%M:%S')}
        data['notes']['items'].append(note)

    save = input("Сохранить заметку? yes/no: ")
    if save.lower().__eq__("yes"):
        with open('notes.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=3)
    elif save.lower().__eq__("no"):
        menu.menu()
    else:
        print("Введена не верная команда!")