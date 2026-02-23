from functools import reduce, partial, lru_cache, singledispatch


def spell_reducer(spells: list[int], operation: str) -> int:
    if operation == "add":
        return reduce(lambda x, y: x + y, spells)
    elif operation == "multiply":
        return reduce(lambda x, y: x * y, spells)
    elif operation == "max":
        return reduce(lambda x, y: max(x, y), spells)
    elif operation == "min":
        return reduce(lambda x, y: min(x, y), spells)
    else:
        raise ValueError(f"Error: {operation} is not a valid operation!")


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    fire = partial(base_enchantment, 50, "Fire")
    ice = partial(base_enchantment, 50, "Ice")
    lightning = partial(base_enchantment, 50, "Lightning")

    return {
        "fire_enchant": fire,
        "ice_enchant": ice,
        "lightning_enchant": lightning
    }


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("Error: n must be a positive int!")
    if n == 0 or n == 1:
        return n
    else:
        return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> callable:

    @singledispatch
    def cast(spell):
        return "Unknow type"

    @cast.register
    def _(x: int):
        return f"Damage deal:, {x}"

    @cast.register
    def _(x: str):
        return f"Enchantment:, {x}"

    @cast.register
    def _(x: list):
        return f"Multi-cast result: {[cast(z) for z in x]}"

    return cast


def main():
    try:
        print("\nTesting spell reducer...")
        print("Sum:", spell_reducer([10 for _ in range(10)], "add"))
        print("Product:", spell_reducer([10, 10, 10, 10, 24], "multiply"))
        print("Max:", spell_reducer([0, 10, 20, 30, 40], "max"))
    except ValueError as e:
        print(e)

    print()

    print("Testing memoized fibonacci...")
    try:
        print("Fib(10)", memoized_fibonacci(10))
        print("Fib(15)", memoized_fibonacci(15))
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
