# AI-Powered Connect Four (Puissance 4)

## Project Overview
This project implements an **AI-powered Connect Four** game as part of an **Introduction to AI** course. The goal was to explore game AI, decision-making algorithms, and heuristic evaluations using the **Minimax algorithm with Alpha-Beta pruning**.

## Features
- **AI vs. Human Mode:** Players can compete against an AI opponent.
- **Minimax Algorithm:** Utilized to determine the best moves for AI.
- **Alpha-Beta Pruning:** Optimizes Minimax for better efficiency.
- **Heuristic Evaluation:** AI prioritizes moves based on board state.
- **Board Representation:** Implements a 6x12 grid for gameplay.

## Technologies Used
- **Python**
- **Game AI Algorithms** (Minimax, Alpha-Beta Pruning)

## How the AI Works
1. **Board Initialization:** A 6x12 matrix is set up.
2. **Minimax Algorithm:** The AI evaluates possible moves up to a depth of 5.
3. **Alpha-Beta Pruning:** Speeds up decision-making by cutting unnecessary evaluations.
4. **Heuristic Evaluation:** AI prioritizes winning moves and blocking opponent moves.
5. **Gameplay Loop:** The game continues until a player wins or the board is full.

**Gameplay Instructions:**
   - Choose whether the AI (`R`) or human (`J`) plays first.
   - Players drop pieces in columns (0-11).
   - AI makes decisions based on the Minimax algorithm.
   - The game ends when a player gets four in a row.

## AI Decision-Making
- **Move Ordering:** AI prioritizes central moves for strategic play.
- **Scoring System:** AI evaluates board positions using:
  - +100 for four in a row (win)
  - +5 for three in a row with an empty space
  - +2 for two in a row with two empty spaces
  - Negative scores for opponent advantages
- **Game Tree Search:** The AI explores possible outcomes before choosing an optimal move.

## License
This project was developed for educational purposes as part of an **Intro to AI** course.

