if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")

    alice = {"first_kill", "level_10", "treasure_hunter", "speed_demon"}
    bob = {"first_kill", "level_10", "boss_slayer", "collector"}
    charlie = {"level_10", "treasure_hunter",
               "boss_slayer", "speed_demon", "perfectionist"}
    players = [alice, bob, charlie]

    print(f"Player Alice achievements: {alice}")
    print(f"Player Bob achievements: {bob}")
    print(f"Player Charlie achievements: {charlie}")

    print("\n=== Achievement Analytics ===")

    all_achievements = alice | bob | charlie
    print(f"All unique achievements: {all_achievements}")
    print(f"Total unique achievement : {len(all_achievements)}")

    print(f"Common to all players: {alice & bob & charlie}")

    rare_achievements = {ach for ach in all_achievements if sum(
        ach in p for p in players) == 1}
    print(f"Rare achievements (1 player): {rare_achievements}")
    print(f"Alice vs Bob common: {alice & bob}")
