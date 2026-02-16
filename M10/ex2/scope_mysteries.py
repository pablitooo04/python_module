def mage_counter() -> callable:
    """Creates a mage counter that keeps track of
    the number of mages created. """
    mage_count = 0

    def count_mage() -> int:
        nonlocal mage_count
        mage_count += 1
        return mage_count

    return count_mage


def spell_accumulator(initial_power: int) -> callable:
    """Creates a spell accumulator that keeps track of
    the total power of spells cast. """
    spell_count = initial_power

    def count_spell(n) -> int:
        nonlocal spell_count
        spell_count += n
        return spell_count

    return count_spell


def enchantment_factory(enchantment_type: str) -> callable:
    """Creates a factory function that applies a specific
    enchantment to items. """
    def apply_enchantment(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return apply_enchantment


def memory_vault() -> dict[str, callable]:
    """Creates a simple memory vault that can store and
    recall values. """
    memory = {}

    def store(key, value):
        memory[key] = value

    def recall(key):
        return memory.get(key, "Memory not found")

    return {
        "store": store,
        "recall": recall
    }


def main() -> None:
    """Test the mage counter, spell accumulator,
    and enchantment factory functions. """
    print("\nTesting mage counter...")

    mage = mage_counter()
    print("".join(f"Call {x + 1}: {mage()}\n" for x in range(3)))

    print("Testing enchantment factory...")
    flaming_factory = enchantment_factory("Flaming")
    frozen_factory = enchantment_factory("Frozen")
    print(flaming_factory("Sword"))
    print(frozen_factory("Shield"))


if __name__ == "__main__":
    main()
