from dataclasses import dataclass
from typing import List, Tuple

@dataclass
class Deck_winrate:
    name: str
    cards: List[Tuple[int, str]]  # Corrected to (quantity, card_name)
    wins: int = 0
    losses: int = 0
    player_score: int = 0

    @property
    def total_games(self) -> int:
        """Returns total games played."""
        return self.wins + self.losses

    @property
    def win_rate(self) -> float:
        """Calculates win rate as a percentage (0.0 to 100.0%)."""
        if self.total_games == 0:
            return 0.0
        return round((self.wins / self.total_games) * 100, 2)

    @property
    def card_count(self) -> int:
        """Calculates total card count taking quantities into account."""
        return sum(quantity for quantity, _ in self.cards)

    def record_game(self, result: str, pts: float = 0.0):
        """Helper method to update stats quickly ('W' or 'L')."""
        if result.upper() == 'W':
            self.wins += 1
            self.player_score += int(pts)  # Fixed attribute name from points -> player_score
        elif result.upper() == 'L':
            self.losses += 1

    def to_dict(self) -> dict:
        """Exports deck summary to a dictionary."""
        return {
            "Name": self.name,
            "Total Cards": self.card_count,
            "Wins": self.wins,
            "Losses": self.losses,
            "Win Rate": f"{self.win_rate}%",
            "Player Score": self.player_score
        }