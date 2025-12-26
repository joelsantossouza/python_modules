from abc import ABC, abstractmethod


class CardFactory(ABC):
    """Abstract Base Class for card's factory interfaces"""

    @abstractmethod
    def create_creature(self, name_or_power) -> Card:
        ...

    @abstractmethod
    def create_spell(self, name_or_power) -> Card:
        ...

    @abstractmethod
    def create_artifact(self, name_or_power) -> Card:
        ...

    @abstractmethod
    def create_themed_deck(self, size: int) -> dict:
        ...

    @abstractmethod
    def get_supported_types(self) -> dict:
        ...
