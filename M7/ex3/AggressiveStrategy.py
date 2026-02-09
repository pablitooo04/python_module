from ex3.GameStrategy import GameStrategy

class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        """
        Aggressive strategy focuses on maximizing damage output each turn.
        It prioritizes attacking the strongest enemy target available and
        playing the most powerful card in hand to deal maximum damage.

        Args:
            hand (list): The player's current hand of cards.
            battlefield (list): The current state of the battlefield with enemy targets.
        Returns:
            dict: A summary of the actions taken during the turn, including:
                - "cards_played": List of card names played.
                - "mana_used": Total mana spent.
                - "targets_attacked": List of target names attacked.
                - "damage_dealt": Total damage dealt to enemy targets.
        """
        turn_infos = {
            "cards_played": [],
            "mana_used": 0,
            "targets_attacked": [],
            "damage_dealt": 0
        }
        if not hand:
            return turn_infos
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
            turn_infos["cards_played"].append(hand[0].name)
        if not prio_list[0] in turn_infos["targets_attacked"]:
            turn_infos["targets_attacked"].append(prio_list[0].name)
        if prio_list[0].health <= 0:
            battlefield.remove(prio_list[0])

        return turn_infos

    def get_strategy_name(self) -> str:
        """Returns the name of the strategy for reporting purposes."""
        return "Aggressive Strategy"

    def prioritize_targets(self, available_targets: list) -> list:
        """Prioritizes targets based on their cost, 
        with higher cost targets being more valuable to attack first."""
        return sorted(available_targets, key=lambda x: x.cost, reverse=True)