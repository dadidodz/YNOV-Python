import json

def get_recipes(file_name):
    file = open(file_name, "r", encoding="utf-8")
    data = json.load(file)
    return data