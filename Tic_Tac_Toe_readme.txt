Tic-Tac-Toe Game with Minimax AI (Python)

This project implements an unbeatable Tic-Tac-Toe AI using the Minimax algorithm.
The computer plays as X, and the human plays as O.
A complete game tree is generated using recursion, and the AI always picks the move with the best minimax score.

The algorithm explores all possible moves and ensures the computer never loses.

minimax(state):
    if terminal(state):
        return score(state)

    if isMax:
        best = -∞
        for each empty cell:
            score = minimax(resulting child)
            best = max(best, score)
        return best

    else:
        best = +∞
        for each empty cell:
            score = minimax(child)
            best = min(best, score)
        return best
