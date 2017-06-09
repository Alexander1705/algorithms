import networkx as nx

filename = 'datasets/' + input('Graph file: ') + '.txt'

graph = nx.DiGraph()

with open(filename) as file:
    n, m = map(int, file.readline().split())

    for line in file.readlines():
        u, v, c = map(int, line.split())
        graph.add_edge(u, v, capacity=c)


s = int(input('Исток: '))
t = int(input('Сток:  '))
flow = nx.maximum_flow(graph, s, t)

print('Максимальный поток: ', flow[0])

for u, d in flow[1].items():
    for v, f in d.items():
        print('Поток из {} в {}: {}'.format(u, v, f))
