* Algorithm for Grid Pathfinding (with Manhattan Heuristic)

This program implements the A* search algorithm to find the shortest path from a source cell to a destination cell on an n × n grid, with water cells acting as obstacles.
A* uses both actual path cost (g) and heuristic estimate (h) to efficiently reach the destination.

The program prints the exact path from source → destination if one exists.

A*(start):
    pq ← [(f(start), start)]
    visited ← matrix(n,n)

    while pq not empty:
        current ← pop smallest f

        if current is goal:
            print_path(current)
            return

        mark current visited

        for each valid neighbor:
            if not water and not visited:
                compute g, h, f
                push neighbor in pq

    print "No solution found"
