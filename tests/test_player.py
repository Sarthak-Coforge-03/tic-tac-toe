import pytest
from player import HumanPlayer, EasyAIPlayer
from board import Board, Mark
import random


@pytest.fixture
def board() -> Board:
    """Fixture for a fresh clean board for every test

    Returns:
        Board: Empty new board
    """
    return Board()


def test_human_player_turn():
    """
    Tests if the human player normalizes the turn input properly
    """
    human = HumanPlayer()
    assert human.turn(3, 3) == (2, 2)


def test_Easy_AI_player_turn(board):
    """Tests if the easy AI player is choosing turns correctly

    Args:
        board (Board): empty board to begin with
    """
    easy_ai_player = EasyAIPlayer()
    choices = random.sample(board.get_empty_cells(), k=5)
    (
        board.set_cell_mark(mark=Mark.X, row=choice[0], col=choice[1])
        for choice in choices
    )
    remaining_cells = board.get_empty_cells()
    turn = easy_ai_player.turn(board=board)
    assert turn in remaining_cells
