import pytest

from board import Board, Cell, Mark

WINS = [
    [
        [Mark.X, Mark.X, Mark.X],
        [Mark.O, Mark.O, None],
        [None, None, None],
    ],
    [
        [Mark.X, Mark.X, None],
        [Mark.O, Mark.O, Mark.O],
        [Mark.X, None, None],
    ],
    [
        [Mark.O, Mark.O, None],
        [None, None, None],
        [Mark.X, Mark.X, Mark.X],
    ],
    [
        [Mark.O, Mark.X, Mark.X],
        [Mark.O, Mark.X, None],
        [Mark.O, None, None],
    ],
    [
        [Mark.O, Mark.X, None],
        [Mark.O, Mark.X, None],
        [None, Mark.X, None],
    ],
    [
        [Mark.X, Mark.X, Mark.O],
        [Mark.X, None, Mark.O],
        [None, None, Mark.O],
    ],
    [
        [Mark.X, Mark.O, None],
        [Mark.O, Mark.X, None],
        [None, None, Mark.X],
    ],
    [
        [Mark.X, Mark.X, Mark.O],
        [Mark.X, Mark.O, None],
        [Mark.O, None, None],
    ],
]

DRAWS = [
    [
        [Mark.X, Mark.O, Mark.X],
        [Mark.X, Mark.O, Mark.O],
        [Mark.O, Mark.X, Mark.X],
    ],
    [
        [Mark.X, Mark.X, Mark.O],
        [Mark.O, Mark.O, Mark.X],
        [Mark.X, Mark.O, Mark.X],
    ],
]


def test_new_cell_is_empty():
    """Test if the new cell is empty"""
    cell = Cell()
    assert not cell.is_filled
    assert cell.mark == None


@pytest.mark.parametrize("mark", [Mark.O, Mark.X])
def test_place_fills_cell(mark: Mark):
    """Test is the place works properly on the cell

    Args:
        mark (Mark): enum of marks in a cell
    """
    cell = Cell()
    cell.place(mark=mark)
    assert cell.is_filled
    assert cell.mark == mark


@pytest.mark.parametrize("mark", [Mark.O, Mark.X])
def test_errors_cell_override_attempt(mark: Mark):
    """Test if a filled cell errors if you attempt to place a mark in it

    Args:
        mark (Mark): mark enum for cell values
    """
    cell = Cell(mark=mark)
    with pytest.raises(ValueError, match="already filled"):
        cell.place(Mark.O if mark is Mark.X else Mark.X)


def test_initialized_empty_board():
    """
    Tests that the new instance of a board is always empty
    """
    board = Board()
    assert len(board.get_empty_cells()) == 9
    assert not board.is_filled


def test_detect_filled_boards():
    """
    Test to check if boards that are filled are detected
    """
    for grid in DRAWS:
        board = Board.board_from_marks(grid=grid)
        assert board.is_filled


def test_detect_wins_in_board():
    """
    Test to check if the board with win conditions are detected
    """
    for grid in WINS:
        board = Board.board_from_marks(grid=grid)
        assert board.check_and_ret_winner()


def test_set_cell_mark():
    """
    Test to see if setting marks on a cell are persisted
    """
    board = Board()
    assert not board.get_cell_at_coord(row=0, col=0).is_filled
    assert board.get_cell_at_coord(row=0, col=0).mark is None
    board.set_cell_mark(Mark.X, row=0, col=0)
    assert board.get_cell_at_coord(row=0, col=0).is_filled
    assert board.get_cell_at_coord(row=0, col=0).mark == Mark.X


def test_get_empty_cells():
    """
    Test to see if get empty cells is working appropriately
    """
    empty_board = Board()
    empty_list = empty_board.get_empty_cells()
    assert len(empty_list) == 9
    for grid in DRAWS:
        board = Board.board_from_marks(grid=grid)
        assert len(board.get_empty_cells()) == 0


def test_board_to_string():
    """
    Test to see if board is accurately converted into string
    """
    board = Board.board_from_marks(
        grid=[
            [Mark.X, Mark.O, None],
            [None, Mark.X, Mark.O],
            [Mark.O, None, Mark.X],
        ]
    )
    assert board.to_string() == (
        " X | O |   \n-----------\n   | X | O \n-----------\n O |   | X "
    )
