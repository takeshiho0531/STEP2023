from collections import deque


def BFS(start, goal, links: dict):
    queue = deque([])
    visited = {}
    queue.append(start)
    visited[start] = True

    while len(queue) != 0:
        node = queue.popleft()
        visited[node] = True
        if node == goal:
            return "found!"
        for child in links[node]:
            if not child in links[node]:
                queue.append(child)
                visited[child] = True
    return "not found!"
