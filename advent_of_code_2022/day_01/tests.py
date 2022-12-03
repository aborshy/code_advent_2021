import solution as s

with open("input.txt", "r") as file:
    inp = file.readlines()


def test_part1_1():
    assert s.Part1.solution(['1000','2000','3000','','4000','','5000','6000']) == 11000
