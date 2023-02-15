import json


def read():
    print("Просмотреть все записки - all")
    print("Просмотреть записку по id - readid")
    print("Просмотреть записки в диапазоне дат - readdate")
    command = input("Введите команду: ")

    with open('notes.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    if command.lower().__eq__("all"):
        for item in data['notes']['items']:
            print(item['id'], item['header'] + ";", item['text'] + ";", item['create_date'])
    elif command.lower().__eq__("readid"):
        id_note = input("Введите id записки: ")
        if id_note.isdigit():
            for item in data['notes']['items']:
                if (item['id']) == int(id_note):
                    print(item['id'], item['header'] + ";", item['text'] + ";", item['create_date'])
        else:
            print("Введен некорректный id")
