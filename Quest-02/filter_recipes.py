def filter_recipes(recipes: list[dict], max_persons: int) -> list[str]:
    return [recipe['title'] for recipe in recipes if recipe['persons']<max_persons]
    
