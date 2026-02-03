try:
    from alchemy.elements import create_fire, create_earth
except ImportError:
    print("Failed to import from alchemy.elements package")
    exit(1)


def lead_to_gold() -> str:
    return f"Lead transmuted to gold using {create_fire()}"


def stone_to_gem() -> str:
    return f"Stone transmuted to gem using {create_earth()}"
