def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: "* " + x + " *", spells))


def mage_stats(mages: list[dict]) -> dict:
    dico = {
        'max_power': max(mages, key=lambda x: x["power"]),
        'min_power': min(mages, key=lambda x: x["power"]),
    }
    if mages:
        return dico.update(
            {'avg_power': sum(mages, key=lambda x: x["power"])/len(mages)}
        )
    return dico


def main() -> None:
    """Test the artifact sorter and spell transformer
    functions with sample data."""
    artifacts = [
        {'name': 'Fire Staff', 'power': 92, 'type': 'focus'},
        {'name': 'Crystal Orb', 'power': 85, 'type': 'focus'}
    ]
    spells_tests = ["fireball", "heal", "shield"]

    print("Testing artifact sorter...")
    artifacts = artifact_sorter(artifacts)
    if len(artifacts) >= 1:
        name, power = artifacts[0].get(
            'name', None), artifacts[0].get('power', None)
        print(f"{name} ({power}) ", end="")

    if len(artifacts) >= 2:
        for artifact in artifacts[1:]:
            name, power = artifact.get(
                'name', None), artifact.get('power', None)
            print(f"comes before {name} ({power}) ", end="")

    if len(artifacts) >= 1:
        print()

    print("Testing spell transformer...")
    if len(spells_tests) >= 1:
        print("".join(c + " " for c in spell_transformer(spells_tests)))


if __name__ == "__main__":
    main()
