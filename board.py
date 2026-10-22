from enum import StrEnum, unique

Coordinate = tuple[int, int]
Combo = tuple[Coordinate, Coordinate, Coordinate]
WINNING_COMBINATIONS: list[Combo] = [
    ((0, 0), (0, 1), (0, 2)),
    ((1, 0), (1, 1), (1, 2)),
    ((2, 0), (2, 1), (2, 2)),
    ((0, 0), (1, 0), (2, 0)),
    ((0, 1), (1, 1), (2, 1)),
    ((0, 2), (1, 2), (2, 2)),
    ((0, 0), (1, 1), (2, 2)),
    ((0, 2), (1, 1), (2, 0)),
]


@unique
class Mark(StrEnum):
    """Enum for the state of our cell objects

    Args:
        StrEnum (str): Either character X or O
    """

    X = "x"
    O = "o"


class Cell:
    def __init__(self, mark: Mark | None = None):
        """
        Class to manage a single unit in the tic-tac-toe board
        mark: In case we want to make a pre-filled cell for testing
        """
        self._mark: Mark | None = None
        if mark is not None:
            self.place(mark)

    def place(self, mark: Mark):
        """Function to place a mark enum object in the cell

        Args:
            mark (Mark): Mark enum object

        Raises:
            ValueError: If something besides a mark object was pushed as an argument
            ValueError: If this cell is already filled, specifically disallowed override
        """

        if not isinstance(mark, Mark):
            raise ValueError("Cannot place an object which is not a mark into a cell")
        if self.is_filled:
            raise ValueError("Cell is already filled, cannot override")
        self._mark = mark

    @property
    def is_filled(self) -> bool:
        """getter to ask if the mark is filled already

        Returns:
            bool: True if there is a mark, else false
        """
        return self._mark is not None

    @property
    def mark(self) -> Mark | None:
        """Getter to get the current mark object

        Returns:
            Mark | None: Returns the mark object or None if the cell is not filled yet
        """
        return self._mark


class Board:
    """
    Class to initialize the tic-tac-toe board
    """

    def __init__(self):
        self._board: list[list[Cell]] = [[Cell() for _ in range(3)] for _ in range(3)]

    @property
    def board(self) -> list[list[Cell]]:
        """Property to access the board underneath

        Returns:
            list[list[Cell]]: The array of array of cells
        """
        return self._board

    @property
    def is_filled(self) -> bool:
        """
        Property to check if all the cells have been filled inside this board
        """
        return all(cell.is_filled for row in self.board for cell in row)

    def set_cell_mark(self, mark: Mark, row: int, col: int):
        """set a mark object to the cell

        Args:
            mark (Mark): Mark.X or Mark.O object
            row (int): row at which to set the mark
            col (int): col at which to set the mark
        """
        self.board[row][col].place(mark=mark)

    def get_cell_at_coord(self, row: int, col: int) -> Cell:
        """Get cell at coordinate

        Args:
            row (int): row of the wanted cell
            col (int): col of the wanted cell

        Returns:
            Cell: returns a Cell object
        """
        return self.board[row][col]

    def check_and_ret_winner(self) -> Mark | None:
        """Checks if any of the win combinations have been satisfied

        Returns:
            bool: if a win condition has been satisfied
        """
        for combo in WINNING_COMBINATIONS:
            cell_marks = [
                self.get_cell_at_coord(row=coord[0], col=coord[1]).mark
                for coord in combo
            ]
            if all(cell_marks):
                if all(mark == Mark.X for mark in cell_marks) or all(
                    mark == Mark.O for mark in cell_marks
                ):
                    return cell_marks[0]
        return None

    @classmethod
    def board_from_marks(cls, grid: list[list[Mark | None]]) -> "Board":
        """Class method to generate an instance with custom set boards for testing purposes

        Args:
            grid (list[list[Mark  |  None]]): a grid of None objects or a specific mark

        Returns:
            Board: Instance of class with custom marks already placed
        """
        board = cls()
        for row_idx, row in enumerate(grid):
            for col, mark in enumerate(row):
                if mark is not None:
                    board.set_cell_mark(mark=mark, row=row_idx, col=col)
        return board

    def get_empty_cells(self) -> list[Coordinate]:
        """returns a list of the coordinates of empty cells

        Returns:
            list[Coordinate]: list of empty cell coordinates
        """
        result = []
        for row_idx, row in enumerate(self.board):
            for col, cell in enumerate(row):
                if not cell.is_filled:
                    result.append((row_idx, col))
        return result

    def to_string(self) -> str:
        """Return a string representation of the grid

        Returns:
            str: string representation of every cell
        """
        lines = []
        for row in self.board:
            cells = [cell.mark.upper() if cell.mark else " " for cell in row]
            lines.append("".join(cells))
        return "\n".join(lines)
