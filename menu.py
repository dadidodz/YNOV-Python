import datetime as dt

def build_menu(recipes: list[dict], start_date: dt.date) -> list[tuple[dt.date, str]]:
    listOfTuple = []
    currentDate = start_date
    
    for recipe in recipes:
        listOfTuple.append((currentDate, recipe['title']))
        currentDate+=dt.timedelta(days=1)
    
    return listOfTuple