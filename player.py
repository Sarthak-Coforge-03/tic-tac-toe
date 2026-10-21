from abc import ABC, abstractmethod
from typing import Protocol, runtime_checkable
from board import Board, Coordinate, Mark
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

    @abstractmethod
    def _calculate_move(self, board: Board, mark: Mark) -> Coordinate:
        """
        Method to calculate the next move based on board state
        """
        ...

    def turn(self, board: Board, mark: Mark) -> Coordinate:
        return self._calculate_move(board=board, mark=mark)


class EasyAIPlayer(AIPlayer):
    """AI player for easy mode

    Args:
        AIPlayer (AIPlayer): Abstract class for AI player to follow
    """

    def __init__(self, name="Easy AI Player"):
        super().__init__(name)

    def _calculate_move(self, board: Board, mark: Mark) -> Coordinate:
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

    def __init__(self, name="Hard AI Player"):
        super().__init__(name)

    def _calculate_move(self, board: Board, mark: Mark) -> Coordinate:
        """Calculate the next move by using minimax
        This specific implementation of minimax was done by the following instructions:
        It's X's turn in state 1. X generates the states 2, 3, and 4 and calls minimax on those states.
        State 2 pushes the score of +10 to state 1's score list, because the game is in an end state.
        State 3 and 4 are not in end states, so 3 generates states 5 and 6 and calls minimax on them, while state 4 generates states 7 and 8 and calls minimax on them.
        State 5 pushes a score of -10 onto state 3's score list, while the same happens for state 7 which pushes a score of -10 onto state 4's score list.
        State 6 and 8 generate the only available moves, which are end states, and so both of them add the score of +10 to the move lists of states 3 and 4.
        Because it is O's turn in both state 3 and 4, O will seek to find the minimum score, and given the choice between -10 and +10, both states 3 and 4 will yield -10.
        Finally the score list for states 2, 3, and 4 are populated with +10, -10 and -10 respectively, and state 1 seeking to maximize the score will chose the winning move with score +10, state 2.

                Args:
                    board (Board): the board object we are playing on
                    mark (Mark): The mark this algorithm wants to win for

                Returns:
                    Coordinate: empty cell that maximizes the score for mark
        """
        opponent = Mark.O if mark == Mark.X else Mark.X
        scores = []
        moves = []
        for move in board.get_empty_cells():
            next_board = self._board_with_move(board=board, mark=mark, move=move)
            scores.append(
                self._minimax(
                    board=next_board,
                    mark=mark,
                    current_mark=opponent,
                )
            )
            moves.append(move)
        best_index = scores.index(max(scores))
        return moves[best_index]

    def _minimax(self, board: Board, mark: Mark, current_mark: Mark) -> int:
        """Implements the minimax algorithm recursively

        Args:
            board (Board): The state to evaluate
            mark (Mark): Mark to optimize for
            current_mark (Mark): the mark current turn of minmax belongs to

        Returns:
            int: score value
        """
        if board.check_and_ret_winner() is not None or board.is_filled:
            return self._score(board=board, mark=mark)
        opponent = Mark.O if current_mark == Mark.X else Mark.X
        scores = []
        for move in board.get_empty_cells():
            next_board = self._board_with_move(
                board=board, mark=current_mark, move=move
            )
            scores.append(
                self._minimax(
                    board=next_board,
                    mark=mark,
                    current_mark=opponent,
                )
            )

        if current_mark == mark:
            return max(scores)
        return min(scores)

    def _score(self, board: Board, mark: Mark) -> int:
        """Scoring function for the min-max algorithm

        Args:
            board (Board): board object to access state
            mark (Mark): mark to optimize for

        Returns:
            int: score given
        """
        winner = board.check_and_ret_winner()
        if winner == mark:
            return 10
        elif winner and winner != mark:
            return -10
        else:
            return 0

    def _board_with_move(self, board: Board, mark: Mark, move: Coordinate) -> Board:
        """Copy the current structure of marks in the grid and generate a brand new board from it
        Additionally append your own 1 extra move on it

        Args:
            board (Board): Board grid to copy current state of
            mark (Mark): Mark to make on the chosen move
            move (Coordinate): where to mark this move

        Returns:
            Board: current state to copy
        """
        grid = [[cell.mark for cell in row] for row in board.board]
        next_board = Board.board_from_marks(grid=grid)
        next_board.set_cell_mark(mark=mark, row=move[0], col=move[1])
        return next_board
