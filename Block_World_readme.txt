This project implements a simple and easy solution to the classic Blocks World Problem using Breadth-First Search (BFS).
The Blocks World domain consists of several stacks of blocks, and the goal is to rearrange them so that the initial configuration transforms into a given goal configuration.

The solver finds the shortest sequence of moves, and each move is described in plain English (e.g., “move A from stack 0 → stack 2”).

The code is intentionally simple and beginner-friendly.

BFS(start):
    queue ← [start]
    parent[start] ← (None, None)

    while queue not empty:
        state = queue.pop()

        if state == goal:
            return reconstruct_path(state)

        for each possible move:
            new_state = apply_move(state)

            if new_state not visited:
                parent[new_state] ← (state, move_desc)
                queue.push(new_state)

    return None
