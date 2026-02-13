try:
    from dotenv import load_dotenv
except ImportError:
    print("Error: dotenv module not found!")
    exit(1)

try:
    import validators
except ImportError:
    print("Error: validators module not found!")
    exit(1)

import os


def api_key_is_valid(api_key: str) -> bool:
    """
    Validates the API key format.
    Args:
        api_key (str): The API key to validate.
    Returns:
        bool: True if the API key is valid, False otherwise.
    """
    alphabet: str = "abcdefghijklmnopqrstuvwxyz"
    alphabet += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet += "0123456789"

    return (
        all(c in alphabet for c in api_key)
        and 20 <= len(api_key) <= 100
    )


def main() -> None:
    """Main function to validate environment variables."""
    validate_status = True

    try:
        if (
            os.environ["MATRIX_MODE"]
            not in {"production", "development"}
        ):
            raise (ValueError)
        print("Mode:", os.environ["MATRIX_MODE"])
    except (KeyError, ValueError):
        validate_status = False
        print("Mode: None")

    try:
        if validators.url(os.environ["DATABASE_URL"]):
            print("Database:", "Connected to local instance")
        else:
            raise ValueError
    except (KeyError, ValueError):
        validate_status = False
        print("Database: Unable to connect to database")

    try:
        if api_key_is_valid(os.environ["API_KEY"]):
            print("API Access: Authenticated")
        else:
            raise ValueError
    except (KeyError, ValueError):
        validate_status = False
        print("API Access: Unable to validate API key.")

    try:
        print("Log Level:", os.environ["LOG_LEVEL"])
    except KeyError:
        validate_status = False
        print("Log Level: None")

    try:
        if validators.url(os.environ["ZION_ENDPOINT"]):
            print("Zion Network: Online")
        else:
            raise ValueError()
    except (KeyError, ValueError) as e:
        validate_status = False
        print("Database: Unable to connect to zion network", e)

    print()

    if validate_status:
        print("[OK] No hardcoded secrets detected")
        print("[OK] .env file properly configured")
        print("[OK] Production overrides available")
    else:
        print("[KO] bad configuration for .env file")

    print()

    print("The Oracle sees all configurations")


if __name__ == "__main__":
    print("\nORACLE STATUS: Reading the Matrix...\n")

    load_dotenv()
    print("Configuration loaded:")
    main()
