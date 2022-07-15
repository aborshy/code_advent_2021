import solution as s

with open("input.txt", "r") as file:
    inp = file.readlines()


def test_part1_1():
    assert s.Part1.solution(inp) is 'test'


def test_part1_2():
    assert s.Part1.solution(inp) is 1


def test_part1_3():
    assert s.Part1.solution(inp) is None


def test_part2_1():
    assert s.Part2.solution(inp) is 'test'


def test_part2_2():
    assert s.Part2.solution(inp) is 1


def test_part2_3():
    assert s.Part2.solution(inp) is None
