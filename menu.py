import datetime as dt

def build_menu(recipes: list[dict], start_date: dt.date) -> list[tuple[dt.date, str]]:
    listOfTuple = []
    currentDate = start_date
    
    for recipe in recipes:
        listOfTuple.append((currentDate, recipe['title']))
        currentDate+=dt.timedelta(days=1)
    
    return listOfTuple

def save_menu(meals: list[tuple[dt.date, str]]):
    file = open("menu.txt", "w", encoding='utf-8')
    for i in meals:
        file.write(str(i))