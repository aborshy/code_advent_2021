from collections import Counter


def main(parens: str):
    """
    Returns int of the floor Santa is currently on based on input.

    :param: file: String of one line of any amount of ( and ) characters
    :return: Int of final Santa floor
    """

    d = Counter(parens)
    return d["("] - d[")"]


with open("input.txt", "r") as file:
    print(main(file.readline()))
