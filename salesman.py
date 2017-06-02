#!/usr/bin/env python3

import math
import itertools


class Vector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)


nodes = []
with open('datasets/salesman.txt') as file:
    n = int(file.readline())

    for line in file.readlines():
        x, y = map(int, line.split())

        nodes.append(Vector(x, y))


min_path = []
min_len = math.inf
for path in itertools.permutations(nodes):
    l = 0
    for i in range(len(path)):
        l += (path[i] - path[i-1]).length()

    if l < min_len:
        min_len = l
        min_path = path

print('Кратчайший путь:', ' -> '.join(str(node) for node in min_path) + ' -> ' + str(min_path[0]))
print('Длина пути:', min_len)
