from collections import Counter

class Part1:
    @staticmethod
    def solution(file_lines: list) -> int:
        """
        Returns int of the floor Santa is currently on based on input.

        :param: file: String of one line of any amount of ( and ) characters
        :return: Int of final Santa floor
        """
        parens = file_lines[0]
        d = Counter(parens)
        return d["("] - d[")"]


class Part2:

    @staticmethod
    def solution(file_lines: list) -> int:
        """
        Returns int of the floor Santa is on, or returns the index of which character sent Santa in the basement

        :param: file: String of one line of any amount of ( and ) characters
        :return: Int of final Santa floor, or the move that sent Santa into the basement
        """

        parens = file_lines[0]
        floor = 0

        for index, paren in enumerate(parens, 1):
            if paren == "(":
                floor += 1
            elif paren == ")":
                floor -= 1
            if floor < 0:
                return index
        return floor

with open("input.txt", "r") as file:
    f = file.readlines()
    print(f"Part 1: {Part1.solution(f)}")
    print(f"Part 2: {Part2.solution(f)}")



