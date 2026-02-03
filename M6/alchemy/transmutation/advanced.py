try:
    from .basic import lead_to_gold
    from ..potions import healing_potion
except ImportError:
    print("Failed to import from alchemy package")
    exit(1)


def philosophers_stone() -> str:
    result = "Philosopher\'s stone created using"
    result += f"{lead_to_gold()} and {healing_potion()}"
    return result


def elixir_of_life() -> str:
    return "Elixir of life: eternal youth achieved!"
