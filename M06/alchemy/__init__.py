try:
    from .elements import create_fire, create_water  # noqa: F401
except ImportError:
    print("Failed to import from alchemy.elements package")
    exit(1)

__version__ = "1.0.0"
__author__ = "Master Pythonicus"
