8-Puzzle Solver Using Depth-First Search (DFS)

This project implements the 8-Puzzle problem using a Depth-First Search (DFS) strategy.
DFS explores one path as deeply as possible before backtracking, printing the first goal configuration it reaches.

The program also includes a mathematical solvability check using inversion count to ensure the puzzle can be solved before DFS begins.

DFS(state):
    if state is goal:
        print path
        return

    add state.board to visited

    for each valid move:
        new_board = swap blank
        if new_board not in visited:
            DFS(new_state)
