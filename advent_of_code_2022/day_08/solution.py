class Part1:
    @staticmethod
    def solution(file_lines: list[str]) -> int:
        """
        The expedition comes across a peculiar patch of tall trees all planted carefully in a grid.
        The Elves explain that a previous expedition planted these trees as a reforestation effort.
        Now, they're curious if this would be a good location for a tree house.

        First, determine whether there is enough tree cover here to keep a tree house hidden.
        To do this, you need to count the number of trees that are visible
        from outside the grid when looking directly along a row or column.

        The Elves have already launched a quadcopter to generate a map with the height of each tree
        Args:
            file_lines: List of lines from input file

        Returns:

        """
        total_trees = 0

        forest_rows = [[int(x) for x in line] for line in file_lines]
        forest_columns = list(zip(*forest_rows))

        for x in range(len(forest_rows[0])):
            for y in range(len(forest_rows)):
                current_tree = forest_rows[x][y]
                if all(x < current_tree for x in forest_rows[x][0:y]):
                    total_trees += 1
                    continue
                if all(x < current_tree for x in forest_rows[x][y + 1:]):
                    total_trees += 1
                    continue
                if all(x < current_tree for x in forest_columns[y][0:x]):
                    total_trees += 1
                    continue
                if all(x < current_tree for x in forest_columns[y][x + 1:]):
                    total_trees += 1
                    continue
        return total_trees


class Part2:
    @staticmethod
    def solution(file_lines: list[str]) -> int:

        total_trees = 0

        forest_rows = [[int(x) for x in line] for line in file_lines]
        forest_columns = list(zip(*forest_rows))

        def view(height, sight):
            view_length = 0
            for x in sight:
                view_length += 1
                if x >= height:
                    break
            return view_length

        for x in range(len(forest_rows[0])):
            for y in range(len(forest_rows)):
                current_tree = forest_rows[x][y]

                n = view(current_tree, forest_rows[x][0:y][::-1]) # reverse....
                s = view(current_tree, forest_rows[x][y + 1:])
                w = view(current_tree, forest_columns[y][0:x][::-1])
                e = view(current_tree, forest_columns[y][x + 1:])

                sight = n * s * e * w
                if sight > total_trees:
                    total_trees = sight

        return total_trees


with open("input.txt", "r") as file:
    f = file.read().splitlines()

print(f"Part 1: {Part1.solution(f)}")
print(f"Part 2: {Part2.solution(f)}")
