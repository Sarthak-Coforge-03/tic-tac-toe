from player import Player
from board import Board, Mark


class Game:
    """
    Class to manage the game state
    """

    def __init__(self, player1: Player, player2: Player):
        if player1.mark is player2.mark:
            raise ValueError("Players cannot have same marks")
        if player1.mark != Mark.X:
            raise ValueError("Player1 has to have X mark")
        if player2.mark != Mark.O:
            raise ValueError("Player1 has to have O mark")
        self.player1 = player1
        self.player2 = player2
        self.board = Board()
        self.current = self.player1

    def apply_move(self, row: int, col: int) -> None:
        """Take the row and column provided to apply the move to the board

        Args:
            row (int): row idx of target cell
            col (int): col idx of target cell

        Raises:
            ValueError: if row/col idx are out of bounds
        """
        if not (0 <= row < 3 and 0 <= col < 3):
            raise ValueError("Move out of bounds")
        self.board.set_cell_mark(self.current.mark, row, col)
        if not self.is_over:
            self.current = (
                self.player2 if self.current is self.player1 else self.player1
            )

    @property
    def is_over(self) -> bool:
        """if the game is over (won by either or tied/full)

        Returns:
            bool: true if over else false
        """
        return self.board.check_and_ret_winner() is not None or self.board.is_filled
