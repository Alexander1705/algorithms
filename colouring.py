#!/usr/bin/env python3
from os import path


class Graph:
    def __init__(self, directed=False):
        self.nodes_num = 0
        self.edges_num = 0
        self.directed = directed
        self.edges = list()
        self.nodes = list()
        self.graph_name = "default"
        self.adj_list = dict()
        self.reweighted = list()
        self.chromatic = -1
        self.coloring = dict()

    def read_from_file(self, filename="graph.txt"):
        self.graph_name = path.splitext(filename)[0]
        with open(filename) as f:
            temp = f.readline().split()
            self.nodes_num = int(temp[0])
            self.edges_num = int(temp[1])
            for i in range(self.edges_num):
                temp = f.readline().split()
                if len(temp) == 3:
                    temp[2] = float(temp[2])
                self.edges.append(tuple(temp))
                for node in temp[0:2]:
                    if node not in self.nodes:
                        self.nodes.append(node)
            if len(self.nodes) != self.nodes_num:
                for i in range(self.nodes_num - len(self.nodes)):
                    self.nodes.append(f.readline().strip('\n'))
        self.nodes.sort()

    def draw(self):
        colors = ["red", "blue", "green", "yellow", "orange", "purple", "gray", "white", "black"]

        A = pgv.AGraph(directed=self.directed)
        A.add_edges_from(self.edges)
        for node in self.nodes:
            A.add_node(node, color=colors[self.coloring[node]])
        A.layout()
        filename = self.graph_name + ".png"
        A.draw(path=filename, format="png", prog="circo")

    def build_adjacency_list(self):
        for node in self.nodes:
            adjacent_nodes = list()
            for edge in self.edges:
                if edge[0] == node:
                    adjacent_nodes.append(edge[1])
                if not self.directed and edge[1] == node:
                    adjacent_nodes.append(edge[0])
            self.adj_list[node] = adjacent_nodes

    def rca(self, m, node: str, coloring: dict, colored: set, nodes: set):
        colors = list(range(m))
        for color in colors:
            valid = True
            for adj in self.adj_list[node]:
                if coloring[adj] == color:
                    valid = False
            if valid:
                coloring[node] = color
                colored.add(node)
                if len(colored) == self.nodes_num:
                    self.chromatic = m
                    self.coloring = coloring
                    return
                break
        if not nodes:
            return
        v = nodes.pop()
        self.rca(m, v, coloring, colored, nodes)

    def brute_coloring(self):
        self.build_adjacency_list()
        for m in range(1, self.nodes_num + 1):
            coloring = {node: -1 for node in self.nodes}
            colored = set()
            nodes = set(self.nodes)
            self.rca(m, self.nodes[0], coloring, colored, nodes)
            if self.chromatic != -1:
                break


def main():
    graph = Graph()
    graph.read_from_file('datasets/' + input('Граф: ') + '.txt')
    graph.brute_coloring()
    print("Хроматическое число: ", graph.chromatic)
    print('\n'.join('Вершина {}: цвет №{}'.format(n, c) for n, c in graph.coloring.items()))


if __name__ == '__main__':
    main()
