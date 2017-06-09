import networkx as nx

filename = 'datasets/' + input('Граф: ') + '.txt'

graph = nx.Graph()

with open(filename) as file:
    n, m = map(int, file.readline().split())

    for line in file.readlines():
        u, v, w = line.split()
        graph.add_edge(u, v, weight=int(w))

sp = nx.Graph()
sp.add_node('A')

while True:
    minw = 1000
    mine = None
    for u, v in graph.edges():
        if (u in sp.nodes()) != (v in sp.nodes()):
            w = graph.get_edge_data(u, v)['weight']
            if w < minw:
                minw = w
                mine = (u, v)

    if not mine:
        break
    else:
        sp.add_edge(mine[0], mine[1])
        graph.remove_edge(mine[0], mine[1])


print('Минимальное остовное дерево:')
for e in sp.edges():
    print('\t{} - {}'.format(e[0], e[1]))
