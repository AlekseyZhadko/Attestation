import sys

from add_note import add
from dell_note import dell
from edit_note import edit
from read_note import read

def menu():
    print("Добавить - add")
    print("Редактировать - edit")
    print("Удалить - dell")
    print("Проcмотреть - read")
    print("Завершить программу - exit")
    command = input("Введите команду: ")

    if command.lower().__eq__("add"):
        add()
    elif command.lower().__eq__("edit"):
        edit()
    elif command.lower().__eq__("dell"):
        dell()
    elif command.lower().__eq__("read"):
        read()
    elif command.lower().__eq__("exit"):
        sys.exit()