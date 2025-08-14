from copy import deepcopy
from collections import deque


class State:
    def __init__(self, parent, board, depth):
        self.parent = parent       # reference to parent state
        self.board = board         # current grid configuration
        self.depth = depth         # level in BFS tree


def is_valid(x, y, n):
    """Check if a move is within grid bounds."""
    return 0 <= x < n and 0 <= y < n


def is_goal(board, goal):
    """Check if the current state matches the goal state."""
    return board == goal


def find_blank(board):
    """Locate the blank (0) tile position."""
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                return i, j
    return -1, -1


def print_path(state):
    """Recursively print the solution path."""
    if state is None:
        return
    print_path(state.parent)
    for row in state.board:
        print(*row)
    print("----")


# ---------------------------- SOLVABILITY CHECK ----------------------------
def count_inversions(flat_board):
    arr = [x for x in flat_board if x != 0]
    inv = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                inv += 1
    return inv


def is_solvable(board, n):
    """Check puzzle solvability mathematically."""
    flat = [num for row in board for num in row]
    inv = count_inversions(flat)
    if n % 2 == 1:
        return inv % 2 == 0
    else:
        blank_row = n - find_blank(board)[0]
        return (inv + blank_row) % 2 == 0


# ---------------------------- BFS FUNCTION ----------------------------
def bfs(start_state, goal, n):
    """Perform BFS to find the shortest solution path."""
    q = deque([start_state])
    visited = {tuple(tuple(row) for row in start_state.board)}

    while q:
        current = q.popleft()

        # Check goal
        if is_goal(current.board, goal):
            print("\nGoal reached!\n")
            print_path(current)
            print("Total steps:", current.depth)
            return

        x, y = find_blank(current.board)

        # Moves: Left, Right, Up, Down
        row_moves = [0, 0, -1, 1]
        col_moves = [-1, 1, 0, 0]

        for i in range(4):
            new_x, new_y = x + row_moves[i], y + col_moves[i]

            if is_valid(new_x, new_y, n):
                new_board = deepcopy(current.board)
                new_board[x][y], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[x][y]

                new_state_tuple = tuple(tuple(row) for row in new_board)
                if new_state_tuple not in visited:
                    visited.add(new_state_tuple)
                    q.append(State(current, new_board, current.depth + 1))

    print("No solution found.")


# ---------------------------- MAIN FUNCTION ----------------------------
def main():
    n = int(input("Enter puzzle size (n): "))

    board = []
    print("Enter puzzle numbers row-wise (use 0 for blank):")
    for i in range(n):
        row = []
        for j in range(n):
            val = int(input(f"Enter number at ({i},{j}): "))
            row.append(val)
        board.append(row)

    # Construct goal state
    goal = [[(i * n + j + 1) % (n * n) for j in range(n)] for i in range(n)]

    print("\nInitial board:")
    for row in board:
        print(*row)
    print("\nGoal board:")
    for row in goal:
        print(*row)

    if not is_solvable(board, n):
        print("\nThis puzzle configuration is UNSOLVABLE.")
        return

    start_state = State(None, board, 0)
    bfs(start_state, goal, n)


if __name__ == "__main__":
    main()
