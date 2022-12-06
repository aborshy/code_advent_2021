class Part1:
    @staticmethod
    def solution(file_lines: list[str]) -> int:
        """

        Args:
            file_lines: List of lines from input file

        Returns:

        """
        total = 0
        for x in file_lines:
            first_elf, second_elf = x.split(",")
            first_elf = [int(x) for x in first_elf.split("-")]
            f_range = range(first_elf[0],first_elf[1]+1)
            second_elf = [int(x) for x in second_elf.split("-")]
            s_range = range(second_elf[0], second_elf[1] + 1)

            if (f_range[0] in s_range and f_range[-1] in s_range) or (s_range[0] in f_range and s_range[-1] in f_range):
                total += 1


        return total


class Part2:
    @staticmethod
    def solution(file_lines: list[str]) -> int:
        """

        Args:
            file_lines: List of lines from input file

        Returns:

        """
        total = 0
        for x in file_lines:
            first_elf, second_elf = x.split(",")
            first_elf = [int(x) for x in first_elf.split("-")]
            f_range = range(first_elf[0], first_elf[1] + 1)
            second_elf = [int(x) for x in second_elf.split("-")]
            s_range = range(second_elf[0], second_elf[1] + 1)

            if (f_range[0] in s_range or f_range[-1] in s_range) or (s_range[0] in f_range or s_range[-1] in f_range):
                total += 1

        return total


with open("input.txt", "r") as file:
    f = file.read().splitlines()

print(f"Part 1: {Part1.solution(f)}")
print(f"Part 2: {Part2.solution(f)}")



