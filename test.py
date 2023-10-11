from filter_recipes import filter_recipes

if __name__ == '__main__':
    recipes = [{'title': 'bananes flambées', 'persons': 30}, {'title': 'avocat au thon', 'persons': 4}]
    print(filter_recipes(recipes, 10))