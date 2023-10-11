import sort_list

if __name__ == '__main__':
    recipes = [{'title': 'bananes flambées', 'persons': 30}, {'title': 'avocat au thon', 'persons': 4}]
    print(sort_list.sort_recipes(recipes, by='title'))
