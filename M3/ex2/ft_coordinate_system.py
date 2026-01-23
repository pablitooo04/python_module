from sys import argv
from math import sqrt

if __name__ == "__main__":
    if len(argv) == 1:
        print("No argument provided. Usage: ", end="")
        print("python3 ft_coordinate_system.py <x,y,z>")
    else:
        pos = tuple(argv[1].split(sep=','))
        if (len(pos) != 3):
            print("Error: Please provide exactly one argument ", end="")
            print("which contain three coordinates in the format <x,y,z>")
        else:
            try:
                int_pos = tuple(int(_) for _ in pos)
            except Exception as e:
                print("Error: ", e)
            else:
                print(f"Position created: {int_pos}")
                x1, y1, z1 = int_pos
                x2, y2, z2 = (0, 0, 0)
                result = round(sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2), 2)
                print(f"Distance between (0, 0, 0) and {int_pos}: {result}")
