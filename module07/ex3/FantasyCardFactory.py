from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex3.CardFactory import CardFactory
from random import choice


class FantasyCardFactory(CardFactory):
    """Factory specialized to create creatures, spells and artifacts"""

    def create_creature(self, name_or_power) -> Card:
        if isinstance(name_or_power, str):
            return CreatureCard(name_or_power, 3, "Legendary", 3, 5)
        elif isinstance(name_or_power, int):
            return CreatureCard(
                "Creature", 3, "Legendary", name_or_power, name_or_power + 3
            )
        return None

    def create_spell(self, name_or_power) -> Card:
        if isinstance(name_or_power, str):
            return SpellCard(name_or_power, 2, "Legendary", "damage")
        elif isinstance(name_or_power, int):
            return SpellCard("Spell", name_or_power, "Legendary", "damage")
        return None

    def create_artifact(self, name_or_power) -> Card:
        if isinstance(name_or_power, str):
            return ArtifactCard(
                name_or_power, 2, "Legendary", 3, "+1 mana per turn"
            )
        elif isinstance(name_or_power, int):
            return ArtifactCard(
                "Artifact", 2, "Legendary", name_or_power, "+1 mana per turn"
            )
        return None

    def create_themed_deck(self, size: int) -> dict:
        deck: list[str] = []
        types: dict = self.get_supported_types()
        keys: list[str] = list(types.keys())
        for _ in range(size):
            card_type: str = choice(keys)
            card_name: str = choice(types[card_type])
            deck.append(card_name)
        return {
            "deck": deck
        }

    def get_supported_types(self) -> dict:
        return {
            "creatures": ["Fire Dragon", "Goblin Warrior"],
            "spells": ["Fireball", "Lightning Bolt"],
            "artifacts": ["Mana Ring"],
        }
