#Q14. Shortest path with a queue (BFS). Given the graph {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": ["E"], "E": []}, find the number of steps from A to E (answer: 3). Use a queue and a seen set so you never visit a node twice.

from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D"],
    "D": ["E"],
    "E": []
}


def shortest_path(graph, start, target):

    queue = deque([(start, 0)])

    seen = {start}

    while queue:

        node, steps = queue.popleft()

        if node == target:
            return steps

        for neighbor in graph[node]:

            if neighbor not in seen:

                seen.add(neighbor)

                queue.append((neighbor, steps + 1))

    return -1


print("Shortest distance:", shortest_path(graph, "A", "E"))
