import datetime as dt
from menu import save_menu

if __name__ == '__main__':
    recipes = [
        (dt.date(2022, 6, 1), 'bananes flambées'), 
        (dt.date(2022, 6, 2), 'avocat au thon'),
    ]
    save_menu(recipes)