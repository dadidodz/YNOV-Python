import datetime as dt

def build_menu(recipes: list[dict], start_date: dt.date) -> list[tuple[dt.date, str]]:
    listOfTuple = []
    currentDate = start_date
    
    for recipe in recipes:
        listOfTuple.append((currentDate, recipe['title']))
        currentDate+=dt.timedelta(days=1)
    
    return listOfTuple

def save_menu(meals: list[tuple[dt.date, str]]):
    with open("menu.txt", "w", encoding='utf-8') as file:
        for meal in meals:
            date, dish = meal
            formatted_date = date.strftime("%A %d %B %Y")
            menu_entry = f"{formatted_date}: {dish}\n"
            file.write(menu_entry)