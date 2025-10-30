# maze_bfs_visual.py
# Maze Solver using BFS (Breadth-First Search)
# Displays the result visually in a new window using Matplotlib

from collections import deque
import matplotlib.pyplot as plt
import numpy as np

# --- Define Maze ---
# 0 = free cell, 1 = wall
maze = [
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 0],
    [0, 0, 0, 1, 0, 0],
    [1, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0],
]

start = (0, 0)   # (row, col)
goal = (4, 5)

# --- BFS Algorithm ---
def bfs(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    queue = deque([(start, [start])])
    visited = {start}
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        (r, c), path = queue.popleft()
        if (r, c) == goal:
            return path

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if maze[nr][nc] == 0 and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append(((nr, nc), path + [(nr, nc)]))
    return None

# --- Visualization Function ---
def visualize_maze(maze, path=None):
    arr = np.array(maze)
    plt.figure(figsize=(6, 6))
    plt.imshow(arr, cmap="gray_r", origin="upper")

    if path:
        xs = [p[1] for p in path]
        ys = [p[0] for p in path]
        plt.plot(xs, ys, "-o", color="red", label="BFS Path")
        plt.scatter(xs[0], ys[0], c="green", s=150, label="Start")
        plt.scatter(xs[-1], ys[-1], c="blue", s=150, label="Goal")

    plt.title("Maze Path using BFS")
    plt.legend()
    plt.axis("off")
    plt.show()

# --- Main Program ---
if __name__ == "__main__":
    print("Finding path using BFS...")
    path = bfs(maze, start, goal)

    if path:
        print("Path found! Length:", len(path))
        print("Path:", path)
    else:
        print("No path found!")

    visualize_maze(maze, path)
