import pytest
from player import EasyAIPlayer, HardAIPlayer
from board import Board, Mark
import random


@pytest.fixture
def board() -> Board:
    """Fixture for a fresh clean board for every test

    Returns:
        Board: Empty new board
    """
    return Board()


def test_Easy_AI_player_turn(board):
    """Tests if the easy AI player is choosing turns correctly

    Args:
        board (Board): empty board to begin with
    """
    rng = random.Random(0)
    easy_ai_player = EasyAIPlayer(rng=rng)
    choices = rng.sample(board.get_empty_cells(), k=5)
    for choice in choices:
        board.set_cell_mark(mark=Mark.X, row=choice[0], col=choice[1])
    remaining_cells = board.get_empty_cells()
    turn = easy_ai_player.choose_move(board=board, mark=Mark.O)
    assert turn in remaining_cells


def test_Hard_AI_player_turn_is_valid(board):
    """Tests if the Hard AI player is returning valid coordinates

    Args:
        board (Board): empty board to begin with
    """
    rng = random.Random(0)
    hard_ai_player = HardAIPlayer(rng=rng)
    choice = rng.choice(board.get_empty_cells())
    board.set_cell_mark(mark=Mark.O, row=choice[0], col=choice[1])
    remaining_cells = board.get_empty_cells()
    turn = hard_ai_player.choose_move(board=board, mark=Mark.O)
    assert turn in remaining_cells


def test_hard_never_skips_winning_move(board):
    """Hard takes the immediate win when given a state close to it

    Args:
        board (Board): empty board
    """
    board.set_cell_mark(Mark.O, 0, 0)
    board.set_cell_mark(Mark.O, 0, 1)
    board.set_cell_mark(Mark.X, 1, 0)
    board.set_cell_mark(Mark.X, 1, 1)
    board.set_cell_mark(Mark.X, 2, 0)
    move = HardAIPlayer().choose_move(board=board, mark=Mark.O)
    assert move == (0, 2)
