try:
    import alchemy.transmutation
except ImportError:
    print("Failed to import alchemy.transmutation module.")
    exit(1)


def main() -> None:
    print("=== Pathway Debate Mastery ===\n")
    
    print("Testing Absolute Imports (from basic.py):")
    print(f"lead_to_gold(): {alchemy.transmutation.lead_to_gold()}")
    print(f"stone_to_gem(): {alchemy.transmutation.stone_to_gem()}\n")

    print("Testing Relative Imports (from advanced.py):")
    print(f"philosophers_stone(): {alchemy.transmutation.philosophers_stone()}")
    print(f"elixir_of_life(): {alchemy.transmutation.elixir_of_life()}\n")
    
    print("Testing Package Access:")
    
if __name__ == "__main__":
    main()