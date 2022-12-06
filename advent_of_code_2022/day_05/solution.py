import re
class Part1:
    @staticmethod
    def solution(file_lines: list[str]) -> str:
        """

        Args:
            file_lines: List of lines from input file

        Returns:

        """
        raw_input = []

        for x in range(0,8):
            raw_input.append([x for x in file_lines[x][1::4]])
        column_stacks = []

        for x in range(0, len(raw_input[0])):
            column_stacks.append([])
            for y in range(0,len(raw_input)):
                column_stacks[x].append(raw_input[y][x])
            column_stacks[x] = [x for x in column_stacks[x][::-1] if x != " "]

        for x in file_lines[10::]:
            amt,frm,to = [int(x) for x in re.split("[^0-9]", x) if x != ""]
            for x in range(0,amt):
                crate = column_stacks[frm-1].pop()
                column_stacks[to-1].append(crate)

        return "".join([x[-1] for x in column_stacks])


class Part2:
    @staticmethod
    def solution(file_lines: list[str]) -> str:
        """

        Args:
            file_lines: List of lines from input file

        Returns:

        """
        raw_input = []

        for x in range(0,8):
            raw_input.append([x for x in file_lines[x][1::4]])
        column_stacks = []

        for x in range(0, len(raw_input[0])):
            column_stacks.append([])
            for y in range(0,len(raw_input)):
                column_stacks[x].append(raw_input[y][x])
            column_stacks[x] = [x for x in column_stacks[x][::-1] if x != " "]

        for x in file_lines[10::]:
            amt,frm,to = [int(x) for x in re.split("[^0-9]", x) if x != ""]

            crates = []
            for x in range(0,amt):
                crates.append(column_stacks[frm-1].pop())
            column_stacks[to-1].extend(reversed(crates))

        return "".join([x[-1] for x in column_stacks])


with open("input.txt", "r") as file:
    f = file.read().splitlines()

print(f"Part 1: {Part1.solution(f)}")
print(f"Part 2: {Part2.solution(f)}")



