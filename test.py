import datetime as dt
import menu

if __name__ == '__main__':
    recipes = [
        {'title': 'bananes flambées', 'persons': 30}, 
        {'title': 'avocat au thon', 'persons': 4},
    ]
    print(menu.build_menu(recipes, dt.date(2022, 6, 1)))