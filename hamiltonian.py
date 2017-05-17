import networkx as nx
from itertools import permutations

filename = 'datasets/' + input('Graph file: ') + '.graph'

graph = nx.DiGraph()

with open(filename) as file:
    n, m = map(int, file.readline().split())

    for line in file.readlines():
        u, v = map(int, line.split())
        graph.add_edge(u, v)

ways = []
circuits = []

for path in permutations(graph.nodes()):
    f = False
    for i in range(len(path) - 1):
        if not graph.has_edge(path[i], path[i+1]):
            f = True
            break

    if f:
        continue

    ways.append(path)

    if graph.has_edge(path[-1], path[0]):
        circuits.append(path)
        break

if circuits:
    print('G is Hamiltonian')
    print(circuits[0])
elif ways:
    print('G is semi-Hamiltonian')
    print(ways[0])
else:
    print('G is not Hamiltonian')
