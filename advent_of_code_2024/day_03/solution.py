total = 0
enabled = True

class Part1:
    @staticmethod
    def solution(file_lines: list[str]) -> int:
        """

        Args:
            file_lines: List of lines from input file

        Returns:

        """
        import re

        for line in file_lines:
            pattern = r"mul\(\d+,\d+\)"
            matches = re.findall(pattern, line)

            def mul(x,y):
                global total
                total += x*y

            for func in matches:
                exec(func, {"mul":mul, "total":total})

        return total


class Part2:
    @staticmethod
    def solution(file_lines: list[str]) -> int:
        """

        Args:
            file_lines: List of lines from input file

        Returns:

        """
        import re

        global total
        total = 0

        for line in file_lines:
            pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
            matches = re.findall(pattern, line)

            def mul(x,y):
                global total
                global enabled

                if enabled:
                    total += x*y

            def do():
                global enabled
                enabled = True

            def dont():
                global enabled
                enabled = False

            for func in matches:
                if func == "don't()":
                    curr = "dont()"
                else:
                    curr = func

                print(curr)
                exec(curr, {"mul":mul, "total":total, "do":do, "dont":dont})

        return total


with open("input.txt", "r") as file:
    f = file.read().splitlines()

print(f"Part 1: {Part1.solution(f)}")
print(f"Part 2: {Part2.solution(f)}")



