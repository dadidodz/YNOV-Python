import json

def get_recipes(file_name):
    file = open("recipes_data.json", "r", encoding="utf-8")
    data = json.load(file)
    return data