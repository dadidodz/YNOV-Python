import argparse
import json
from sort_list import sort_recipes
from filter_recipes import filter_recipes
from menu import build_menu
from datetime_utils import parse_time
from menu import save_menu

parser = argparse.ArgumentParser(description="Create a menu from recipes")
parser.add_argument("--start", "-s", required=True, help="Start date (format: DD/MM/YYYY)")
parser.add_argument("--max-persons", "-p", type=int, default=4, help="Maximum number of persons for recipes")
args = parser.parse_args()

with open('recipes_data.json', 'r', encoding='utf-8') as file:
    recipes = json.load(file)

sorted_recipes = sort_recipes(recipes, 'title')

filtered_recipes = filter_recipes(sorted_recipes, args.max_persons)

format_date = parse_time(args.start)

menu_content = build_menu(filtered_recipes, format_date)

save_menu(menu_content)

print("Menu generated and saved in menu.txt")