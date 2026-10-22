from game import Game
from player import AIPlayer, HumanPlayer, Player, EasyAIPlayer, HardAIPlayer
from board import Mark


def handle_mode_choice():
    """
    Function that provides an infinite while loop unless the player chooses a valid mode

    Returns:
        _type_: _description_
    """
    choice = None
    while choice not in (1, 2):
        choice = int(
            input(
                "Please input [1] to play against the AI or [2] for multi-player mode:\n"
            )
        )
    return choice


def handle_difficulty_choice():
    """
    Function that provides an infinite loop unless player chooses a valid difficulty
    """
    difficulty = None
    while difficulty not in (1, 2):
        difficulty = int(
            input("Please input [1] for easy difficulty and [2] for hard difficulty:\n")
        )
    return difficulty


def print_difficulty_choice_acknowledgement(difficulty: int):
    """
    Prints the message acknowledging difficulty choice

    Args:
        difficulty (int): 1 for easy ; 2 for hard
    """
    if difficulty == 1:
        print("Playing on Easy Mode!")
    elif difficulty == 2:
        print("Playing on Hard Mode!")


def initialize_players(choice: int, difficulty: int) -> tuple[Player, Player]:
    """Initializes the players based on the mode and difficulty choices

    Args:
        choice (int): 1 for against AI, 2 for against human
        difficulty (int): 1 for easy, 2 for hard

    Raises:
        ValueError: in case player chooses against AI mode but no difficulty is provided

    Returns:
        tuple[Player, Player]: Player1 and player2 instance
    """
    player1 = HumanPlayer()
    if choice == 1 and not difficulty:
        raise ValueError(
            "Cannot choose to play against AI and not have a difficulty selected!"
        )
    elif choice == 1 and difficulty == 1:
        player2 = EasyAIPlayer()
    elif choice == 1 and difficulty == 2:
        player2 = HardAIPlayer()
    else:
        player2 = HumanPlayer(mark=Mark.O)
    return (player1, player2)


def read_move() -> tuple[int, int]:
    """Read a 1-based row and column from stdin until the input is valid.

    Returns 0-based coordinates for the board.
    """
    prompt = "Please input your desired row and column separated by a space: "
    while True:
        parts = input(prompt).split()
        if len(parts) != 2:
            print("Please enter exactly two numbers")
            continue
        try:
            row, col = int(parts[0]), int(parts[1])
        except ValueError:
            print("Row and column must be integers.")
            continue
        if not (1 <= row <= 3 and 1 <= col <= 3):
            print("Row and column must be between 1 and 3.")
            continue
        return (row - 1, col - 1)


def game_loop(game: Game):
    """
    tic-tac-toe game loop to run while progress is going

    Args:
        game (Game): game state manager class
    """
    while not game.is_over:
        print(game.board.to_string(), end="\n\n")
        if isinstance(game.current, AIPlayer):
            print(f"{game.current.mark.upper()}'s turn (AI)")
            row, col = game.current.turn(game.board, game.current.mark)
        else:
            row, col = read_move()
        try:
            game.apply_move(row=row, col=col)
        except ValueError as exc:
            print(exc)
    print(game.board.to_string())


def tic_tac_toe():
    """
    Function to orchestrate the tic tac toe game
    """
    choice = handle_mode_choice()
    difficulty = None
    if choice == 2:
        print("You have chosen multi-player mode!")
    elif choice == 1:
        print("You have chosen to play against the AI!")
        difficulty = handle_difficulty_choice()
        print_difficulty_choice_acknowledgement(difficulty=difficulty)
    player1, player2 = initialize_players(choice=choice, difficulty=difficulty)
    game = Game(player1=player1, player2=player2)
    game_loop(game=game)
    winner = game.board.check_and_ret_winner()
    if winner:
        print(f"{winner.upper()} is the WINNER!")
    else:
        print("This was a draw, better luck next time!")


if __name__ == "__main__":
    tic_tac_toe()
