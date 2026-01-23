def ft_count_harvest_recursive():
    first_day = int(input("Days until harvest: "))

    def recursive(days):
        if days == 0:
            print("Harvest time!")
        else:
            print(f"Day {first_day - days + 1}")
            recursive(days - 1)
    recursive(first_day)
