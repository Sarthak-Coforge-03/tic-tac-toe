from enum import StrEnum, unique


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
