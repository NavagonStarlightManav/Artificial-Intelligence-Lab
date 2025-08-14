from copy import deepcopy

class State:
    def __init__(self, parent, board, depth):
        self.parent = parent
        self.board = board
        self.depth = depth


def is_valid(x, y, n):
    return 0 <= x < n and 0 <= y < n


def is_goal(board, goal):
    return board == goal


def find_blank(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                return i, j
    return -1, -1


def print_path(state):
    if state is None:
        return
    print_path(state.parent)
    for row in state.board:
        print(*row)
    print("----")



def count_inversions(flat_board):
    arr = [x for x in flat_board if x != 0]
    inversions = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                inversions += 1
    return inversions


def is_solvable(board, n):
    flat = [num for row in board for num in row]
    inv = count_inversions(flat)
    if n % 2 == 1:
        return inv % 2 == 0  # odd grid
    else:
        blank_row = n - find_blank(board)[0]
        return (inv + blank_row) % 2 == 0



def dfs(current, visited, goal, n):
    visited.add(tuple(tuple(row) for row in current.board))  # store immutable version

    if is_goal(current.board, goal):
        print("\nGoal reached!\n")
        print_path(current)
        print("Total steps:", current.depth)
        exit(0)

    x, y = find_blank(current.board)

    row_moves = [0, 0, -1, 1]
    col_moves = [-1, 1, 0, 0]

    for i in range(4):
        new_x, new_y = x + row_moves[i], y + col_moves[i]

        if is_valid(new_x, new_y, n):
            new_board = deepcopy(current.board)
            new_board[x][y], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[x][y]

            new_state_tuple = tuple(tuple(row) for row in new_board)
            if new_state_tuple not in visited:
                child = State(current, new_board, current.depth + 1)
                dfs(child, visited, goal, n)



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

    goal = [[(i * n + j + 1) % (n * n) for j in range(n)] for i in range(n)]

    print("\nInitial board:")
    for row in board:
        print(*row)
    print("\nGoal board:")
    for row in goal:
        print(*row)

    # Solvability check
    if not is_solvable(board, n):
        print("\nThis puzzle configuration is UNSOLVABLE.")
        return

    start_state = State(None, board, 0)
    visited = set()

    dfs(start_state, visited, goal, n)
    print("No solution found.")


if __name__ == "__main__":
    main()
