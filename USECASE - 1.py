# A* Map Navigation using Euclidean heuristic
import heapq
import math

# Coordinates (x, y) for nodes on a simple road map
coords = {
    'S': (0, 0),
    'A': (2, 1),
    'B': (2, -1),
    'C': (4, 0),
    'D': (6, 1),
    'E': (6, -1),
    'G': (8, 0)  # Goal
}

# Undirected connectivity (roads); edge cost = Euclidean distance between endpoints
neighbors = {
    'S': ['A', 'B'],
    'A': ['S', 'C'],
    'B': ['S', 'C'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['C', 'G'],
    'E': ['C', 'G'],
    'G': ['D', 'E']
}

def euclidean(u, v):
    ux, uy = coords[u]
    vx, vy = coords[v]
    return math.hypot(ux - vx, uy - vy)

def heuristic(n, goal):
    return euclidean(n, goal)

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path

def astar(neighbors, coords, start, goal):
    open_heap = []
    counter = 0  # tie-breaker
    g = {node: float('inf') for node in neighbors}
    came_from = {}

    g[start] = 0.0
    heapq.heappush(open_heap, (heuristic(start, goal), counter, start))

    closed = set()

    while open_heap:
        _, _, current = heapq.heappop(open_heap)
        if current in closed:
            continue
        closed.add(current)

        if current == goal:
            return reconstruct_path(came_from, current), g[goal]

        for nb in neighbors[current]:
            tentative_g = g[current] + euclidean(current, nb)
            if tentative_g < g.get(nb, float('inf')):
                came_from[nb] = current
                g[nb] = tentative_g
                counter += 1
                f = tentative_g + heuristic(nb, goal)
                heapq.heappush(open_heap, (f, counter, nb))

    return None, float('inf')

if __name__ == "__main__":
    path, cost = astar(neighbors, coords, start='S', goal='G')
    if path:
        print("Path:", " -> ".join(path))
        print(f"Total distance: {cost:.3f}")
    else:
        print("No path found.")
