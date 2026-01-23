def garden_operations() -> None:
    """
    Perform garden operations that may raise different error types.
    """
    value = "abc"
    div = 0
    file = "missing.txt"
    key = "plant"
    test_error_types(value, div, file, key)


def test_error_types(value: str, div: int, file: str, key: str) -> None:
    """
    Test various error types in garden operations.
    Args:
        value (str): A string to convert to int.
        div (int): A divisor for division operation.
        file (str): A filename to open.
        key (str): A key to access in a dictionary.
    """
    print("=== Garden Error Types Demo ===\n")
    try:
        print("Testing ValueError...")
        value = int(value)
    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")
    try:
        print("Testing ZeroDivisionError..")
        if 1 / div:
            pass
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")
    try:
        print("Testing FileNotFoundError...")
        open(file)
    except FileNotFoundError:
        print(f"Caught FileNotFoundError: No such file '{file}'\n")
    try:
        print("Testing KeyError...")
        print({}[key])
    except KeyError as e:
        print("Caught KeyError", e, end="\n\n")

    print("Testing multiple errors together...")
    try:
        value = int(value)
        1 / div
        file = open(file, 'r')
        file.close()
        print({}[key])
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!\n")

    print("All error types tested successfully!")


if __name__ == "__main__":
    garden_operations()
