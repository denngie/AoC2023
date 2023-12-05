"""Day 3: Gear Ratios"""
from re import finditer
from math import prod
from aocd.models import Puzzle  # type: ignore


class Engine:
    """Gondola lift engine"""

    def __init__(self) -> None:
        self.input_data: list[str] = []
        self.chars: dict[tuple, list] = {}

    def add_input(self, input_data: str) -> None:
        """Take input data and store it per line"""
        self.input_data = list(input_data.split())

    def _char_calculation(self) -> None:
        """Find valid engine parts"""
        schematic_size = len(self.input_data)
        self.chars = {
            (r, c): []
            for r in range(schematic_size)
            for c in range(schematic_size)
            if self.input_data[r][c] not in "0123456789."
        }
        for r, row in enumerate(self.input_data):
            for n in finditer(r"\d+", row):
                edge = {
                    (r, c)
                    for r in (r - 1, r, r + 1)
                    for c in range(n.start() - 1, n.end() + 1)
                }

                for o in edge & self.chars.keys():
                    self.chars[o].append(int(n.group()))

    def sum_part_numbers(self) -> None:
        """Sum of all the engine parts"""
        self._char_calculation()
        print(sum(sum(p) for p in self.chars.values()))

    def product_gears(self) -> None:
        """Product of all the gears"""
        self._char_calculation()
        print(sum(prod(p) for p in self.chars.values() if len(p) == 2))


def main() -> None:
    """Solve the puzzle."""
    puzzle = Puzzle(day=3, year=2023)
    engine = Engine()
    engine.add_input(puzzle.examples[0].input_data)
    engine.add_input(puzzle.input_data)
    engine.sum_part_numbers()
    engine.product_gears()


if __name__ == "__main__":
    main()
