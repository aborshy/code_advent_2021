class Part1:
    @staticmethod
    def solution(file_lines: list[str]) -> int:
        """
        This rope bridge creaks as you walk along it. You aren't sure how old it is, or whether it
        can even support your weight.

        It seems to support the Elves just fine, though. The bridge spans a gorge which was carved out by
        the massive river far below you.

        You step carefully; as you do, the ropes stretch and twist. You decide to distract yourself by
        modeling rope physics; maybe you can even figure out where not to step.

        Consider a rope with a knot at each end; these knots mark the head and the tail of the rope.
        If the head moves far enough away from the tail, the tail is pulled toward the head.

        Due to nebulous reasoning involving Planck lengths, you should be able to model the positions of
        the knots on a two-dimensional grid. Then, by following a hypothetical series of motions (your puzzle input)
        for the head, you can determine how the tail will move.

        After simulating the rope, you can count up all the positions the tail visited at least once.
        In this diagram, 's' again marks the starting position (which the tail also visited)
        and # marks other positions the tail visited:

        How many positions does the tail of the rope visit at least once?

        Args:
            file_lines: List of lines from input file

        Returns: positions of the rope's tail visit at least once?

        """

        class RopePart:
            def __init__(self, x: int, y: int):
                self.x = x
                self.y = y

            def move(self, shift: tuple[int, int]):
                self.x += shift[0]
                self.y += shift[1]

        def check(tail: RopePart, head: RopePart, last_seen: tuple[int, int]):
            if abs(tail.x - head.x) > 1 or abs(tail.y - head.y) > 1:
                tail.x = last_seen[0]
                tail.y = last_seen[1]
                return check(tail, head, last_seen)
            else:
                return head.x, head.y

        visited = set()
        movement_dict = {
            "U": (0, 1),
            "D": (0, -1),
            "L": (-1, 0),
            "R": (1, 0)
        }
        head = RopePart(0, 0)
        tail = RopePart(0, 0)
        last_seen = (0,0)

        for x in file_lines:
            line = x.split(" ")
            for i in range(int(line[1])):
                head.move(movement_dict[line[0]])
                last_seen = check(tail, head, last_seen)
                visited.add((tail.x, tail.y))

        return len(visited)


class Part2:
    @staticmethod
    def solution(file_lines: list[str]) -> int:
        """
        Args:
            file_lines: List of lines from input file
        Returns:

        """

        class RopePart:
            def __init__(self, x: int, y: int):
                self.x = x
                self.y = y

            def move(self, shift: tuple[int, int]):
                self.x += shift[0]
                self.y += shift[1]

        def check(tail: RopePart, head: RopePart, last_seen: tuple[int, int]):
            if abs(tail.x - head.x) > 9 or abs(tail.y - head.y) > 9:
                tail.x = last_seen[0]
                tail.y = last_seen[1]
                return check(tail, head, last_seen)
            else:
                return head.x, head.y

        visited = set()
        movement_dict = {
            "U": (0, 1),
            "D": (0, -1),
            "L": (-1, 0),
            "R": (1, 0)
        }
        head = RopePart(0, 0)
        tail = RopePart(0, 0)
        last_seen = (0, 0)

        for x in file_lines:
            line = x.split(" ")
            for i in range(int(line[1])):
                head.move(movement_dict[line[0]])
                last_seen = check(tail, head, last_seen)
                visited.add((tail.x, tail.y))

        return len(visited)


with open("input.txt", "r") as file:
    f = file.read().splitlines()

print(f"Part 1: {Part1.solution(f)}")
print(f"Part 2: {Part2.solution(f)}")
