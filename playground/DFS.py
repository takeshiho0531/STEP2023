from collections import deque


def DFS(start, goal, links: dict):
    stack = deque([])
    visited = {}
    visited[start] = True
    stack.append(start)
    while len(stack) != 0:
        node = stack.pop()
        visited[node] = True
        if node == goal:
            return "found!"
        for child in links[node]:
            if not child in visited:
                stack.append(child)
    return "not found!"
