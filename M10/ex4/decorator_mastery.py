from functools import wraps
import time


def fireball() -> str:
    time.sleep(0.1)
    return "Fireball cast!"


def power_validator(min_power: int) -> callable:
    def decorator_factory(func: callable) -> callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> str:
            power = kwargs["power"] if "power" in kwargs else args[2]
            if power < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)
        return wrapper
    return decorator_factory


def retry_spell(max_attempts: int) -> callable:
    def decorator(func: callable) -> callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(
                        "Spell failed, retrying..."
                        f"(attempt {i+1}/{max_attempts})"
                    )
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


def spell_timer(func: callable) -> callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> None:
        print(f"Casting {func.__name__}...")
        start = time.time()
        res = func(*args, **kwargs)
        print(f"Spell completed in {round(time.time() - start, 3)} seconds")
        return res
    return wrapper


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(
            c.isalpha() or c == " " for c in name
        )

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:
    print("Testing spell timer...")
    timed_fireball = spell_timer(fireball)
    print("Result:", timed_fireball())
    print()

    print("Testing MageGuild...")
    guild = MageGuild()

    print(guild.validate_mage_name("Gandalf"))
    print(guild.validate_mage_name("X1"))

    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Lightning", 5))


if __name__ == "__main__":
    main()
