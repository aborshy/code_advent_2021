import solution as s

with open("input.txt", "r") as file:
    inp = file.readlines()


def test_part1_1():
    assert s.Part1.solution(['>']) == 2


def test_part1_2():
    assert s.Part1.solution(['^>v<']) == 4


def test_part1_3():
    assert s.Part1.solution(['^v^v^v^v^v']) == 2


def test_part2_1():
    assert s.Part2.solution(['^v']) == 3


def test_part2_2():
    assert s.Part2.solution(['^^vv^^vv']) == 2


def test_part2_3():
    assert s.Part2.solution(['^v^v^v^v^v>']) == 12
