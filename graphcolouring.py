#!/usr/bin/env python3

from collections import defaultdict
import itertools

itertools.accumulate


filename = 'datasets/' + input('Graph: ') + '.txt'

nodes = set()
graph = defaultdict(set)


with open(filename) as file:
    n, m = map(int, file.readline().split())

    for line in file.readlines():
        u, v = map(int, file.readline().split())

        nodes.add(u)
        nodes.add(v)

        graph[u].add(v)
        graph[v].add(u)


for k in range(2, len(nodes) + 2):


print('\n'.join('Node {}: {} colour'.format(n, c) for n, c in node_colours.items()))







