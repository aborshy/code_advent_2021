class Part1:
    @staticmethod
    def solution(file_lines: list[str]) -> int:
        """

        Args:
            file_lines: List of lines from input file

        Returns:

        """
        x = 0
        inp = file_lines[0]
        code_length = 4
        while True:
            if len(set(inp[x:x+code_length])) == code_length:
                break
            x += 1
        return x+code_length


class Part2:
    @staticmethod
    def solution(file_lines: list[str]) -> int:
        """

        Args:
            file_lines: List of lines from input file

        Returns:

        """
        x = 0
        inp = file_lines[0]
        code_length = 14
        while True:
            if len(set(inp[x:x+code_length])) == code_length:
                break
            x += 1
        return x+code_length



with open("input.txt", "r") as file:
    f = file.read().splitlines()

print(f"Part 1: {Part1.solution(f)}")
print(f"Part 2: {Part2.solution(f)}")



