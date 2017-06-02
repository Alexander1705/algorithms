#!/usr/bin/env python3

from collections import defaultdict

filename = 'datasets/' + input('Название графа: ') + '.txt'

rang = defaultdict(int)
count = defaultdict(int)

with open(filename) as file:
    for line in file.readlines():
        a, b = map(int, line.split())

        rang[a] += 1
        rang[b] += 1

for i in range(len(rang)):
    count[rang[i]] += 1

for i in range(len(rang)-2, -1, -1):
    count[i] += count[i+1]

if count[2] > 5 or count[3] > 4:
    print('Граф НЕ планарний')
else:
    print('Граф планарний')
