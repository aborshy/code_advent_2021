class Part1:
    @staticmethod
    def solution(file_lines: list[str]) -> int:
        """

        Args:
            file_lines: List of lines from input file

        Returns:

        """
        total = 0

        for line in file_lines:
            o = filter(lambda x: x.isdecimal(), line)
            num = "".join(o)
            if len(num) == 1:
                num += num
            else:
                num = "".join([num[0], num[-1]])

            total += int(num)

        return total


class Part2:
    @staticmethod
    def solution(file_lines: list[str]) -> int:
        import re
        """

        Args:
            file_lines: List of lines from input file

        Returns:

        """
        total = 0
        number_strings = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
        pattern = r'\d+|(?:one|two|three|four|five|six|seven|eight|nine)'
        number_dict = {string: str(index) for index, string in enumerate(number_strings,1)}
        for line in file_lines:
            raw_nums = re.findall(pattern,line)
            nums = "".join(map(lambda x: number_dict[x] if x in number_dict else x, raw_nums))
            print(nums)
            if len(nums) == 1:
                nums += nums
            else:
                nums = "".join([nums[0], nums[-1]])
            print(nums)
            total += int(nums)
        return total


with open("input.txt", "r") as file:
    f = file.read().splitlines()

print(f"Part 1: {Part1.solution(f)}")
print(f"Part 2: {Part2.solution(f)}")
