"""
find all the paths. how to fully traverse a graph?

graph is made up of nodes
first node is "start"
nodes are either large or small
small nodes cannot be visited more than once
large nodes can be visited any number of times
find all the possible paths

rules:

- don't go back to start
- path ends at end

"""
from collections import defaultdict

from rich import print

input = """\
start-A
start-b
A-c
A-b
b-d
A-end
b-end"""

input = """\
dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc"""

input = """\
fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW"""

input = """\
ma-start
YZ-rv
MP-rv
vc-MP
QD-kj
rv-kj
ma-rv
YZ-zd
UB-rv
MP-xe
start-MP
zd-end
ma-UB
ma-MP
UB-xe
end-UB
ju-MP
ma-xe
zd-UB
start-xe
YZ-end"""

graph = defaultdict(set)
for line in input.splitlines():
    node1, node2 = line.split("-")
    graph[node1].add(node2)
    graph[node2].add(node1)

# print(graph)


def traverse_graph():
    # always start at start
    paths = []
    node_stack = [(["start"], n) for n in graph["start"]]

    while len(node_stack) > 0:
        path, node = node_stack.pop()
        path.append(node)

        if node == "end":
            paths.append(path)
            continue

        new_nodes = graph[node].copy()

        # we don't go back to start
        new_nodes -= {"start"}

        rem_nodes = set()
        for n in path:
            if n.islower() and path.count(n) == 2:
                rem_nodes.add(n)
                break

        new_nodes -= rem_nodes

        # the rest we only visit once now
        if rem_nodes:
            rem_nodes = set(n for n in new_nodes if n in path and n.islower())
            new_nodes -= rem_nodes

        if len(new_nodes) == 0:
            continue

        for n in new_nodes:
            node_stack.append((path.copy(), n))

    return paths


paths = traverse_graph()
# print(sorted(paths))
# print(len(paths))


paths_visit_small = sum([any(n.islower() for n in path) for path in paths])
print(paths_visit_small)
