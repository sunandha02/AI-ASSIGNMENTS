import heapq
import math


directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
              (-1, -1), (-1, 1), (1, -1), (1, 1)]


def heuristic(x, y, goal):
    return math.sqrt((x - goal[0])**2 + (y - goal[1])**2)


def best_first_search(grid):
    n = len(grid)
    if grid[0][0] != 0 or grid[n-1][n-1] != 0:
        return -1, []

    pq = [(heuristic(0, 0, (n-1, n-1)), (0, 0), [(0, 0)])]  # (heuristic, node, path)
    visited = set([(0, 0)])

    while pq:
        _, (x, y), path = heapq.heappop(pq)
        if (x, y) == (n-1, n-1):
            return len(path), path
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0 and (nx, ny) not in visited:
                visited.add((nx, ny))
                heapq.heappush(pq, (heuristic(nx, ny, (n-1, n-1)), (nx, ny), path + [(nx, ny)]))
    return -1, []


def a_star_search(grid):
    n = len(grid)
    if grid[0][0] != 0 or grid[n-1][n-1] != 0:
        return -1, []

    pq = [(heuristic(0, 0, (n-1, n-1)), 0, (0, 0), [(0, 0)])]  # (f = g+h, g, node, path)
    visited = set()

    while pq:
        f, g, (x, y), path = heapq.heappop(pq)
        if (x, y) == (n-1, n-1):
            return len(path), path
        if (x, y) in visited:
            continue
        visited.add((x, y))
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0 and (nx, ny) not in visited:
                new_g = g + 1
                new_f = new_g + heuristic(nx, ny, (n-1, n-1))
                heapq.heappush(pq, (new_f, new_g, (nx, ny), path + [(nx, ny)]))
    return -1, []




n = int(input("Enter grid size n: "))
grid = []

print("Enter the grid row by row (0 for free cell, 1 for blocked cell):")
for _ in range(n):
    row = list(map(int, input().split()))
    grid.append(row)


bfs_len, bfs_path = best_first_search(grid)
a_len, a_path = a_star_search(grid)


print("\nResults:")

if bfs_len == -1:
    print("Best First Search  →  Path length: -1, No path exists")
else:
    print(f"Best First Search  →  Path length: {bfs_len}, Path: {bfs_path}")

if a_len == -1:
    print("A* Search          →  Path length: -1, No path exists")
else:
    print(f"A* Search          →  Path length: {a_len}, Path: {a_path}")
