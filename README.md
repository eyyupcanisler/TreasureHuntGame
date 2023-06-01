# Treasure Hunt Game

This code implements a simple treasure hunt game in Python. The game is played on a grid where the player navigates and collects treasures while avoiding monsters and hazards.

## Game Rules

- The game grid consists of empty cells, treasures (T), monsters (M), swords (S), potions (P), and venom (V).
- The player's starting position is randomly determined on an empty cell.
- The player can move left (L), right (R), up (U), or down (D) on the grid.
- The goal is to collect treasures and increase the score while avoiding monsters and hazards.
- The player's score is incremented by 1 for each empty cell and by 2 for each treasure collected.
- The player can collect swords to defeat monsters and potions to counteract venom.
- If the player encounters a monster without a sword, the game ends.
- If the player encounters venom without a potion, the game ends.
- The game also tracks the player's moves and the corresponding scores.

## Usage

1. Run the script using a Python interpreter.
2. Enter L, R, U, or D to move the player left, right, up, or down, respectively.
3. The game will display the updated grid, score, and inventory (swords and potions).
4. The game continues until an invalid move is entered or the player encounters a monster or venom without the necessary items.

## File Structure

- `main.py`: The main Python script that implements the treasure hunt game.
- `sample.json`: A JSON file that stores the game history, including scores and moves.

## Author

This game was created by Eyyüpcan İşler as a fun coding project. Feel free to modify and improve it as desired.

Enjoy playing the treasure hunt game!
