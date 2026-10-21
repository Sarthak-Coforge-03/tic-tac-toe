from abc import ABC, abstractmethod
from typing import Protocol, runtime_checkable
from board import Board, Coordinate
import random


@runtime_checkable
class Player(Protocol):
    """Protocol class defining the function of every kind of player"""

    name: str

    def turn(self, row: int, col: int) -> Coordinate: ...


class HumanPlayer(Player):
    """Human player class defining

    Args:
        Player (Protocol): Protocol class to follow
    """

    def __init__(self, name="Human Player"):
        self.name = name

    def turn(self, row, col) -> Coordinate:
        """Takes the turn for the human by returning their chosen row and column
        Normalizes the input 0-indexing for our board management

        Args:
            row (int): chosen row to mark in this turn
            col (int): chosen column to mark in this turn

        Returns:
            _type_: _description_
        """
        return (row - 1, col - 1)


class AIPlayer(Player, ABC):
    """Class defined for the AI player

    Args:
        Player (Protocol): Protocol to follow for every AI player
        ABC (Abstract): This is an abstract class for every AI implementation
    """

    def __init__(self, name="AI Player"):
        self.name = name

    def _calculate_move(self, board: Board) -> Coordinate:
        """
        Method to calculate the next move based on board state
        """
        pass

    def turn(self, board: Board) -> Coordinate:
        return self._calculate_move(board=board)


class EasyAIPlayer(AIPlayer):
    """AI player for easy mode

    Args:
        AIPlayer (AIPlayer): Abstract class for AI player to follow
    """

    def __init__(self, name="Easy AI Player"):
        super().__init__(name)

    def turn(self, board: Board):
        """Take a turn as an AI player

        Returns:
            tuple[int, int]: Row, col int coordinate for this turn
        """
        return super().turn(board=board)

    def _calculate_move(self, board):
        """Calculate the next move by choosing a random available

        Args:
            board (_type_): _description_

        Returns:
            _type_: _description_
        """
        return random.choice(board.get_empty_cells())


class HardAIPlayer(AIPlayer):
    """AI player for hard mode

    Args:
        AIPlayer (Absract class): Abstract class to follow
    """

    def __init__(self, name="Easy AI Player"):
        super().__init__(name)

    def turn(self, board: Board):
        """Take a turn as an AI player

        Returns:
            tuple[int, int]: Row, col int coordinate for this turn
        """
        return super().turn(board=board)

    def _calculate_move(self, board):
        """Calculate the next move by using minimax

        Args:
            board (_type_): _description_

        Returns:
            _type_: _description_
        """
        return super()._calculate_move(board)
