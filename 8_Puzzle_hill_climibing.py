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


# -------- Validity check --------
def is_valid(x, y, n):
    return 0 <= x < n and 0 <= y < n


# -------- Goal check --------
def is_goal(goal, state):
    return goal == state


# -------- Print path recursively --------
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


# -------- Copy a board --------
def copy_board(src):
    return deepcopy(src)


# -------- Check if visited --------
def is_visited(visited, board):
    return board in visited


def displaced_count(s, n):
    count = 0
    num = 1
    for i in range(n):
        for j in range(n):
            if s.state_array[i][j] != 0 and s.state_array[i][j] != num:
                count += 1
            num += 1
    return count



def get_state(s, visited, n, goal):
    stack = []
    stack.append(s)
    visited.append(s.state_array)

    to_push = None
    peak = sys.maxsize  # equivalent of INT_MAX

    while stack:
        temp = stack.pop()

        # Check goal
        if is_goal(goal, temp.state_array):
            count = 0
            count = print_path(temp, n, count)
            print("Count :", count)
            sys.exit(0)

        # Find blank (0)
        blankX = blankY = 0
        for i in range(n):
            for j in range(n):
                if temp.state_array[i][j] == 0:
                    blankX, blankY = i, j

        disp_count = sys.maxsize
        flag = False

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

                if not is_visited(visited, new_board):
                    child = State(temp, new_board, temp.state_no + 1)
                    visited.append(new_board)
                    c = displaced_count(child, n)

                    # Choose better state (lower heuristic)
                    if disp_count > c and c < peak:
                        disp_count = c
                        peak = c
                        flag = True
                        to_push = child


        if flag:
            stack.append(to_push)
        else:
            print("Local maxima Reached !!")
            count = 0
            count = print_path(temp, n, count)
            print("Count :", count)
            sys.exit(0)


if __name__ == "__main__":
    n = int(input("Enter size : "))
    puzzle, x, y = get_puzzle(n)
    print("X and Y :", x, y)

    # Goal state
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
