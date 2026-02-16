def check_temperature(temp_str: str) -> int | None:
    """
    Try to convert a string into a valid temperature.

    Args:
        temp_str (str): A string representing a temperature.

    Returns:
        int | None: The temperature if it is valid, otherwise None.
    """
    try:
        temperature = int(temp_str)
        if temperature < 0:
            print(f"Error: {temp_str}°C is too low.")
        elif temperature > 40:
            print(f"Error: {temp_str}°C is too high.")
        else:
            print(f"{temp_str}°C is perfect.")
            return temperature
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number.")

    return None


def test_temperature_input() -> None:
    """
    Test the check_temperature function with several example inputs.
    """
    print("=== Garden Temperature Checker ===")

    print("\nTesting temperature: 25")
    check_temperature("25")

    print("\nTesting temperature: abc")
    check_temperature("abc")

    print("\nTesting temperature: 100")
    check_temperature("100")

    print("\nTesting temperature: -50")
    check_temperature("-50")


if __name__ == "__main__":
    test_temperature_input()
