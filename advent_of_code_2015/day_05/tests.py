import solution as s

with open("input.txt", "r") as file:
    inp = file.readlines()


def test_part1_1():
    assert s.Part1.solution(['ugknbfddgicrmopn']) == 1, "Result: 1 (nice) because it has three vowels and no bad strs"


def test_part1_2():
    assert s.Part1.solution(['aaa']) == 1, "Result: 1 (nice) because it has three vowels and a double letter"


def test_part1_3():
    assert s.Part1.solution(['jchzalrnumimnmhp']) == 0, "Result: 0 (naughty) because no double letter"


def test_part1_4():
    assert s.Part1.solution(['haegwjzuvuyypxyu']) == 0, "Result: 0 (naughty) because it contains sub string xy"


def test_part1_5():
    assert s.Part1.solution(['dvszwmarrgswjxmb']) == 0, "Result: 0 (naughty) because it only contains one vowel"


def test_part2_1():
    assert s.Part2.solution(['']) == 0


def test_part2_2():
    assert s.Part2.solution(['']) == 0


def test_part2_3():
    assert s.Part2.solution(['']) == 0
