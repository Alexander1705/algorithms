class CubicSpline(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.npoints = len(x)
        self.nsplines = len(x) - 1

        self.h = [x[i+1] - x[i] for i in range(self.nsplines)]
        self.a = y
        self.c = self.solve_tdmatrix()

        self.d = [(self.c[i+1] - self.c[i]) / self.h[i] for i in range(self.nsplines)]
        self.b = [(self.a[i+1] - self.a[i]) / self.h[i] - (2*self.c[i] + self.c[i+1]) * self.h[i] / 6 for i in range(self.nsplines)]


    def solve_tdmatrix(self):
        f = [6 * ((self.a[i+1] - self.a[i]) / self.h[i] - (self.a[i] - self.a[i-1]) / self.h[i-1])
             for i in range(1, self.nsplines)]

        l = [self.h[i] for i in range(1, self.nsplines - 1)]
        u = [self.h[i] for i in range(1, self.nsplines - 1)]
        d = [2 * (self.h[i] + self.h[i+1]) for i in range(self.nsplines - 1)]

        # Make upper triangle matrix:
        for i in range(self.nsplines-2):
            f[i] /= d[i]
            u[i] /= d[i]
            d[i] = 1

            d[i+1] -= u[i] * l[i]
            f[i+1] -= f[i] * l[i]
            l[i] = 0

        f[-1] /= d[-1]
        d[-1] = 1

        for i in range(self.nsplines-2, 0, -1):
            f[i-1] -= f[i] * u[i-1]
            u[i-1] = 0

        return [0] + f + [0]

    def __call__(self, x):
        beg, end = 0, self.nsplines
        while beg != end:
            mid = (beg + end) // 2

            if x < self.x[mid]:
                end = mid
            elif mid != self.nsplines - 1 and x > self.x[mid+1]:
                beg = mid
            else:
                break

        return self.a[mid] + \
               self.b[mid] * (x - self.x[mid]) + \
               self.c[mid] * (x - self.x[mid]) ** 2 / 2 + \
               self.d[mid] * (x - self.x[mid]) ** 3 / 6


if __name__ == '__main__':
    from math import sin, cos
    import matplotlib.pyplot as plt

    group = 63
    variant = 18

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

        k = variant - 11
        start = -6 + k
        stop = 2 + k

    else:
        def f(x):
            return x ** 2 / 15 + cos(x + a)

        k = 2 * (variant - 21)
        start = -6 + k
        stop = 2 + k

    nodes = list(range(start, stop + 1, step))

    cs = CubicSpline(nodes, list(map(f, nodes)))

    X = [start + i * (stop - start) / 100 for i in range(101)]

    exact = list(map(f, X))
    polynom = list(map(cs, X))

    for i in range(cs.nsplines):
        print('S[{i}]: {a} + {b} * (x - {x}) + {c} * (x - {x})^2 + {d} * (x - {x})^3'.format(
            i=i, a=cs.a[i], b=cs.b[i], c=cs.c[i]/2, d=cs.d[i]/6, x=cs.x[i]
        ))

    plt.plot(X, exact)
    plt.plot(X, polynom)
    plt.savefig('output/spline.png')