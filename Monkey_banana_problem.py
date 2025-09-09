

from collections import deque

def print_plan(path):
    for step, action in enumerate(path):
        print(f"{step:2d}. {action}")

def neighbors(state, banana_loc, locations):
    monkey, box, on_box, has = state

    # If monkey already has banana, no further moves
    if has:
        return []

    result = []

    # 1) Move monkey to any other location (only if not on box)
    if not on_box:
        for loc in locations:
            if loc != monkey:
                new = (loc, box, 0, has)
                result.append((new, f"move monkey from {monkey} -> {loc}"))

    # 2) Push box (monkey and box move together) : monkey must be at box and not on box
    if not on_box and monkey == box:
        for loc in locations:
            if loc != box:
                new = (loc, loc, 0, has)   # monkey and box both at loc
                result.append((new, f"push box from {box} -> {loc}"))

    # 3) Climb ONTO the box (must be at same location and not already on box)
    if not on_box and monkey == box:
        new = (monkey, box, 1, has)
        result.append((new, f"climb on box at {box}"))

    # 4) Climb DOWN from the box (if currently on it)
    if on_box:
        new = (monkey, box, 0, has)
        result.append((new, f"climb down from box at {box}"))

    # 5) Take banana (if on box and box is at banana location)
    if on_box and box == banana_loc:
        new = (monkey, box, on_box, 1)
        result.append((new, f"take banana at {banana_loc}"))

    return result

def bfs(start, banana_loc, locations):
    q = deque([start])
    parent = {start: (None, None)}   # state -> (prev_state, action)
    while q:
        cur = q.popleft()
        monkey, box, on_box, has = cur

        if has:  # goal reached
            # reconstruct path
            path = []
            s = cur
            while s is not None:
                prev, act = parent[s]
                path.append((s, act))
                s = prev
            path.reverse()
            # produce readable actions only (skip initial state's None action)
            actions = [f"Start: monkey={path[0][0][0]}, box={path[0][0][1]}" ]
            for st, act in path[1:]:
                actions.append(act)
            return actions

        for nxt, act in neighbors(cur, banana_loc, locations):
            if nxt not in parent:
                parent[nxt] = (cur, act)
                q.append(nxt)

    return None

if __name__ == "__main__":
    # Example setup (classic): monkey at A, box at C, banana hanging at B
    locations = ['A', 'B', 'C']          # can be any labels
    start = ('A', 'C', 0, 0)             # monkey_pos, box_pos, on_box(0/1), has_banana(0/1)
    banana_loc = 'B'

    print("Monkey & Banana (simple BFS solver)\n")
    print("Locations:", locations)
    print("Start: monkey at A, box at C, banana at B (hanging). Goal: monkey has banana.\n")

    plan = bfs(start, banana_loc, locations)
    if plan:
        print("Plan found (steps):\n")
        print_plan(plan)
    else:
        print("No plan found.")
