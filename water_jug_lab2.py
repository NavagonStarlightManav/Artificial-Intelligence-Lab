
visited = set()          # set of visited states (jug1, jug2)
path = []                # list to store the solution path

def dfs(jug1, jug2):
    if (jug1, jug2) in visited:
        return False

    visited.add((jug1, jug2))
    path.append((jug1, jug2))

    # check target condition
    if (targetJug == 1 and jug1 == target) or (targetJug == 2 and jug2 == target):
        return True

    # Fill jug1
    if dfs(capacity1, jug2):
        return True

    # Fill jug2
    if dfs(jug1, capacity2):
        return True

    # Empty jug1
    if dfs(0, jug2):
        return True

    # Empty jug2
    if dfs(jug1, 0):
        return True

    # Pour jug1 -> jug2
    pour1to2 = min(jug1, capacity2 - jug2)
    if dfs(jug1 - pour1to2, jug2 + pour1to2):
        return True

    # Pour jug2 -> jug1
    pour2to1 = min(jug2, capacity1 - jug1)
    if dfs(jug1 + pour2to1, jug2 - pour2to1):
        return True

    # Backtrack
    path.pop()
    return False



if __name__ == "__main__":
    capacity1 = int(input("Enter capacity of jug X: "))
    capacity2 = int(input("Enter capacity of jug Y: "))
    target = int(input("Enter target amount of water: "))
    targetJug = int(input("In which jug do you want the target (1 for X, 2 for Y)? "))

    if dfs(0, 0):
        print("\nSolution steps:")
        for state in path:
            print(f"({state[0]}, {state[1]})")
    else:
        print("No solution found.")
