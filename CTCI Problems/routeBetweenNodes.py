"""
Route Between Nodes: Given a directed graph, design an algorithm to find out whether there is a
route between two nodes.
CTCI, pg 109
"""


def route(start, goal, graph):
    stack = [start]
    visited = set()
    visited.add(start)

    while stack:
        node = stack.pop()
        if node == goal:
            print(visited)
            return True
        for adjacent in graph[node]:
            if adjacent not in visited:
                stack.append(adjacent)
                visited.add(adjacent)
    return False


g = {1: [2, 3], 2: [3, 5], 3: [1, 4], 4: [], 5: [2]}
print(route(5, 1, g))