import heapq
import math
import itertools

class State:
    def __init__(self, parent, state_array, x, y):
        self.parent = parent
        self.state_array = state_array
        self.x = x
        self.y = y

def is_valid(x, y, n):
    return 0 <= x < n and 0 <= y < n

def is_goal(x, y, dest_x, dest_y):
    return x == dest_x and y == dest_y

def print_path(s):
    if s is None:
        return
    print_path(s.parent)
    print(f"({s.x}, {s.y})")

def copy_board(src):
    return [row[:] for row in src]

def manhattan_dist(x, y, dest_x, dest_y):
    return abs(x - dest_x) + abs(y - dest_y)

def get_state(s, n, dest_x, dest_y):
    row_moves = [0, 0, -1, 1]
    col_moves = [-1, 1, 0, 0]
    pq = []
    counter = itertools.count()
    heapq.heappush(pq, (s.state_array[s.x][s.y][0] + s.state_array[s.x][s.y][1],
                        next(counter), s))
    visited = [[False for _ in range(n)] for _ in range(n)]
    while pq:
        _, _, current = heapq.heappop(pq)
        if visited[current.x][current.y]:
            continue
        visited[current.x][current.y] = True
        if is_goal(current.x, current.y, dest_x, dest_y):
            print("\nPath found:")
            print_path(current)
            return
        for i in range(4):
            new_x = current.x + row_moves[i]
            new_y = current.y + col_moves[i]
            if is_valid(new_x, new_y, n):
                if current.state_array[new_x][new_y][1] == math.inf:
                    continue
                new_board = copy_board(current.state_array)
                g_new = current.state_array[current.x][current.y][0] + 1
                h_new = manhattan_dist(new_x, new_y, dest_x, dest_y)
                new_board[new_x][new_y] = (g_new, h_new)
                child = State(current, new_board, new_x, new_y)
                f_val = g_new + h_new
                heapq.heappush(pq, (f_val, next(counter), child))
    print("No solution found!")

def main():
    n = int(input("Enter grid size (n): "))
    grid = [[(math.inf, 0) for _ in range(n)] for _ in range(n)]
    i, j = map(int, input("Enter source (x y): ").split())
    grid[i][j] = (0, 0)
    dest_i, dest_j = map(int, input("Enter destination (x y): ").split())
    grid[dest_i][dest_j] = (grid[dest_i][dest_j][0], 0)
    print("Enter indices with water (obstacles):")
    while True:
        x, y = map(int, input("Enter water cell (x y): ").split())
        if is_valid(x, y, n):
            grid[x][y] = (math.inf, math.inf)
        ch = input("Do you want to enter more water cells? (y/n): ").lower()
        if ch != 'y':
            break
    for a in range(n):
        for b in range(n):
            if grid[a][b][1] != math.inf:
                grid[a][b] = (grid[a][b][0], manhattan_dist(a, b, dest_i, dest_j))
    s1 = State(None, grid, i, j)
    get_state(s1, n, dest_i, dest_j)

if __name__ == "__main__":
    main()
