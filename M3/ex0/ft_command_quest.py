from sys import argv

if __name__ == "__main__":
    print("=== Command Quest ===")
    print(f"Program name: {argv[0]}")
    if len(argv) == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {len(argv) - 1}")
    for i in range(1, len(argv)):
        print(f"Argument {i}: {argv[i]}")
    print(f"Total arguments: {len(argv)}")
