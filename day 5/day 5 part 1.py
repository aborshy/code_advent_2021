with open("input.txt") as x:
    lines = x.readlines()

# input manip stuff
lines = [x.strip() for x in lines]
raw_points = [x.split(" -> ") for x in lines]
points_list = [[x.split(",") for x in y] for y in raw_points]
points_list = [[[int(x) for x in a] for a in b] for b in points_list]

"""
assuming no negatives as a coordinate will be input, also only full ints with 45 deg slopes.
i guess i could use floats for non 45 deg slopes, but it's advent of code and it didn't ask for it
"""

class LineSeg:

    def __init__(self, points):
        self.first_point = [points[0]]
        self.second_point = [points[1]]

    def line(self):
        horiz = list(range(self.first_point[0], self.second_point[0] + 1))
        if horiz is []:
            horiz = self.first_point[0]
        vert = list(range(self.first_point[1], self.second_point[1] + 1))
        if vert is []:
            vert = self.first_point[0]

        if len(horiz) > len(vert):
            vert = vert * len(horiz)
        else:
            horiz = horiz * len(vert)

        return list(zip(horiz, vert))

print(points_list)
all_lines = [LineSeg(x) for x in points_list]
