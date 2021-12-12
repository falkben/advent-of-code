from collections import defaultdict

input = """\
start-A
start-b
A-c
A-b
b-d
A-end
b-end"""


graph = defaultdict(set)
for line in input.splitlines():
    node1, node2 = line.split("-")
    graph[node1].add(node2)
    graph[node2].add(node1)

print(graph)


def traverse_graph():
    # first node is "start"
    # keep in history nodes you've visited
    # capital letters can be visited any number of times
    # lowercase letters only once

    nodes = graph["start"]

    path = []
    for node in nodes:

        ...
