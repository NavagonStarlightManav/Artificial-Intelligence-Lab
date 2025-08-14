from copy import deepcopy
import sys


class State:
    def __init__(self, parent, state_array, state_no):
        self.parent = parent
        self.state_array = state_array
        self.state_no = state_no



row_moves = [0, 0, -1, 1]
col_moves = [-1, 1, 0, 0]



def get_puzzle(n):
    puzzle = []
    state_i = state_y = 0
    for i in range(n):
        row = []
        for j in range(n):
            val = int(input(f"Enter number on index ({i} {j}) : "))
            row.append(val)
            if val == 0:
                state_i, state_y = i, j
        puzzle.append(row)
    return puzzle, state_i, state_y



def is_valid(x, y, n):
    return 0 <= x < n and 0 <= y < n



def is_goal(goal, state):
    return goal == state



def print_path(s, n, count):
    if s is None:
        return count
    count = print_path(s.parent, n, count)
    count += 1
    for i in range(n):
        for j in range(n):
            print(s.state_array[i][j], end=" ")
        print()
    print("----")
    return count


# Copy board (deepcopy equivalent)
def copy_board(src):
    return deepcopy(src)


# Check if already visited
def is_visited(visited, board):
    return board in visited


# Calculate displaced tile count heuristic
def displaced_count(s, n):
    count = 0
    num = 1
    for i in range(n):
        for j in range(n):
            # Do not count the blank tile (0)
            if s.state_array[i][j] != 0 and s.state_array[i][j] != num:
                count += 1
            num += 1
    return count



def get_state(s, visited, n, goal):
    stack = []
    stack.append(s)
    visited.append(s.state_array)

    disp_count = sys.maxsize  # INT_MAX
    to_push = None

    while stack:
        temp = stack.pop()

        # Goal check
        if is_goal(goal, temp.state_array):
            count = 0
            count = print_path(temp, n, count)
            print("Count :", count)
            return

        # Find blank position (0)
        blankX = blankY = 0
        for i in range(n):
            for j in range(n):
                if temp.state_array[i][j] == 0:
                    blankX, blankY = i, j

        # Try all 4 possible moves
        for i in range(4):
            newX = blankX + row_moves[i]
            newY = blankY + col_moves[i]

            if is_valid(newX, newY, n):
                new_board = copy_board(temp.state_array)
                # Swap blank and target
                new_board[blankX][blankY], new_board[newX][newY] = (
                    new_board[newX][newY],
                    new_board[blankX][blankY],
                )

                # If not visited yet
                if not is_visited(visited, new_board):
                    child = State(temp, new_board, temp.state_no + 1)
                    visited.append(new_board)
                    c = displaced_count(child, n)

                    # Keep the one with the lowest displaced count
                    if disp_count > c:
                        disp_count = c
                        to_push = child

        # Push the best next state
        if to_push:
            stack.append(to_push)


if __name__ == "__main__":
    n = int(input("Enter size : "))
    puzzle, x, y = get_puzzle(n)
    print("X and Y:", x, y)

    # Create goal state
    goal = []
    num = 1
    for i in range(n):
        row = []
        for j in range(n):
            row.append(num)
            num += 1
        goal.append(row)
    goal[n - 1][n - 1] = 0

    s1 = State(None, puzzle, 0)
    print("Given state :")

    visited = []
    get_state(s1, visited, n, goal)
