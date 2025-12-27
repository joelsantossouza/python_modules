from ex4.TournamentCard import TournamentCard
from random import shuffle


class TournamentPlatform:
    """Interface to manage tournaments"""

    def __init__(self) -> None:
        self.matches_played: int = 0
        self.cards: dict = {}

    def register_card(self, card: TournamentCard) -> str:
        if not isinstance(card, TournamentCard):
            return None
        self.cards[card._info["id"]] = card
        return card._info["id"]

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        if not isinstance(card1_id, str) or not isinstance(card2_id, str) or \
                card1_id == card2_id:
            return None
        self.matches_played += 1
        players: list[TournamentCard] = [card1_id, card2_id]
        shuffle(players)
        winner: TournamentCard = players[0]
        loser: TournamentCard = players[1]
        self.cards[winner].update_wins(1)
        self.cards[loser].update_losses(1)
        winner_rating: int = self.cards[winner].get_rank_info()["rating"]
        loser_rating: int = self.cards[loser].get_rank_info()["rating"]
        return {
            "winner": winner,
            "loser": loser,
            "winner_rating": winner_rating,
            "loser_rating": loser_rating
        }

    def get_leaderboard(self) -> list:
        cards: list[TournamentCard] = [
            self.cards[id] for id in self.cards.keys()
        ]
        return sorted(
            cards, key=lambda card: card._TournamentCard__rating,
            reverse=True
        )

    def generate_tournament_report(self) -> dict:
        cards: list[TournamentCard] = [
            self.cards[id] for id in self.cards.keys()
        ]
        total_cards: int = 0
        avg_rating: float = 0
        for card in cards:
            total_cards += 1
            avg_rating += card._TournamentCard__rating
        if total_cards > 0:
            avg_rating /= total_cards
        return {
            "total_cards": total_cards,
            "matches_played": self.matches_played,
            "avg_rating": avg_rating,
            "plataform_status": "active"
        }
