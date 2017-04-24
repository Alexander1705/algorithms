import matplotlib.pyplot as plt


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
    from math import cos

    def f(x):
        return 0.5 * x * cos(3 * x)

    nodes = list(range(1, 10, 2))

    cs = CubicSpline(nodes, list(map(f, nodes)))

    X = [1 + 8 * (i/100) for i in range(101)]
    exact = list(map(f, X))
    spline = list(map(cs, X))

    print(spline)

    plt.plot(X, exact)
    plt.plot(X, spline)
    plt.savefig('output/plot.png')
    plt.show()