from board import Mark, Cell
import pytest


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
