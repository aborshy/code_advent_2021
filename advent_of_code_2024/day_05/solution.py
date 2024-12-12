from attr.setters import validate


class Part1:
    @staticmethod
    def solution(file_lines: list[str]) -> int:
        """

        Args:
            file_lines: List of lines from input file

        Returns:

        """

        # x|y page x and page y
        # rule that page X has to come before page Y
        # empty line splits inputs
        # list of inputs that need to be rule checked
        # if valid, find middle idx and add to total, return total

        def validate(given_rules: dict[int, set], inputs: list[str]):
            # reverse iterate over list, build not allowed entries based on rules
            # if entry is in not allowed, then it's invalid
            output = []

            for to_validate in inputs:
                curr = list(map(lambda x: int(x), reversed(to_validate.split(","))))
                rule_set = set()
                for num in curr:
                    rule_set.update(given_rules[num])
                    if num in rule_set:
                        break
                else:
                    output.append(list(map(lambda x: int(x), to_validate.split(","))))

            return output

        def gather_total(valid_lines: list[list[int]]):
            total = 0

            for line in valid_lines:
                total += line[len(line) // 2]

            return total

        rules: dict[int, set] = {}
        valid_lines: list[list[int]] = []

        for n, line in enumerate(file_lines):
            if line == "":
                valid_lines = validate(rules, file_lines[n+1:])
                break
            page_rules = line.split("|")
            line_rule = tuple(map(lambda x: int(x), page_rules))
            try:
                rules[line_rule[0]].add(line_rule[1])
            except KeyError:
                rules[line_rule[0]] = set()
                rules[line_rule[0]].add(line_rule[1])

        return gather_total(valid_lines)



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



