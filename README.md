# tic-tac-toe

A command-line game of tic-tac-toe on a 3x3 grid. Two players take turns placing X and O (X goes first); the first to get three in a row, column, or diagonal wins, and a full board with no winner is a draw. Taken cells and invalid input are rejected without costing you your turn.

You can play against another human, or against an AI in one of two difficulties:
- **Easy**: picks a random empty cell.
- **Hard**: uses minimax and never loses.

## Setup
1. Clone this repository
2. Please ensure your system has python installed
3. Please create a venv in the root dir with ```python -m venv .venv```
4. Please activate .venv with ```source .venv/bin/activate```
5. Please download requirements with ```pip install -r requirements.txt```
6. Please start game with ```python main.py```
7. Please start the tests with ```pytest```
