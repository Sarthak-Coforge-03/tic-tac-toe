import random
from board import Mark
from game import Game
from player import EasyAIPlayer, HardAIPlayer


def test_never_loses_on_3x3():
    """
    runs the game 20 times with easy vs hard AI
    Hard never loses
    seeded via a random.Random(0) passed in, so the choice in easy AI sequentially chooses
    """
    rng = random.Random(0)
    player1 = EasyAIPlayer(mark=Mark.X, rng=rng)
    player2 = HardAIPlayer(mark=Mark.O)
    for _ in range(20):
        game = Game(player1=player1, player2=player2)
        while not game.is_over:
            player = game.current
            row, col = player.choose_move(game.board, player.mark)
            game.apply_move(row=row, col=col)
        assert game.board.check_and_ret_winner() != Mark.X
