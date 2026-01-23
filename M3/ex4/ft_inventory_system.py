from sys import argv

usage = "usage: python3 ft_inventory_system.py <item:value> <item:value> ..."


def parse_args(argv: list) -> dict:
    """
    Parse command line arguments into a dictionary.
    Args:
        argv (list): List of command line arguments.
    Returns:
        dict: Dictionary with item names as keys and their values as integers.
    """
    argv_dict = {}
    for item in argv:
        if ":" not in item:
            raise ValueError(usage)
        else:
            parse = item.split(sep=":")
            argv_dict[parse[0]] = int(parse[1])
            if int(parse[1]) <= 0:
                raise ValueError("value must be non-nul positive number")
    return argv_dict


if __name__ == "__main__":
    if len(argv) == 1:
        print("No argument provided !")
        print(usage)
    else:
        try:
            item_dict = parse_args(argv[1:])
        except ValueError as e:
            print("Error :", e)
        else:
            print("=== Inventory System Analysis ===")
            print("Dictionnary created !")
            print("\n=== Current Inventory ===")
            total_items = sum(value for value in item_dict.values())
            value_max, value_min = float("-inf"), float("inf")
            for key, value in item_dict.items():
                print(f"{key}: {value}"
                      f"units ({round((value*100)/total_items, 1)}%)")
                if value > value_max:
                    value_max, key_max = value, key
                if value < value_min:
                    value_min, key_min = value, key

            print("\n=== Inventory Statistics ===")
            print(f"Most abundant: {key_max} ({value_max} units)")
            print(f"Least abundant: {key_min} ({value_min} units)")
            print("\n=== Item Categories ===")
            moderate = {k: v for k, v in item_dict.items() if v > 3}
            scarse = {k: v for k, v in item_dict.items() if v <= 3}
            print(f"Moderate: {moderate}")
            print(f"Scarse: {scarse}")

            print("\n=== Management Suggestions ===")
            restock = [k for k, v in item_dict.items() if v == 1]
            print(f"Restock needed : {restock}")

            moderate.update(scarse)
            new_dict = moderate
            print("\n=== Dictionary Properties Demo ===")
            print(f"Dictionary keys: {list(new_dict.keys())}")
            print(f"Dictionnary values: {list(new_dict.values())}")
            print(
                f'Sample lookup - "sword" in inventory: '
                f'{new_dict.get("sword", "NOT_FOUND") != "NOT_FOUND"}')
