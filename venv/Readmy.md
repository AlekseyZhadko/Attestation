## Промежуточная аттестация
### Приложение заметки
### Информация о проекте
Необходимо написать проект, содержащий функционал работы с заметками.
Программа должна уметь:
* создавать заметку, 
* сохранять её, 
* читать список заметок, 
* редактировать заметку, 
* удалять заметку.
### Как сдавать проект
Для сдачи проекта необходимо создать отдельный общедоступный
репозиторий (Github, gitlub, или Bitbucket). Разработку вести в этом
репозитории, использовать пул реквесты на изменения. Программа должна
запускаться и работать, ошибок при выполнении программы быть не должно.
### Задание
#### Реализовать консольное приложение заметки:
* с сохранением,
* чтением,
* добавлением, 
* редактированием, 
* удалением заметок. <br>

#### Заметка должна содержать: 
* идентификатор, 
* заголовок, 
* тело заметки 
* дату/время создания или последнего изменения заметки.<br>

Сохранение заметок необходимо сделать в формате json или csv формат (разделение полей рекомендуется делать через
точку с запятой). Реализацию пользовательского интерфейса студент может
делать как ему удобнее, можно делать как параметры запуска программы
(команда, данные), можно делать как запрос команды с консоли и
последующим вводом данных, как-то ещё, на усмотрение студента. 
#### Например:
python notes.py add --title "новая заметка" –msg "тело новой заметки"
##### Или так:
* python note.py
* Введите команду: add
* Введите заголовок заметки: новая заметка
* Введите тело заметки: тело новой заметки
* Заметка успешно сохранена
* Введите команду: <br><br>
При чтении списка заметок реализовать фильтрацию по дате.
### Критерии оценки
Приложение должно запускаться без ошибок, должно уметь сохранять данные
в файл, уметь читать данные из файла, делать выборку по дате, выводить на
экран выбранную запись, выводить на экран весь список записок, добавлять
записку, редактировать ее и удалять.
***
# Документация
### Запуск программы производится по средствами запуска функции run
main.py -> run()

### Функция run 
app.py -> run() Запускает проверку на доступность файла, если таковой
отсутствует, создаёт. Выводит в консоль название программы, а так же 
запускает меню.

    default_notes()
    text = "Консольное приложение заметки notes.py"
    print(text.center(100, "_"))
    menu() 

### функция default_notes

Данная функция проверяет есть ли json файл в директории, если он отсуствует то
создаёт данный файл. Если же файл существует, но он пустой, добавляет в файл 
структуру заметки.

    default_json = """
        {
        "notes": {
            "items": [{
                "id":0,
                "header": "",
                "text": "",
                "create_date": "",
                "change_date": ""
            }]
        }
        }"""
    default_data = json.loads(default_json)

    if (os.path.exists("notes.json")):
        if (os.stat("notes.json").st_size == 0):
            with open('notes.json', 'w', encoding='utf-8') as file:
                json.dump(default_data, file, indent=3)
    else:
        with open('notes.json', 'w', encoding='utf-8') as file:
            json.dump(default_data, file, indent=3)

### Функция menu()

Функция меню, печатает меню, в котором указаны команды для приложения заметки.

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
    else:
        print("Введенная команда не верна! Повторите Ввод")
        menu()

### Функция add

Данная функция производит добавление заметки. Для начала открываем файл на чтение
и проверяем есть ли в данном файле заметки. Если заметок нет то начинаем нумерацию с 1 
и добавляем заметку. Или же если есть заметки, берём последний id и увеличиваем его на еденицу
добавляя новую заметку. После заполнения заметки у пользователя спрашивается нужно ли её сохранить?
У пользователя на выбор да или нет. При заполнении неверных команд пользователь снова попадает
в функцию "add", если же всё корректно заполнено пользователь попадает в главное меню!

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
        menu.menu()
    elif save.lower().__eq__("no"):
        menu.menu()
    else:
        print("Введена не верная команда!")
        menu.menu()

### Функция Edit

В данной функции есть собственное меню, в котором предлагается выбрать: просмотр
всех записок, редактирование записок по id <br>
Подключаемся к файлу, после чего в зависимости от выбранного действия: Если просматриваем 
все записи, то выводим полный список в консоль и снова выводим меню.
Если же выбираем редактирование по id, от пользователя требуется ввести id. После чего программа
проверит на наличие данной записки. В положительном результате пользователя попросит
ввести новый заголовок и текст записки, иначе пользователю выведется сообщение о том что
такой id не существует или некорректен. По окончанию работы пользователя программа вернёт в Меню!

    print("Просмотреть все записки - all")
    print("Редактировать записку с id - editid")
    print("Вернуться в меню - menu")
    command = input("Введите команду: ")

    with open('notes.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    if command.lower().__eq__("all"):
        for item in data['notes']['items']:
            print(item['id'], item['header'] + ";", item['text'] + ";", item['create_date'])
        edit()
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
                        edit()
        else:
            print("Введен некорректный id")
            edit()
    elif command.lower().__eq__("menu"):
        menu.menu()

### Функция Dell

Данная функция работает по аналогии с предыдущей, есть собственное меню,
в котором предлагается выбрать: просмотр
всех записок, удаление записок по id <br>
Подключаемся к файлу, после чего в зависимости от выбранного действия: Если просматриваем 
все записи, то выводим полный список в консоль и снова выводим меню.
Если же выбираем удаление по id, от пользователя требуется ввести id. После чего программа
проверит на наличие данной записки. В положительном результате пользователя попросит
подтвердить удаление записки, иначе пользователю выведется сообщение о том что
такой id не существует или некорректен. По окончанию работы пользователя программа вернёт в Меню!

    print("Просмотреть все записки - all")
    print("Редактировать записку с id - dellid")
    print("Вернуться в меню - menu")
    command = input("Введите команду: ")

    with open('notes.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    if command.lower().__eq__("all"):
        for item in data['notes']['items']:
            print(item['id'], item['header'] + ";", item['text'] + ";", item['create_date'])
        dell()
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
                        dell()
        else:
            print("Введен некорректный id")
            dell()
    elif command.lower().__eq__("menu"):
        menu.menu()


### Функция Read

Данная функция имеет похожий функционал, единственное отличие в данной функции появляется
возможность получить выборку записок по дате с помощью команды readdate

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

