from ex3.GameStrategy import GameStrategy

class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        turn_infos = {
            "cards_played": [],
            "mana_used": 0,
            "targets_attacked": [],
            "damage_dealt": 0
        }

        if not battlefield:
            return turn_infos
        prio_list = self.prioritize_targets(battlefield)
        if hand[0].type == "creature":
            prio_list[0].health -= hand[0].attack
            turn_infos["damage_dealt"] += hand[0].attack
        elif hand[0].type == "spell":
            prio_list[0].health -= 20
            turn_infos["damage_dealt"] += 20
            turn_infos["mana_used"] += hand[0].cost
        else:
            turn_infos["damage_dealt"] += 5
            prio_list[0].health -= 5
        if not hand[0] in turn_infos["cards_played"]:
            turn_infos["cards_played"].append(hand[0])
        if not prio_list[0] in turn_infos["targets_attacked"]:
            turn_infos["targets_attacked"].append(prio_list[0])
        if prio_list[0].health <= 0:
            battlefield.remove(prio_list[0])

        return turn_infos

    def get_strategy_name(self) -> str:
        return "Agressive Strategy"

    def prioritize_targets(self, available_targets: list) -> list:
        return sorted(available_targets, key=lambda x: x.cost)