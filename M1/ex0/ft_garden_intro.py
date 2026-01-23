def ft_garden_intro():
    """
    This function prints a welcome message for the garden.
    """
    print("=== Welcome to My Garden ===")
    print(f"Plant: {name}")
    print(f"Height: {height}cm")
    print(f"Age: {age} days")
    print("\n=== End of Program ===")


if __name__ == "__main__":
    name = "Rose"
    height = 25
    age = 30

    ft_garden_intro()
