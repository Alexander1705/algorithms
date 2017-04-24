import math
from functools import reduce
from operator import mul


def prod(s):
    return reduce(mul, s, 1)


class LagrangePolynomial(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def l(self, i, x):
        k = len(self.x)
        return prod(
            (x - self.x[j]) / (self.x[i] - self.x[j])
            for j in range(k) if j != i
        )

    def __call__(self, x):
        k = len(self.x)

        return sum(self.y[i] * self.l(i, x) for i in range(k))


class NewtonPolynomials(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.h = x[1] - x[0]

        self.n = len(self.x) - 1
        self.dy = []
        self.dy.append([])
        for i in range(self.n + 1):
            self.dy[0].append(y[i])
        for k in range(1, self.n + 1):
            self.dy.append([])
            for i in range(self.n - k):
                self.dy[k].append(self.dy[k-1][i+1] - self.dy[k-1][i])

    def a(self, i):
        return self.dy[i][0] / (math.factorial(i) * self.h ** i)

    def __call__(self, x):
        t = (x - self.x[0]) / self.h
        s = 0
        q = 1
        for i in range(self.n):
            s += q * self.dy[i][0] / math.factorial(i)
            q *= t
            t -= 1
        return s


if __name__ == '__main__':
    from math import sin, cos
    import matplotlib.pyplot as plt

    group = 63
    variant = 19

    a = 3
    step = 2

    if variant <= 10:
        def f(x):
            return sin(a * x / 2) + (a * x) ** (1 / 3)


        k = variant - 1
        start = -5 + k
        stop = 3 + k

    elif variant <= 20:
        def f(x):
            return 0.5 * x * cos(a * x)

        k = 7
        start = 1
        stop = 9

    else:
        def f(x):
            return x ** 2 / 15 + cos(x + a)

        k = 2 * (variant - 21)
        start = -6 + k
        stop = 2 + k

    nodes = list(range(start, stop + 1, step))

    if variant % 2:
        P = LagrangePolynomial(nodes, list(map(f, nodes)))
    else:
        P = NewtonPolynomials(nodes, list(map(f, nodes)))

    X = [start + i * (stop - start) / 100 for i in range(101)]

    exact = list(map(f, X))
    polynom = list(map(P, X))

    print(polynom)

    plt.plot(X, exact)
    plt.plot(X, polynom)
    plt.savefig('output/polynom.png')
