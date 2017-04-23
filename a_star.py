#!/usr/bin/env python3
import math

import sys

from priorityqueue import PriorityQueue


class Cell(object):
    def __init__(self, passable):
        self.char = ' ' if passable else 'X'
        self.passable = passable
        self.distance = math.inf


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


def read_matrix(file):
    return [
        [Cell(line[i] != 'X') for i in range(0, len(line), 2)]
        for line in file
    ]


def print_matrix(file, matrix):
    s = ''
    for line in matrix:
        for cell in line:
            s += cell.char + ' '
        s += '\n'
    print(s, file=file)


def manhattan_distance(a, b):
    return abs(a.x - b.x) + abs(a.y - b.y)


def a_star(matrix, start, target):
    alphabet = 'abcdefghijklmnopqrstuvwxyz' * 100
    directions = '↓↑→←'
    pq = PriorityQueue()
    pq.insert(0, start)
    matrix[start.x][start.y].distance = 0

    while pq:
        curr = pq.pop()
        # matrix[curr.x][curr.y].char = alphabet[matrix[curr.x][curr.y].distance]

        if curr == target:
            break

        neighbours = [Point(curr.x - 1, curr.y), Point(curr.x + 1, curr.y), Point(curr.x, curr.y - 1), Point(curr.x, curr.y + 1)]
        for next, d in zip(neighbours, directions):
            if not matrix[next.x][next.y].passable:
                continue

            cost = matrix[curr.x][curr.y].distance + 1

            if cost < matrix[next.x][next.y].distance:
                matrix[next.x][next.y].distance = cost
                priority = cost + manhattan_distance(next, target)
                pq.insert(priority, next)
                matrix[next.x][next.y].char = d

        print_matrix(sys.stdout, matrix)
        input()

    print_matrix(sys.stdout, matrix)


if __name__ == '__main__':
    filename = input('Maze file: ')

    with open('datasets/' + filename) as file:
        m = read_matrix(file)

    start = Point(*map(int, input('Start: ').split()))
    target = Point(*map(int, input('Target: ').split()))

    a_star(m, start, target)
