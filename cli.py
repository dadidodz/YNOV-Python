import argparse
import json
import datetime as dt
from sort_list import sort_recipes
from filter_recipes import filter_recipes
from menu import build_menu
from datetime_utils import parse_time
from menu import save_menu
# from datetime_utils import format_date

parser = argparse.ArgumentParser(description="Create a menu from recipes")
parser.add_argument("--start", "-s", required=True, help="Start date (format: DD/MM/YYYY)")
parser.add_argument("--max-persons", "-p", type=int, default=4, help="Maximum number of persons for recipes")
args = parser.parse_args()

with open('recipes_data.json', 'r', encoding='utf-8') as file:
    recipes = json.load(file)

sorted_recipes = sort_recipes(recipes, 'title')

filtered_recipes = filter_recipes(sorted_recipes, args.max_persons)

a = parse_time(args.start)

menu_content = build_menu(filtered_recipes, a)
#print(menu_content)

save_menu(menu_content)

print("Menu generated and saved in menu.txt")