with open("input.txt") as x:
    lines = x.readlines()

# input manip stuff
lines = [x.strip() for x in lines]
raw_points = [x.split(" -> ") for x in lines]
points_list = [[x.split(",") for x in y] for y in raw_points]
points_list = [[[int(x) for x in a] for a in b] for b in points_list]


class LineSeg:

    def __init__(self, points):
        self.first_point = points[0]
        self.second_point = points[1]
        self.x1 = self.first_point[0]
        self.x2 = self.second_point[0]
        self.y1 = self.first_point[1]
        self.y2 = self.second_point[1]

    def line(self):
        """
        creates a line segment and returns a list of all points
        """
        if self.x1 < self.x2:   # check if pos or neg slope
            horiz = list(range(self.first_point[0], self.second_point[0] + 1))
        else:
            horiz = list(reversed(range(self.second_point[0], self.first_point[0] + 1)))

        if horiz is []:  # if range is 0
            horiz = self.first_point[0]

        if self.y1 < self.y2:  # check if pos or neg slope
            vert = list(range(self.first_point[1], self.second_point[1] + 1))
        else:
            vert = list(reversed(range(self.second_point[1], self.first_point[1] + 1)))

        if vert is []:  # if range is 0
            vert = self.first_point[0]

        if len(horiz) > len(vert):     # gen a list of n length coord if it doesn't change, will prob merge with
            vert = vert * len(horiz)   # upper if statements later
        else:
            horiz = horiz * len(vert)

        return list(zip(horiz, vert))


all_lines = [LineSeg(x) for x in points_list]

test = LineSeg(points_list[3])
print(test.line())

"""
after this i want to check each line seg list of coords against all others to see if there's any overlap
(may have to div by 2 because of repeats (line 1 intersects with line 2, and line 2 intersects with line 1)
"""
