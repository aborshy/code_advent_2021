import os

from numpy.matrixlib.defmatrix import matrix


class Part1:
    @staticmethod
    def solution(file_lines: list[str]) -> int:
        """

        Args:
            file_lines: List of lines from input file

        Returns:

        """

        class Direction:
            def __init__(self,x,y):
                self.x = x
                self.y = y

            @property
            def direction(self):
                return self.x, self.y

            @direction.setter
            def direction(self, direction: tuple[int, int]):
                self.x, self.y = direction

            def __add__(self, other):
                if not isinstance(other, (tuple, Direction)):
                    raise ValueError()

                self.x += other[0]
                self.y += other[1]

                return self.x, self.y

            def __getitem__(self, item: int):
                if item == 0:
                    return self.x
                elif item == 1:
                    return self.y
                else:
                    raise ValueError()

            def __repr__(self):
                return f"Direction ({self.x},{self.y})"

        class Guard:
            x: int
            y: int
            char: str
            dir: Direction

            def __init__(self, x:int, y:int, char: str):
                self.x = x
                self.y = y
                self.char = char
                self.dir = self.__get_direction_from_char()

            def __get_direction_from_char(self) -> Direction:
                if self.char == "^":
                    return Direction(0, -1)
                elif self.char == ">":
                    return Direction(1,0)
                elif self.char == "<":
                    return Direction(-1,0)
                elif self.char == "v":
                    return Direction(0,1)


            def move_in_direction(self, direction: Direction):
                self.x += direction.x
                self.y += direction.y

            def get_coord_in_front(self):
                x_coord = self.x + self.dir[0]
                y_coord = self.y + self.dir[1]
                return x_coord, y_coord

            def turn_right(self):
                directions = "^>v<"
                current_direction = directions.find(self.char)
                next_direction = current_direction + 1
                self.char = directions[next_direction % len(directions)]
                self.dir = self.__get_direction_from_char()



        class Grid:
            def __init__(self, matrix: list[str]):
                self.coord_dict = self.matrix_to_coordinate_dict(matrix)
                self.matrix = matrix
                self.len_x = len(matrix[0])
                self.len_y = len(matrix)

            @staticmethod
            def matrix_to_coordinate_dict(matrix: list[str]) -> dict[tuple[int, int], any]:
                coord_dict = {}
                rows = len(matrix)
                cols = len(matrix[0])
                for i in range(rows):
                    for j in range(cols):
                        value = matrix[i][j]
                        if value != 0:
                            coord_dict[(i, j)] = value
                return coord_dict


            def get_coord_value(self,x: int,y: int):
                if self.check_in_bounds(x,y):
                    return self.coord_dict[(y,x)]

            def check_in_bounds(self,x,y):
                if -1 < x < self.len_x and -1 < y < self.len_y:
                    return True
                return False

            def find_first_value(self, value: any) -> tuple[int, int]:
                for n_y, y in enumerate(self.matrix):
                    for n_x, x in enumerate(y):
                        if x == value:
                            return n_x, n_y

            def print_with_excluded_cells(self,cells_to_mark: set[tuple]):
                os.system("cls")
                printed_matrix = self.matrix
                printed_matrix = [[x.split() for x in y] for y in printed_matrix]
                print(printed_matrix)
                for x,y in cells_to_mark:
                    printed_matrix[y][x] = "#"


        grid = Grid(file_lines)
        guard = None
        for x in "^><v":
            guard_pos = grid.find_first_value(x)
            if guard_pos:
                guard = Guard(guard_pos[0], guard_pos[1], x)
                break

        unique_coords = set()
        while grid.check_in_bounds(guard.x,guard.y):
            coord_to_check = guard.get_coord_in_front()
            check_coord_value = grid.get_coord_value(coord_to_check[0], coord_to_check[1])
            if check_coord_value is None:
                break
            if check_coord_value == "." or check_coord_value in "^<>v":
                unique_coords.add((guard.x, guard.y))
                guard.move_in_direction(guard.dir)
                # grid.print_with_excluded_cells(unique_coords)
                continue
            elif check_coord_value == "#":
                unique_coords.add((guard.x, guard.y))
                guard.turn_right()
                # grid.print_with_excluded_cells(unique_coords)
                continue

        grid.print_with_excluded_cells(unique_coords)
        return len(unique_coords)


class Part2:
    @staticmethod
    def solution(file_lines: list[str]) -> int:
        """

        Args:
            file_lines: List of lines from input file

        Returns:

        """
        return 0


with open("input.txt", "r") as file:
    f = file.read().splitlines()

print(f"Part 1: {Part1.solution(f)}")
print(f"Part 2: {Part2.solution(f)}")



