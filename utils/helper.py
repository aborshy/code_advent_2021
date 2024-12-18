from typing import TypeVar, Generic, List, Dict, Tuple

T = TypeVar('T')

class GridDict(Generic[T]):
    """
    A class to represent and manipulate a 2D matrix.

    Attributes:
        coord_dict (dict): A dictionary mapping coordinates to their values in the matrix.
        matrix (list[list[T]]): The 2D matrix.
        len_x (int): The number of columns in the matrix.
        len_y (int): The number of rows in the matrix.
    """

    def __init__(self, matrix: List[List[T]]):
        """
        Initializes the GridDict object with a given matrix.

        Args:
            matrix (list[list[T]]): The 2D matrix.
        """
        self.coord_dict = self.matrix_to_coordinate_dict(matrix)
        self.matrix = matrix
        self.len_x = len(matrix[0])
        self.len_y = len(matrix)

    def __repr__(self) -> str:
        return '\n'.join([' '.join(map(str, row)) for row in self.matrix])

    def __str__(self) -> str:
        return self.__repr__()

    @staticmethod
    def matrix_to_coordinate_dict(matrix: List[List[T]]) -> Dict[Tuple[int, int], T]:
        """
        Converts a matrix to a dictionary of coordinates.

        Args:
            matrix (list[list[T]]): The 2D matrix.

        Returns:
            dict: A dictionary mapping coordinates to their values in the matrix.
        """
        coord_dict = {}
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                value = matrix[i][j]
                if value != 0:
                    coord_dict[(i, j)] = value
        return coord_dict

    def get_coord_value(self, x: int, y: int) -> T:
        """
        Returns the value at the given coordinates if within bounds.

        Args:
            x (int): The x-coordinate.
            y (int): The y-coordinate.

        Returns:
            T: The value at the given coordinates, or None if out of bounds.
        """
        if self.check_in_bounds(x, y):
            return self.coord_dict[(y, x)]

    def check_in_bounds(self, x: int, y: int) -> bool:
        """
        Checks if the given coordinates are within the bounds of the matrix.

        Args:
            x (int): The x-coordinate.
            y (int): The y-coordinate.

        Returns:
            bool: True if the coordinates are within bounds, False otherwise.
        """
        return -1 < x < self.len_x and -1 < y < self.len_y

    def find_first_value(self, value: T) -> Tuple[int, int]:
        """
        Finds the first occurrence of a value in the matrix.

        Args:
            value (T): The value to find.

        Returns:
            tuple[int, int]: The coordinates of the first occurrence of the value.
        """
        for n_y, y in enumerate(self.matrix):
            for n_x, x in enumerate(y):
                if x == value:
                    return n_x, n_y

    def find_all_value_coords(self, value: T) -> List[Tuple[int, int]]:
        """
        Finds all occurrences of a value in the matrix.

        Args:
            value (T): The value to find.

        Returns:
            list[tuple[int, int]]: A list of coordinates of all occurrences of the value.
        """
        coords = []
        for n_y, y in enumerate(self.matrix):
            for n_x, x in enumerate(y):
                if x == value:
                    coords.append((n_x, n_y))
        return coords

    @staticmethod
    def get_rectangle_coords(x1: int, y1: int, x2: int, y2: int) -> List[Tuple[int, int]]:
        """
        Gets the coordinates of all squares within a rectangle or square defined by two opposite corners.

        Args:
            x1 (int): The x-coordinate of the first corner.
            y1 (int): The y-coordinate of the first corner.
            x2 (int): The x-coordinate of the opposite corner.
            y2 (int): The y-coordinate of the opposite corner.

        Returns:
            list[tuple[int, int]]: A list of coordinates of all squares within the rectangle or square.
        """
        coords = []
        for x in range(min(x1, x2), max(x1, x2) + 1):
            for y in range(min(y1, y2), max(y1, y2) + 1):
                coords.append((x, y))
        return coords

    def get_line_values(self, x1: int, y1: int, x2: int, y2: int) -> List[T]:
        """
        Gets all values in a 2D matrix in a line given the beginning and end points.

        Args:
            x1 (int): The x-coordinate of the beginning point.
            y1 (int): The y-coordinate of the beginning point.
            x2 (int): The x-coordinate of the end point.
            y2 (int): The y-coordinate of the end point.

        Returns:
            list[T]: A list of values in the matrix along the line.
        """
        points = []
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        sx = 1 if x1 < x2 else -1
        sy = 1 if y1 < y2 else -1
        err = dx - dy

        while True:
            points.append((x1, y1))
            if x1 == x2 and y1 == y2:
                break
            e2 = err * 2
            if e2 > -dy:
                err -= dy
                x1 += sx
            if e2 < dx:
                err += dx
                y1 += sy

        line_values = [self.matrix[y][x] for x, y in points if 0 <= y < len(self.matrix) and 0 <= x < len(self.matrix[0])]

        return line_values

    def set_coord_value(self, x: int, y: int, value: T):
        """
        Sets the value at the given coordinates if within bounds.

        Args:
            x (int): The x-coordinate.
            y (int): The y-coordinate.
            value (T): The value to set at the coordinates.
        """
        if self.check_in_bounds(x, y):
            self.coord_dict[(y, x)] = value
            self.matrix[y][x] = value