import networkx as nx

filename = 'datasets/' + input('Graph file: ') + '.graph'

graph = nx.DiGraph()

with open(filename) as file:
    n, m = map(int, file.readline().split())

    for line in file.readlines():
        u, v = map(int, line.split())
        graph.add_edge(u, v)

try:
    circuit = list(nx.eulerian_circuit(graph))
    print('G is Eulerian')
    print(' -> '.join(str(e[0]) for e in circuit))

except nx.NetworkXError as e:
    try:
        a, b = filter(lambda node: nx.degree(graph, node) & 1, graph.nodes())
    except ValueError:
        print('G is neither Eulerian nor semi-Eulerian')
    else:
        print('G is semi-Eulerian')
        try:
            graph.add_edge(a, b)
            path = list(nx.eulerian_circuit(graph))
            path.remove((a, b))
            print(' -> '.join(str(e[0]) for e in path))
        except nx.NetworkXError:
            try:
                graph.remove_edge(a, b)
                graph.add_edge(b, a)
                path = list(nx.eulerian_circuit(graph))
                path.remove((b, a))
                print(' -> '.join(str(e[0]) for e in path))

            except nx.NetworkXError:
                print('G is not Eulerian')

