try:
    import alchemy.transmutation
except ImportError:
    print("Failed to import alchemy.transmutation module.")
    exit(1)


def main() -> None:
    print("=== Pathway Debate Mastery ===\n")

    print("Testing Absolute Imports (from basic.py):")
    try:
        from alchemy.transmutation.basic import lead_to_gold, stone_to_gem
    except ImportError:
        print("Failed to import from alchemy.transmutation.basic module.")
    else:
        print(f"lead_to_gold(): {lead_to_gold()}")
        print(f"stone_to_gem(): {stone_to_gem()}\n")

    try:
        from alchemy import philosophers_stone, elixir_of_life
    except ImportError:
        print("Failed to import from alchemy module.")
    else:
        print("Testing Alchemy Module Access:")
        print(f"philosophers_stone(): {philosophers_stone()}")
        print(f"elixir_of_life(): {elixir_of_life()}\n")

    print("Testing Package Access:")
    print("alchemy.transmutation.lead_to_gold(): ", end="")
    print(f"{alchemy.transmutation.lead_to_gold()}")
    print("alchemy.transmutation.philosophers_stone(): ", end="")
    print(f"{alchemy.transmutation.philosophers_stone()}\n")

    print("Both pathways work! Absolute: clear, Relative: concise.")


if __name__ == "__main__":
    main()
