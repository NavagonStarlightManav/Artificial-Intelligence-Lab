-Puzzle Solver Using BFS (Shortest Path Search)

This project implements the 8-Puzzle problem using a Breadth-First Search (BFS) approach to find the shortest possible solution path to reach the goal state.
Before solving, the program performs a mathematical solvability check based on inversion count to ensure the puzzle can be solved.

BFS(start):
    queue ← [start]
    visited ← {start.board}

    while queue not empty:
        state ← queue.pop_front()

        if state.board == goal:
            print_path(state)
            return

        for each valid direction:
            new_board ← move blank
            if new_board not in visited:
                visited.add(new_board)
                queue.push(new_state)
