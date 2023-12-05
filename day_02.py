"""Day 2: Cube Conundrum"""
from aocd.models import Puzzle  # type: ignore


class GameCube:
    """Sky launching machine"""

    def __init__(self) -> None:
        self.input_data: list[str] = []

    def add_input(self, input_data: str) -> None:
        """Take input data and store it per line"""
        self.input_data = list(input_data.split("\n"))

    def sum_valid_gameids(self) -> None:
        """Validate each cubeset"""
        gameid = 0
        games = []
        for line in self.input_data:
            gameid += 1
            for cubeset in line.split(": ")[1].split(";"):
                red = green = blue = 0
                cubesets = cubeset.split(",")
                for cubes in cubesets:
                    cubes = cubes.strip()
                    value = int(cubes.split()[0])
                    if "red" in cubes:
                        red = value
                    elif "green" in cubes:
                        green = value
                    elif "blue" in cubes:
                        blue = value
                if red > 12 or green > 13 or blue > 14:
                    break
            else:
                games.append(gameid)

        print(sum(games))

    def sum_power_cubesets(self) -> None:
        """Calculate minimum cubeset power"""
        games = []
        for line in self.input_data:
            red = green = blue = 0
            for cubeset in line.split(": ")[1].split(";"):
                cubesets = cubeset.split(",")
                for cubes in cubesets:
                    cubes = cubes.strip()
                    value = int(cubes.split()[0])
                    if "red" in cubes and value > red:
                        red = value
                    elif "green" in cubes and value > green:
                        green = value
                    elif "blue" in cubes and value > blue:
                        blue = value
            games.append(red * green * blue)

        print(sum(games))


def main() -> None:
    """Solve the puzzle."""
    puzzle = Puzzle(day=2, year=2023)
    gamecube = GameCube()
    gamecube.add_input(puzzle.input_data)
    gamecube.sum_valid_gameids()
    gamecube.sum_power_cubesets()


if __name__ == "__main__":
    main()
