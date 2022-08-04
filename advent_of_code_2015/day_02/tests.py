import solution as s

with open("input.txt", "r") as file:
    inp = file.readlines()


def test_part1_1():
    assert s.Part1.solution(['2x3x4']) == 58


def test_part1_2():
    assert s.Part1.solution(['1x1x10']) == 43


def test_part2_1():
    assert s.Part2.solution(['2x3x4']) == 34


def test_part2_2():
    assert s.Part2.solution(['1x1x10']) == 14
