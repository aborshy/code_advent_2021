class Part1:
    @staticmethod
    def solution(file_lines: list[str]) -> int:
        """
        Santa is delivering presents to an infinite two-dimensional grid of houses.

        He begins by delivering a present to the house at his starting location,
        and then an elf at the North Pole calls him via radio and tells him where to move next.
        Moves are always exactly one house to the north (^), south (v), east (>), or west (<). After each move,
        he delivers another present to the house at his new location.

        However, the elf back at the North Pole has had a little too much eggnog,
        and so his directions are a little off, and Santa ends up visiting some houses more than once.
        How many houses receive at least one present?

        Args:
            file_lines: List of lines from input file

        Returns: Int of unique houses visited

        """

        direction_dict = {
            "<": (-1, 0),
            ">": (1, 0),
            "v": (0, -1),
            "^": (0, 1)
        }
        x, y = 0, 0
        locations = {(0, 0): (0, 0)}  # empty tuple represents starting point
        total = 1

        for direct in file_lines[0]:
            x += direction_dict[direct][0]
            y += direction_dict[direct][1]
            if (x, y) not in locations:
                total += 1
                locations[(x, y)] = (x, y)

        return total


class Part2:
    @staticmethod
    def solution(file_lines: list[str]) -> int:
        """
        --- Part Two ---
        The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa,
        to deliver presents with him.

        Santa and Robo-Santa start at the same location (delivering two presents to the same starting house),
        then take turns moving based on instructions from the elf,
        who is eggnoggedly reading from the same script as the previous year.

        This year, how many houses receive at least one present?

        Args:
            file_lines: List of lines from input file

        Returns: Int of total gifts given.

        """
        instructions = {
            "<": (-1, 0),
            ">": (1, 0),
            "v": (0, -1),
            "^": (0, 1)
        }

        locations = {(0, 0): (0, 0)}

        class Santa:

            def __init__(self):
                self.x = 0
                self.y = 0
                self.total = 0

            def move(self, direction, locations):
                self.x += instructions[direction][0]
                self.y += instructions[direction][1]
                if (self.x, self.y) not in locations:
                    self.total += 1
                    locations[(self.x, self.y)] = (self.x, self.y)
                return locations

        robosanta = Santa()
        santa = Santa()

        for n, direct in enumerate(file_lines[0], 1):
            if n % 2 != 0:
                santa.move(direct, locations)
            else:
                robosanta.move(direct, locations)

        return robosanta.total + santa.total + 1


with open("input.txt", "r") as file:
    f = file.read().splitlines()

print(f"Part 1: {Part1.solution(f)}")
print(f"Part 2: {Part2.solution(f)}")
