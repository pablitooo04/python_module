try:
    import alchemy.grimoire as grm
except ImportError:
    print("Failed to import alchemy.grimoire module.")
    exit(1)


def main() -> None:
    print("=== Circular Curse Breaking ===\n")

    print("Testing ingredient validation:")
    print('validate_ingredients("fire air") ', end="")
    print(f'{grm.validate_ingredients("fire air")}')
    print('validate_ingredients("dragon scale")', end="")
    print(f'"{grm.validate_ingredients("dragon scale")}')

    print()

    print("Testing spell recording with validation:")
    print('record_spell("Fireball", "fire air"): ', end="")
    print(f'{grm.record_spell("Fireball", "fire air")}')
    print('record_spell("Dark Magic", "shadow"): ', end="")
    print(f'{grm.record_spell("Dark Magic", "shadow")}')

    print()

    print("Testing late import technique:")
    print("record_spell('Lightning', 'air'): ", end="")
    print(f"{grm.record_spell('Lightning', 'air')}")

    print("Circular dependency curse avoided using late imports!")
    print("All spells processed safely.")


if __name__ == "__main__":
    main()
