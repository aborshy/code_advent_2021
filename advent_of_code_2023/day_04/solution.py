class Part1:
    @staticmethod
    def solution(file_lines: list[str]) -> int:
        """

        Args:
            file_lines: List of lines from input file

        Returns:

        """
        output = 0
        for x in file_lines:
            winning, game = x.split(":")[1].strip().split("|")
            winning = {x for x in winning.split(" ") if x != ""}
            game = [x for x in game.split(" ") if x != ""]
            points = 0
            for x in game:
                if x in winning:
                    if points == 0:
                        points += 1
                    else:
                        points *= 2
            output += points
        return output


class Part2:
    @staticmethod
    def solution(file_lines: list[str]) -> int:
        """

        Args:
            file_lines: List of lines from input file

        Returns:

        """
        output = file_lines
        print(file_lines)
        for n,x in enumerate(output):
            winning, game = x.split(":")[1].strip().split("|")
            winning = {int(x) for x in winning.split(" ") if x != ""}
            print(winning)

            game = {int(x) for x in game.split(" ") if x != ""}
            print(game)
            to_append = []
            if len(game.intersection(winning)):
                print(game.intersection(winning))
                for x in output[n+1:n+len(game.intersection(winning))]:
                    output.append(x)
                continue


        return len(output)


with open("input.txt", "r") as file:
    f = file.read().splitlines()

print(f"Part 1: {Part1.solution(f)}")
print(f"Part 2: {Part2.solution(f)}")



