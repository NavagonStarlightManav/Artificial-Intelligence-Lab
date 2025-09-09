Monkey & Banana Problem — BFS Solution (Python)

This project implements the classic AI planning problem "Monkey and Banana" using a simple Breadth-First Search (BFS) approach.

The monkey wants to reach the banana hanging from the ceiling.
However, the monkey can only grab the banana if it stands on a box placed under the banana.

This program models monkey movement, box pushing, climbing actions, and finally grabbing the banana — producing the shortest sequence of steps.

The code is intentionally made easy, simple, and minimal for students

BFS(start):
    queue ← [start]
    parent[start] ← (None, None)

    while queue not empty:
        cur ← pop

        if cur.has_banana:
            return reconstruct_path(cur)

        for each action producing next_state:
            if next_state not visited:
                parent[next_state] ← (cur, action)
                queue.push(next_state)

    return failure
