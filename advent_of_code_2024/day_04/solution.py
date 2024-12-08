from sqlalchemy import false


class Part1:
    @staticmethod
    def solution(file_lines: list[str]) -> int:
        """

        Args:
            file_lines: List of lines from input file

        Returns:

        """

        VALID_STRING = "XMAS"

        if len(VALID_STRING) < 2:
            raise ValueError("Valid string is not greater than 2")

        START_OF_STRING = VALID_STRING[0]

        # find cell around X
        # find Ms and direction
        # for each M, continue checking direction to see if XMAS is spelled
        # repeat until end of input

        def get_cell(matrix_x: int, matrix_y: int, matrix: list[list[str | None]]) -> list[list[str | None]]:
            cell_size = 3
            half_size = cell_size // 2
            cell = []

            for y in range(matrix_y - half_size, matrix_y + half_size + 1):
                row = []
                for x in range(matrix_x - half_size, matrix_x + half_size + 1):
                    if 0 <= y < len(matrix) and 0 <= x < len(matrix[0]):
                        row.append(matrix[y][x])
                    else:
                        row.append(None)
                cell.append(row)

            return cell


        def get_direction(raw_dir_x: int, raw_dir_y: int) -> tuple[int, int]:
            return raw_dir_x - 1, raw_dir_y - 1

        def check_direction(
                first_x: int,
                first_y: int,
                second_direction: tuple[int, int],
                matrix: list[list[str | None]]) -> bool:

            matrix_top_bound = 0
            matrix_bottom_bound = len(matrix) - 1
            matrix_left_bound = 0
            matrix_right_bound = len(matrix[0]) - 1

            if not matrix[first_y][first_x] == VALID_STRING[0]:
                return False

            current_coords = (first_x,first_y)
            for character in VALID_STRING[1:]:
                current_coords = tuple(map(lambda i, j: i + j, current_coords, second_direction))
                if not matrix_left_bound <= current_coords[0] <= matrix_right_bound:
                    return False
                if not matrix_top_bound <= current_coords[1] <= matrix_bottom_bound:
                    return False
                if not matrix[current_coords[1]][current_coords[0]] == character:
                    return False

            return True

        def build_matrix(file_input: list[str]) -> list[list[str]]:
            middle_rows = [[c for c in row] for row in file_input]

            return middle_rows

        valid_xmas_count = 0
        bordered_matrix = build_matrix(file_lines)

        for y, line in enumerate(bordered_matrix):
            for x, char in enumerate(line):
                if char == START_OF_STRING:
                    surrounding_cell = get_cell(x, y, bordered_matrix)

                    directions_to_check = []
                    for cell_y, cell_line in enumerate(surrounding_cell):
                        for cell_x, cell_char in enumerate(cell_line):
                            if cell_char is not None and cell_char.lower() == "m":
                                directions_to_check.append(get_direction(cell_x, cell_y))

                    for direction in directions_to_check:
                        if check_direction(x, y, direction, bordered_matrix):
                            valid_xmas_count += 1

        return valid_xmas_count


class Part2:
    @staticmethod
    def solution(file_lines: list[str]) -> int:
        """

        Args:
            file_lines: List of lines from input file

        Returns:

        """

        # find cell around A
        # check if diags both make MAS (or SAM)

        def get_cell(matrix_x: int, matrix_y: int, matrix: list[list[str | None]]) -> list[list[str | None]]:
            cell_size = 3
            half_size = cell_size // 2
            cell = []

            for y in range(matrix_y - half_size, matrix_y + half_size + 1):
                row = []
                for x in range(matrix_x - half_size, matrix_x + half_size + 1):
                    if 0 <= y < len(matrix) and 0 <= x < len(matrix[0]):
                        row.append(matrix[y][x])
                    else:
                        row.append(None)
                cell.append(row)
            return cell

        def check_cell(cell: list[list[str | None]]) -> bool:
            pos_diag = cell[2][0], cell[1][1], cell[0][2]
            neg_diag = cell[0][0], cell[1][1], cell[2][2]

            if None in pos_diag or None in neg_diag:
                return False

            valid = {"MAS","SAM"}

            pos_str = "".join(pos_diag)
            neg_str = "".join(neg_diag)

            if pos_str in valid and neg_str in valid:
                return True

        def build_matrix(file_input: list[str]) -> list[list[str]]:
            middle_rows = [[c for c in row] for row in file_input]
            return middle_rows

        valid_xmas_count = 0
        bordered_matrix = build_matrix(file_lines)

        for y, line in enumerate(bordered_matrix):
            for x, char in enumerate(line):
                if char == "A":
                    surrounding_cell = get_cell(x, y, bordered_matrix)
                    if check_cell(surrounding_cell):
                        valid_xmas_count += 1

        return valid_xmas_count


with open("input.txt", "r") as file:
    f = file.read().splitlines()

print(f"Part 1: {Part1.solution(f)}")
print(f"Part 2: {Part2.solution(f)}")
