"""Day 1: Trebuchet?!"""
from aocd.models import Puzzle  # type: ignore


class Trebuchet:
    """Sky launching machine"""

    def __init__(self) -> None:
        self.input_data: list[str] = []

    def add_input(self, input_data: str) -> None:
        """Take input data and store it per line"""
        self.input_data = list(input_data.split())

    def read_calibration_values(self) -> None:
        """Extract calibration values as digits"""
        values: list[int] = []
        for line in self.input_data:
            digits = [i for i in line if i.isdigit()]
            value = digits[0] + digits[-1]
            values.append(int(value))

        print(sum(values))

    def read_calibration_values_with_letters(self) -> None:
        """Extract calibration values with some of the digits spelled out as letters"""
        values: list[int] = []
        digit_dict = {
            "one": "o1e",
            "two": "t2o",
            "three": "t3e",
            "four": "f4r",
            "five": "f5e",
            "six": "s6x",
            "seven": "s7n",
            "eight": "e8t",
            "nine": "n9e",
        }
        for line in self.input_data:
            for k, v in digit_dict.items():
                line = line.replace(k, v)

            digits = [i for i in line if i.isdigit()]
            value = digits[0] + digits[-1]
            values.append(int(value))

        print(sum(values))


def main() -> None:
    """Solve the puzzle."""
    puzzle = Puzzle(day=1, year=2023)
    trebuchet = Trebuchet()
    trebuchet.add_input(puzzle.input_data)
    trebuchet.read_calibration_values()
    trebuchet.read_calibration_values_with_letters()


if __name__ == "__main__":
    main()
