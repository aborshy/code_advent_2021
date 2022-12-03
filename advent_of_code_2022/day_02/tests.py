import solution as s

with open("input.txt", "r") as file:
    inp = file.readlines()


def test_part1_1():
    assert s.Part1.solution(['A Z']) == 3

def test_part2_1():
    assert s.Part2.solution(['A Z']) == 8
