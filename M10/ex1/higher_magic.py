def spell_combiner(spell1: callable, spell2: callable) -> callable:
    return lambda x: (spell1(x), spell2(x))


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    return lambda x: base_spell(x) * multiplier


def conditional_caster(condition: callable, spell: callable) -> callable:
    return lambda x: spell(x) if condition(x) else "Spell fizzled"


def spell_sequence(spells: list[callable]) -> callable:
    return lambda x: [spell(x) for spell in spells]


def main() -> None:
    print("\nTesting spell combiner..")

    def fireball(x):
        return "Fireball hits " + x

    def heal(x):
        return "Heals " + x

    combined_functions = spell_combiner(fireball, heal)
    res1, res2 = combined_functions("Dragon")

    print("Combined spell result:", res1, res2)

    print()

    print("Testing power amplifier...")

    sum_amplified = power_amplifier(sum, 3)

    print(
        f"Original: {sum([1, 2, 3, 4])}"
        f"Amplified: {sum_amplified([1, 2, 3, 4])}"
    )


if __name__ == "__main__":
    main()
