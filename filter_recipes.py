def filter_recipes(recipes: list[dict], max_persons: int) -> list[str]:
    newlist = [recipe['title'] for recipe in recipes if recipe['persons']<max_persons]
    return newlist
    
