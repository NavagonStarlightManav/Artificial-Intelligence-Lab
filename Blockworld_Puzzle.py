# blocks_world.py
# Simple Blocks World solver using BFS (shortest sequence of moves)
# Representation: state = tuple of stacks; each stack is a tuple of blocks (bottom -> top)

from collections import deque

def normalize_input_line(s):
    # user types stack as letters bottom->top, or "-" for empty
    s = s.strip()
    return tuple(s) if s != "-" and s != "" else tuple()

def state_to_key(state):
    # convert state (tuple of tuples) to an immutable key (already immutable) - returned directly
    return state

def neighbors(state):
    # yield (new_state, description) for every legal move: top of stack i -> stack j (i != j)
    n = len(state)
    for i in range(n):
        if len(state[i]) == 0:
            continue
        for j in range(n):
            if i == j:
                continue
            # move top from i to j
            src = list(state[i])
            dest = list(state[j])
            block = src.pop()           # top block
            dest.append(block)
            new_state = list(state)
            new_state[i] = tuple(src)
            new_state[j] = tuple(dest)
            move_desc = f"move {block} from stack {i} -> stack {j}"
            yield tuple(new_state), move_desc

def bfs(start, goal):
    q = deque()
    q.append(start)
    parent = { state_to_key(start): (None, None) }  # key -> (prev_state, move_description)
    while q:
        cur = q.popleft()
        if cur == goal:
            # reconstruct path
            path = []
            s = cur
            while True:
                prev, mv = parent[state_to_key(s)]
                path.append((s, mv))
                if prev is None:
                    break
                s = prev
            path.reverse()
            return path
        for nxt, mv in neighbors(cur):
            k = state_to_key(nxt)
            if k not in parent:
                parent[k] = (cur, mv)
                q.append(nxt)
    return None

if __name__ == "__main__":
    print("Blocks World solver (simple BFS).")
    p = int(input("Enter number of stacks (p): ").strip())

    print("\nEnter initial stacks one per line (bottom->top).")
    print("Example: 'AB' means A bottom, B top. Use '-' or empty line for an empty stack.")
    start_stacks = []
    for i in range(p):
        line = input(f"Initial stack {i}: ")
        start_stacks.append(normalize_input_line(line))
    start = tuple(start_stacks)

    print("\nEnter goal stacks in same format:")
    goal_stacks = []
    for i in range(p):
        line = input(f"Goal stack {i}: ")
        goal_stacks.append(normalize_input_line(line))
    goal = tuple(goal_stacks)

    print("\nSolving... (this finds shortest move sequence)\n")
    result = bfs(start, goal)

    if not result:
        print("No solution found.")
    else:
        print(f"Solution found in {len(result)-1} moves:\n")
        step = 0
        for state, mv in result:
            print(f"Step {step}:")
            for idx, st in enumerate(state):
                print(f"  Stack {idx}: {''.join(st) if st else '-'}")
            if mv:
                print("  ->", mv)
            print()
            step += 1
