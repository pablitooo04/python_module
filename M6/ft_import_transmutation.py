def main() -> None:
    print("=== Import Transmutation Mastery ===")

    print()

    print("Method 1 - Full module import")
    try:
        import alchemy
    except ImportError:
        print("Failed to import alchemy.elements module.")
    else:
        print(f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}")
    
    print()
    
    print("Method 2 - Specific function import:")
    try:
        from alchemy.elements import create_water
    except ImportError:
        print("Failed to import create_water from alchemy.elements")
    else:
        print(f"create_water(): {create_water()}")

    print()

    print("Method 3 - Aliased import:")
    try:
        from alchemy.potions import healing_potion as heal
    except ImportError:
        print("Failed to import healing_potion from alchemy.potions")
    else:
        print(f"heal(): {heal()}")
    
    print()
    
    print("Method 4 - Multiple imports:")

    try:
        from alchemy.elements import create_earth, create_fire
        from alchemy.potions import strength_potion
    except ImportError:
        print("Failed to import from alchemy package")
    else:
        print(f"create_earth(): {create_earth()}")
        print(f"create_fire(): {create_fire()}")
        print(f"strength_potion(): {strength_potion()}")

    print()

    print("All import transmutation methods mastered!")

if __name__ == "__main__":
    main()
