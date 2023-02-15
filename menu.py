from add_note import add
from read_note import read

def menu():
    print("Добавить - add")
    print("Редактировать - edit")
    print("Удалить - edit")
    print("Проcмотреть - read")
    command = input("Введите команду: ")

    if command.lower().__eq__("add"):
        add()
    elif command.lower().__eq__("read"):
        read()