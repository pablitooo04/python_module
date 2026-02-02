def healing_potion() -> str:
    try:
        from .elements import create_fire, create_water
    except ImportError:
        print("Failed to import from .element package")
    else:
        result = "Healing potion brewed with "
        result += f"{create_water()} and {create_fire()}"
        return result


def strength_potion() -> str:
    try:
        from .elements import create_fire, create_earth
    except ImportError:
        print("Failed to import from .element package")
    else:
        result = "Strength potion brewed with "
        result += f"{create_earth()} and {create_fire()}"
        return result


def invisibility_potion() -> str:
    try:
        from .elements import create_air, create_water
    except ImportError:
        print("Failed to import from .element package")
    else:
        result = "Invisibility potion brewed with "
        result += f"{create_air()} and {create_water()}"
        return result


def wisdom_potion() -> str:
    try:
        from .elements import create_air, create_water, \
            create_earth, create_fire
    except ImportError:
        print("Failed to import from .element package")
    else:
        result = "Wisdom potion brewed with all elements: "
        result += f"{create_air()}, {create_water()}, "
        result += f"{create_earth()}, and {create_fire()}"
        return result
