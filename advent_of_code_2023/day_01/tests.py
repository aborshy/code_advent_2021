import solution as s

with open("input.txt", "r") as file:
    inp = file.readlines()


def test_part1_1():
    assert s.Part1.solution([ "1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]) == 0


def test_part1_2():
    assert s.Part1.solution(['']) == 0


def test_part1_3():
    assert s.Part1.solution(['']) == 0


def test_part2_1():
    assert s.Part2.solution(['']) == 0


def test_part2_2():
    assert s.Part2.solution(['']) == 0


def test_part2_3():
    assert s.Part2.solution(['']) == 0
