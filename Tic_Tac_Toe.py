import sys
from copy import deepcopy

n = 3

class State:
    def __init__(self, parent, board, score, isMax, children=None):
        if children is None:
            children = []
        self.parent = parent
        self.board = board
        self.score = score
        self.isMax = isMax
        self.children = children


def moves_left(board):
    for i in range(n):
        for j in range(n):
            if board[i][j] == '_':
                return True
    return False


def get_score(board):
    # Rows
    for i in range(3):
        if board[i][0] != '_' and board[i][0] == board[i][1] == board[i][2]:
            return 1 if board[i][0] == 'X' else -1
        if board[0][i] != '_' and board[0][i] == board[1][i] == board[2][i]:
            return 1 if board[0][i] == 'X' else -1


    if board[0][0] != '_' and board[0][0] == board[1][1] == board[2][2]:
        return 1 if board[0][0] == 'X' else -1
    if board[0][2] != '_' and board[0][2] == board[1][1] == board[2][0]:
        return 1 if board[0][2] == 'X' else -1

    return 0

def print_board(board):
    print("\n")
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()
    print("\n")


def generate_tree(s):
    score = get_score(s.board)
    if score != 0:
        s.score = score
        return score

    if not moves_left(s.board):
        s.score = 0
        return 0

    if s.isMax:
        best = -sys.maxsize
        for i in range(n):
            for j in range(n):
                if s.board[i][j] == '_':
                    newBoard = deepcopy(s.board)
                    newBoard[i][j] = 'X'
                    child = State(s, newBoard, 0, False, [])
                    s.children.append(child)
                    best = max(best, generate_tree(child))
        s.score = best
        return best
    else:
        best = sys.maxsize
        for i in range(n):
            for j in range(n):
                if s.board[i][j] == '_':
                    newBoard = deepcopy(s.board)
                    newBoard[i][j] = 'O'
                    child = State(s, newBoard, 0, True, [])
                    s.children.append(child)
                    best = min(best, generate_tree(child))
        s.score = best
        return best



def best_computer_move(s):
    bestVal = -sys.maxsize
    bestChild = None
    for child in s.children:
        if child.score > bestVal:
            bestVal = child.score
            bestChild = child
    return bestChild


def play_game(root):
    current = root

    while True:
        print_board(current.board)
        score = get_score(current.board)

        if score == 1:
            print("Computer (X) wins!")
            break
        if score == -1:
            print("You (O) win!")
            break
        if not moves_left(current.board):
            print("It's a draw!")
            break


        try:
            x, y = map(int, input("Enter your move (row col, 0-indexed): ").split())
        except:
            print("Invalid input format. Try again.")
            continue

        if x < 0 or x >= n or y < 0 or y >= n or current.board[x][y] != '_':
            print("Invalid move. Try again.")
            continue


        nextState = None
        for child in current.children:
            if child.board[x][y] == 'O':
                nextState = child
                break

        if nextState is None:
            newBoard = deepcopy(current.board)
            newBoard[x][y] = 'O'
            nextState = State(current, newBoard, 0, True, [])
            generate_tree(nextState)
            current.children.append(nextState)

        current = nextState

        print_board(current.board)
        score = get_score(current.board)
        if score == -1:
            print("You (O) win!")
            break
        if not moves_left(current.board):
            print("It's a draw!")
            break

        # Computer move
        current = best_computer_move(current)
        print("Computer plays:")


if __name__ == "__main__":
    board = [
        ['_', '_', '_'],
        ['_', '_', '_'],
        ['_', '_', '_']
    ]

    # Root: X starts (computer)
    root = State(None, board, 0, True, [])
    generate_tree(root)
    play_game(root)
