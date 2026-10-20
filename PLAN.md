# Goal

This tic-tac-toe game promises a 3 * 3 board along with a CLI intended for human players. The human may play optionally with another human or against an AI. The AI also offers an Easy or Hard difficulty.

# Requirements

| ID | Requirement | How Verified |
|----|-------------|--------------|
| R1 | Two marks, X and O. <br> X always moves first. | Test that the first mark placed is X. <br> O mark is present in the turn after. |
| R2 | Players enter moves as row and columns, index from 1 | Tests for board cell position marked relative to input |
| R3 | Hard never loses on 3x3 when it plays second | Simulate many games against another AI opponent |
| R4 | The game detects vertical, horizontal, and diagonal wins | Test the win condition of boards with and without the state |
| R5 | Players cannot overwrite/select filled cells or input out of board bounds | Test to simulate invalid input, the player does not lose a turn after |
| R6 | The game detects completed board states and marks a draw | Test to check boards entirely filled accurately detect if a winner exists |

# Components
1. Cell (Class) -> Cell class to manage the internal state of the board
2. Board (Class) -> Board class to manage a 3*3 grid of cells
3. Game (Class) -> Game class to manage the overall state so we can track turns
4. Player (ABC) -> Player Abstract class so we can handle different kinds of players
5. Human Player (Class) -> Human player class that relies on the input from the human via CLI
6. AI Player (Class) -> AI player class so a human can contend with an AI
7. Main.py -> Entry point to the program, game loop, and CLI data collection

# Decisions
1. I was considering implementing a difficulty level abstract class to make easy and difficult levels as per strategy pattern. I realized while being superior design, it is over-engineered for the current scope of this assignment
2. I decided to make a cell class instead of just using a character array because it gives excellent future extensibility/state management while being a minimal complexity trade-off over a simple grid of string arrays.

# What Changed 
TODO: ...
