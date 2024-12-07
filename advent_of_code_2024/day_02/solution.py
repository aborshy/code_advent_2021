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
            int_arr: list[int] = list(map(lambda x: int(x),line.split(" ")))

            last = int_arr[0]
            ascending = True

            if last - int_arr[1] > 0:
                ascending = False

            for num in int_arr[1:]:
                if ascending:
                    if not 1 <= (num - last) <= 3:
                        break
                    else:
                        last = num
                if not ascending:
                    if not 1 <= (last - num) <= 3:
                        break
                    else:
                        last = num
            else:
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

        return 0

with open("input.txt", "r") as file:
    f = file.read().splitlines()

print(f"Part 1: {Part1.solution(f)}")
print(f"Part 2: {Part2.solution(f)}")



