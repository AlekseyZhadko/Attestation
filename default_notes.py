import json
import os

def default_notes():
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
