from functools import wraps
from time import time

def spell_timer(func: callable) -> callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> None:
        print("Casting", func.__name__)
        time_before = time()
        result = func(*args, **kwargs)
        print("Spell completed in", time() - time_before)

    return wrapper


@spell_timer
def power_validator(min_power: int) -> callable:
    print("test1")

def retry_spell(max_attempts: int) -> callable:
    ...
class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        ...

    def cast_spell(self, spell_name: str, power: int) -> str:
        ...

power_validator(2)