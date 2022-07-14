from collections import Counter


class Part1:
    @staticmethod
    def solution(parens: str):
        """
        Returns int of the floor Santa is currently on based on input.

        :param: file: String of one line of any amount of ( and ) characters
        :return: Int of final Santa floor
        """

        d = Counter(parens)
        return d["("] - d[")"]


class Part2:
    @staticmethod
    def solution(parens: str):
        """
        Returns int of the floor Santa is currently on, or returns the index of which character sent Santa in the basement

        :param: file: String of one line of any amount of ( and ) characters
        :return: Int of final Santa floor, or the move that sent Santa into the basement
        """

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
    print(Part1.solution(file.readline()))
    print(Part2.solution(file.readline()))
