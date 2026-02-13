import sys
import site

env_help = """\
To enter the construct, run:
python -m venv matrix_env
source matrix_env/bin/activate # On Unix
matrix_env
Scripts
activate # On Windows
"""

success_msg = """\
SUCCESS: You're in an isolated environment!
Safe to install packages without affecting
the global system.
"""


def in_virtualenv() -> bool:
    """
    Returns:
        bool: True if the current Python interpreter is running
        inside a virtual environment, False otherwise.
    """
    return sys.prefix != sys.base_prefix


def main() -> None:
    """Main function."""

    if not in_virtualenv():
        print("\nMATRIX STATUS: You're still plugged in\n")

        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected\n")

        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")

        print(env_help)

        print("Then run this program again.")
    else:
        print("\nMATRIX STATUS: Welcome to the construct\n")

        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {sys.prefix.split(sep='/')[-1]}")
        print(f"Environment Path: {sys.prefix}\n")

        print(success_msg)

        print("Package installation path:")
        print(site.getsitepackages()[0])
        # construct.py


if __name__ == "__main__":
    main()
