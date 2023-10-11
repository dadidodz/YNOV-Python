def create_recipe(nameb, personsb, ingredientsb):
    recipe = {
        'title': nameb, 
        'persons': personsb, 
        'ingredients': ingredientsb,
    }
    if len(recipe['title'])>150:
        raise ValueError("Title is too long")
    if recipe['persons']==False or recipe['persons']>50:
        raise ValueError("Invalid persons number")
    if not len(recipe['ingredients']):
        raise ValueError("This recipe has no ingredients")
    return recipe

def create_recipe_v2(title, persons, *ingredients, **tags):
    if len(title) > 40:
        raise ValueError("Title is too long")
    if persons <= 0 or persons > 20:
        raise ValueError("Invalid persons number")
    if not ingredients:
        raise ValueError("Ingredient list cannot be empty")

    return {
        'title': title,
        'persons': persons,
        'ingredients': ingredients,
        'tags': tags
    }
    