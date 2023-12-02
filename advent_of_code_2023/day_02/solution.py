import functools
import operator
import sys
from collections import namedtuple
from typing import NamedTuple
from dataclasses import dataclass


class Part1:
    @staticmethod
    def solution(file_lines: list[str]) -> int:
        """
        You play several games and record the information from each game (your puzzle input). Each game is listed with
        its ID number (like the 11 in Game 11: ...) followed by a semicolon-separated list of subsets of cubes that
        were revealed from the bag (like 3 red, 5 green, 4 blue).

        For example, the record of a few games might look like this:

        Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
        Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
        Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
        Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
        Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
        In game 1, three sets of cubes are revealed from the bag (and then put back again). The first set is
        3 blue cubes and 4 red cubes; the second set is 1 red cube, 2 green cubes, and 6 blue cubes;
        the third set is only 2 green cubes.

        The Elf would first like to know which games would have been possible if the bag contained only
        12 red cubes, 13 green cubes, and 14 blue cubes?

        In the example above, games 1, 2, and 5 would have been possible if the bag had been loaded with that
        configuration. However, game 3 would have been impossible because at one point the Elf showed you 20 red
        cubes at once; similarly, game 4 would also have been impossible because the Elf showed you 15 blue cubes at
        once. If you add up the IDs of the games that would have been possible, you get 8.

        Determine which games would have been possible if the bag had been loaded with only
        12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?

        Args:
            file_lines: List of lines from input file

        Returns:

        """
        MAX_RED, MAX_GREEN, MAX_BLUE = 12, 13, 14

        output = 0
        for line in file_lines:
            game = CubeGame(line, MAX_RED, MAX_GREEN, MAX_BLUE)
            if game.check_below_max():
                output += game.id

        return output


class Part2:
    @staticmethod
    def solution(file_lines: list[str]) -> int:
        """

        Args:
            file_lines: List of lines from input file

        Returns:

        """
        output = 0
        for line in file_lines:
            output += CubeGame(line).lowest_amt_needed()
        return output


@dataclass
class Draw:
    r: int = 0
    g: int = 0
    b: int = 0

    def power(self):
        return self.r * self.g * self.b


class CubeGame:
    def __init__(self, raw_game: str, max_red=None, max_green=None, max_blue=None):
        self.max_red, self.max_green, self.max_blue = max_red, max_green, max_blue
        self.id = self.parse_id(raw_game)
        self.draws: list[Draw] = self.parse_draws(raw_game)

    @staticmethod
    def parse_id(raw_game) -> int:
        if len(raw_game) == 0:
            raise RuntimeError

        return int(raw_game.split(":")[0][5:])

    @staticmethod
    def parse_draws(raw_game) -> list[Draw]:
        output = []
        if len(raw_game) == 0:
            return output

        raw_draws: list[str] = raw_game.split(":")[1].split(";")

        for raw_draw in raw_draws:
            draw = list(map(lambda x: x.strip(), raw_draw.split(",")))

            current_draw = Draw()
            for color_amt in draw:
                current_draw.r = int(color_amt.split(" ")[0]) if color_amt.find("red") > 0 else current_draw.r
                current_draw.g = int(color_amt.split(" ")[0]) if color_amt.find("green") > 0 else current_draw.g
                current_draw.b = int(color_amt.split(" ")[0]) if color_amt.find("blue") > 0 else current_draw.b

            output.append(current_draw)

        return output

    def check_below_max(self) -> bool:
        for draw in self.draws:
            if draw.r > self.max_red:
                return False
            if draw.g > self.max_green:
                return False
            if draw.b > self.max_blue:
                return False
        return True

    def lowest_amt_needed(self) -> (int, int, int):
        lowest_r, lowest_g, lowest_b = 0, 0, 0
        for draw in self.draws:
            lowest_r = draw.r if draw.r > lowest_r else lowest_r
            lowest_g = draw.g if draw.g > lowest_g else lowest_g
            lowest_b = draw.b if draw.b > lowest_b else lowest_b
        return self.__get_power(lowest_r, lowest_g, lowest_b)

    def __get_power(self, *args) -> int:
        return functools.reduce(operator.mul, args)


with open("input.txt", "r") as file:
    f = file.read().splitlines()

print(f"Part 1: {Part1.solution(f)}")
print(f"Part 2: {Part2.solution(f)}")
