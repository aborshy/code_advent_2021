class Part1:
    @staticmethod
    def solution(file_lines: list[str]) -> int:
        """

        Args:
            file_lines: List of lines from input file

        Returns:

        """

        left_nums = []
        right_nums = []

        for line in file_lines:
            left,right = line.split()
            left_nums.append(int(left))
            right_nums.append(int(right))

        left_nums.sort()
        right_nums.sort()

        zipped_nums = list(zip(left_nums, right_nums))

        return sum([abs(x-y) for x,y in zipped_nums])


class Part2:
    @staticmethod
    def solution(file_lines: list[str]) -> int:
        """

        Args:
            file_lines: List of lines from input file

        Returns:

        """

        total = 0
        left_nums = []
        right_nums_count = {}

        for line in file_lines:
            left,right = line.split()
            left_nums.append(int(left))

            right = int(right)
            if right in right_nums_count:
                right_nums_count[right] += 1
            else:
                right_nums_count[right] = 1

        for n in left_nums:
            if n in right_nums_count:
                total += (n * right_nums_count[n])


        return total


with open("input.txt", "r") as file:
    f = file.read().splitlines()

print(f"Part 1: {Part1.solution(f)}")
print(f"Part 2: {Part2.solution(f)}")



