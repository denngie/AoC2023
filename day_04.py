"""Day 4: Scratchcards"""
from aocd.models import Puzzle  # type: ignore


class Scratchcard:
    """Colorful cards"""

    def __init__(self, input_data: str) -> None:
        self.input_data = list(input_data.split("\n"))
        self.cards: list[tuple[set, set]] = []

    def parse_input(self) -> None:
        """Parse input data to list of sets"""
        for card in self.input_data:
            data = card.split(":")
            winning_data, numbers_data = data[1].split("|", 1)
            winning_numbers = set(winning_data.split())
            lottery_numbers = set(numbers_data.split())
            self.cards.append((winning_numbers, lottery_numbers))

    def count_points(self) -> None:
        """Count point from each card"""
        points = 0
        for card in self.cards:
            matches = len(card[0].intersection(card[1]))
            if matches:
                points += pow(2, matches - 1)
        print(points)

    def count_cards(self) -> None:
        """Count total amount of cards"""
        stacked_cards = [[x] for x in self.cards]
        for i, card_stack in enumerate(stacked_cards):
            for card in card_stack:
                matches = len(card[0].intersection(card[1]))
                if matches:
                    for n in range(1, matches + 1):
                        stacked_cards[i + n].append(stacked_cards[i + n][0])
        print(sum(len(x) for x in stacked_cards))


def main() -> None:
    """Solve the puzzle."""
    puzzle = Puzzle(day=4, year=2023)
    scratchcard = Scratchcard(puzzle.input_data)
    scratchcard.parse_input()
    scratchcard.count_points()
    scratchcard.count_cards()


if __name__ == "__main__":
    main()
