from typing import Tuple


class Part1:
    @staticmethod
    def solution(file_lines: list[str]) -> int:
        """

        Args:
            file_lines: List of lines from input file

        Returns:


    """
        valid_symbols = {x for x in """!@#$%^&*()_-+={}[],/;'\"\'\\"""}
        output = 0
        parser = LineParser()
        symbols = []
        numbers = []


        for line in file_lines:
            symbols.append(parser.find_symbols(line))
            numbers.append(parser.find_numbers(line))
        out = parser.check_output_near_symbol(numbers, symbols)
        return sum(out)


class Part2:
    @staticmethod
    def solution(file_lines: list[str]) -> int:
        """

        Args:
            file_lines: List of lines from input file

        Returns:

        """
        return 0


class LineParser:

    def __init__(self):
        self.numbers = None
        self.valid_symbols = {x for x in """!@#$%^&*()_-+={}[],/;'\"\'\\"""}

    def find_symbols(self, line: str) -> set[int]:
        output = []
        for n, x in enumerate(line):
            if x in self.valid_symbols:
                output.append(n)

        return set(output)

    def find_numbers(self, line: str):
        output = []
        new_num = []
        num_indexes = []

        for n, x in enumerate(line):
            if len(new_num) == 0 and not x.isdigit():
                continue
            elif x.isdigit():
                new_num.append(x)
                num_indexes.append(int(n))
            else:
                output.append(tuple([int("".join(new_num)), tuple(num_indexes)]))
                new_num = []
                num_indexes = []

        return tuple(output)

    def check_output_near_symbol(self, numbers, symbols):
        output = []
        print(symbols)
        for n, x in enumerate(numbers, 0):
            print(n)
            for y in x:
                print(y)
                idx_to_check = list(range(y[1][0]-1, y[1][-1]+1))
                print(idx_to_check)
                for line in symbols[n-1:n+1]:
                    print(line)
                    for num in idx_to_check:
                        if num in line:
                            print("true")
                            output.append(y[0])
                            break
        return output

with open("input.txt", "r") as file:
    f = file.read().splitlines()

print(f"Part 1: {Part1.solution(f)}")
print(f"Part 2: {Part2.solution(f)}")
