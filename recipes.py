def create_recipe(nameb, personsb, ingredientsb):
    recipe = {
        'title': nameb, 
        'persons': personsb, 
        'ingredients': ingredientsb,
    }
    if len(recipe['ingredients'])>149:
        raise ValueError("Title is too long")
    if recipe['persons']==False or recipe['persons']>50:
        raise ValueError("Invalid persons number")
    if not len(recipe['ingredients']):
        raise ValueError("This recipe has no ingredients")
    return recipe