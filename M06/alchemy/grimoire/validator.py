def validate_ingredients(ingredients: str) -> str:
    elt = {"fire", "water", "earth", "air"}
    ingredients_list = ingredients.split(sep=" ")
    if all(i in elt for i in ingredients_list) and ingredients_list:
        return f"{ingredients} - VALID"
    else:
        return f"{ingredients} - INVALID"
