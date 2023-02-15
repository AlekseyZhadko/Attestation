from default_notes import default_notes
from menu import menu


def run():
    default_notes()
    text = "Консольное приложение заметки notes.py"
    print(text.center(100, "_"))
    menu()

