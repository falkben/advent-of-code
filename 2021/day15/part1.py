import networkx as nx
from rich import print

input = """\
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""

with open("2021/day15/data.txt") as fh:
    input = fh.read()

lines = len(input.splitlines())
chars = len(input.splitlines()[0])


def get_adjacent(x, y):
    yield (x + 1, y)
    yield (x - 1, y)
    yield (x, y + 1)
    yield (x, y - 1)


data = {}
for y, line in enumerate(input.splitlines()):
    for x, char in enumerate(line):
        data[(x, y)] = int(char)


G = nx.Graph()
for y in range(lines):
    for x in range(chars):
        G.add_node((x, y))
        for x_a, y_a in get_adjacent(x, y):
            G.add_edge((x, y), (x_a, y_a), weight=data.get((x_a, y_a), 1e100))

# length = nx.dijkstra_path_length(G, (0, 0), (lines - 1, chars - 1), weight="weight")
length, path = nx.single_source_dijkstra(
    G, (0, 0), (lines - 1, chars - 1), weight="weight"
)
# length, path = nx.bidirectional_dijkstra(
#     G, (0, 0), (lines - 1, chars - 1), weight="weight"
# )

print(length)
# print(path)

ll = 0
for x, y in path:
    if (x, y) != (0, 0):
        ll += data[(x, y)]
print(f"{ll=}")


def print_data(data):
    for y in range(lines):
        line = ""
        for x in range(chars):
            if (x, y) in path:
                line += f"[white]{data[x,y]}[/white]"
            else:
                line += f"[grey37]{data[x,y]}[/grey37]"
        print(line)


print_data(data)
