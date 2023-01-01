from collections import defaultdict
from queue import PriorityQueue

input = """\
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
"""
input = open("2022/day12/data.txt").read()


def get_adjacent(x, y):
    yield (x + 1, y)
    yield (x - 1, y)
    yield (x, y + 1)
    yield (x, y - 1)


nodes = defaultdict(lambda: float("inf"))
for y, line in enumerate(input.splitlines()):
    for x, char in enumerate(line):
        if char == "S":
            start = (x, y)
            nodes[(x, y)] = ord("a")
        elif char == "E":
            end = (x, y)
            nodes[(x, y)] = ord("z")
        else:
            nodes[(x, y)] = ord(char)

# create a graph from the nodes
G = {}
for pos, height in list(nodes.items()):
    # can be at most one higher, otherwise blocked, e.g. m -> n is okay, but m -> o is blocked
    # edges are all equal
    x, y = pos
    conn_nodes = set()
    for x_a, y_a in get_adjacent(*pos):
        if nodes[(x_a, y_a)] <= height + 1:
            conn_nodes.add((x_a, y_a))
    G[pos] = conn_nodes


def dijkstra(G, start, end):
    # where cost is always 1
    visited = set()
    cost = {start: 0}
    parent = {start: None}
    todo = PriorityQueue()
    todo.put((0, start))

    while todo:
        while not todo.empty():
            _, vert = todo.get()  # finds lowest cost vertex
            # loop until we get a fresh vertex
            if vert not in visited:
                break
        else:  # if todo ran out
            break  # quit main loop

        visited.add(vert)

        if vert == end:
            break

        for neighbor in G[vert]:
            if neighbor in visited:
                continue
            old_cost = cost.get(neighbor, float("inf"))
            new_cost = cost[vert] + 1
            if new_cost < old_cost:
                todo.put((new_cost, neighbor))
                cost[neighbor] = new_cost
                parent[neighbor] = vert

    return parent


# need to traverse parent to get the path
def make_path(parent, end):
    if end not in parent:
        return None
    v = end
    path = []
    while v is not None:  # root has null parent
        path.append(v)
        v = parent[v]
    return path[::-1]


parent = dijkstra(G, start, end)
path = make_path(parent, end)
print(len(path) - 1)
