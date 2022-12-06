class Part1:
    @staticmethod
    def solution(file_lines: list[str]) -> int:
        total = 0
        for x in file_lines:
            firstpart, secondpart = set(x[:len(x)//2]), set(x[len(x)//2:])
            for y in firstpart:
                if y in secondpart:
                    if ord(y) > 90:
                        total += (ord(y) - 96)
                    else:
                        total += (ord(y) - 38)

        return total


class Part2:
    @staticmethod
    def solution(file_lines: list[str]) -> int:
        total = 0

        for n in range(0,len(file_lines),3):
            a = set(file_lines[n])
            b = set(file_lines[n+1])
            c = set(file_lines[n+2])

            for x in a:
                if x in b and x in c:
                    if ord(x) > 90:
                        total += (ord(x) - 96)
                        break
                    else:
                        total += (ord(x) - 38)
                        break

        return total


with open("input.txt", "r") as file:
    f = file.read().splitlines()

print(f"Part 1: {Part1.solution(f)}")
print(f"Part 2: {Part2.solution(f)}")



