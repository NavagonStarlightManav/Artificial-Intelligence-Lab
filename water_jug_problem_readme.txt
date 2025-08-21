Water Jug Problem Solver Using Depth-First Search (DFS)

This program solves the classic Water Jug Problem using the Depth-First Search (DFS) strategy.
Given two jugs of capacities X and Y, the goal is to measure exactly T liters of water in one of the jugs.

The algorithm recursively explores all possible jug operations and uses a visited set to avoid infinite loops.

DFS(j1, j2):
    if (j1,j2) in visited:
        return False
    add to visited
    add to path
    if goal state reached:
        return True

    try all 6 operations recursively
    if any returns True:
        return True

    remove from path (backtrack)
    return False
