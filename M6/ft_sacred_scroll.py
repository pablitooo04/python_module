try:
    import alchemy.elements as elt
except ImportError:
    print("Failed to import alchemy.elements module.")
    exit(1)

try:
    import alchemy as al
except ImportError:
    print("Failed to import alchemy package.")
    exit(1)

def main() -> None:
    print("=== Sacred Scroll Mastery ===\n")

    print("Testing direct module access:")
    print(f"alchemy.elements.create_fire(): {elt.create_fire()}")
    print(f"alchemy.elements.create_water(): {elt.create_water()}")
    print(f"alchemy.elements.create_earth(): {elt.create_earth()}")
    print(f"alchemy.elements.create_air(): {elt.create_air()}\n")

    print("Testing package-level access (controlled by __init__.py):")
    try:
        print(f"alchemy.create_fire(): {al.create_fire()}")
    except AttributeError:
        print("alchemy.create_fire(): AttributeError - not exposed")
    try:
        print(f"alchemy.create_water(): {al.create_water()}")
    except AttributeError:
        print("alchemy.create_water(): AttributeError - not exposed")
    try:
        print(f"alchemy.create_earth(): {al.create_earth()}")
    except AttributeError:
        print("alchemy.create_earth(): AttributeError - not exposed")
    try:
        print(f"alchemy.create_air(): {al.create_air()}")
    except AttributeError:
        print("alchemy.create_air(): AttributeError - not exposed")

    print()

    print("Package metadata:")
    try:
        print(f"Version {al.__version__}")
    except AttributeError:
        print("Version: AttributeError - not exposed")
    try:
        print(f"Author: {al.__author__}")
    except AttributeError:
        print("Author: AttributeError - not exposed")

if __name__ == "__main__":
    main()