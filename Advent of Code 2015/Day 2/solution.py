class Part1:
    @staticmethod
    def solution(file_lines: list[str]) -> int:
        """
        Find needed amt of wrapping paper in feet^2, accounting for slack needed (+area of the smallest side).
        l will always be the smallest, h the largest.

        Args:
            file_lines (list): List of lines from input file

        Returns:
            int: Total amount of wrapping paper for all presents
        """
        total = 0
        for x in file_lines:
            l, w, h = x.split('x')
            l, w, h = sorted([int(l), int(w), int(h)])
            total += 2 * l * w + 2 * w * h + 2 * h * l + l * w
        return total


class Part2:
    @staticmethod
    def solution(file_lines: list[str]) -> int:
        """
        Determines the shortest line to be made around an object, then adds the cubic volume to it.
        l will always be the smallest, h the largest.

        Example:
            input: 1x2x10
            shortest line: 6 (1+1+2+2)
            volume: 20 (1x2x10)
            output: 26
        Args:
            file_lines: List of lines from input file

        Returns: int of the shortest line + cubic volume

        """
        total = 0
        for x in file_lines:
            l, w, h = x.split('x')
            l, w, h = sorted([int(l), int(w), int(h)])
            total += l * 2 + w * 2 + l * w * h

        return total


with open("input.txt", "r") as file:
    f = file.read().splitlines()

print(f"Part 1: {Part1.solution(f)}")
print(f"Part 2: {Part2.solution(f)}")
