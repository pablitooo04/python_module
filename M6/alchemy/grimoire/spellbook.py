from .validator import validate_ingredients


def record_spell(spell_name: str, ingredients: str) -> str:
    string_end = f"{spell_name} ({validate_ingredients(ingredients)})"
    if validate_ingredients(ingredients).split(sep=" ")[-1] == "VALID":
        return "Spell recorded: " + string_end
    else:
        return "Spell rejected: " + string_end
