#!/usr/bin/env python3
from math import sin


def runge_kutta(f, x0, x1, h, y0):
    n = int((x1 - x0)/h)
    vx = [0] * (n + 1)
    vy = [0] * (n + 1)
    h = (x1 - x0) / float(n)
    vx[0] = x = x0
    vy[0] = y = y0

    for i in range(1, n + 1):
        k1 = h * f(x, y)
        k2 = h * f(x + 0.5 * h, y + 0.5 * k1)
        k3 = h * f(x + 0.5 * h, y + 0.5 * k2)
        k4 = h * f(x + h, y + k3)
        vx[i] = x = x0 + i * h
        vy[i] = y = y + (k1 + k2 + k2 + k3 + k3 + k4) / 6

    return vx, vy


def adams(f, h, vx, vy):
    x = vx
    y = vy[0:4]

    for k in range(3, len(x) - 1):
        y.append(y[k] + (h/24)*(55*f(x[k], y[k]) - 59*f(x[k-1], y[k-1]) + 37*f(x[k-2], y[k-2]) - 9*f(x[k-3], y[k-3])))

    y_inter = y[0:3]

    for k in range(2, len(x) - 1):
        y_inter.append(y[k] + (h/24)*(9*f(x[k+1], y[k+1]) + 19*f(x[k], y[k]) - 5*f(x[k-1], y[k-1]) + f(x[k-2], y[k-2])))

    return y_inter


def tolerance(yh, yh2, m):
    temp = [yh2[i] for i in range(len(yh2)) if i % 2 == 0]
    return [(yh[i] - temp[i])/(2**m - 1) for i in range(len(yh))]


def main():

    def f(x, y): return 1 - sin(2.2*x + y) + 3.4*y / (2 + x)

    a = 0
    b = 5
    y0 = 0
    h = 0.1

    xh, yh = runge_kutta(f, a, b, h, y0)
    xh2, yh2 = runge_kutta(f, a, b, h/2, y0)

    eps = tolerance(yh, yh2, 4)

    print('Метод Рунге-Кутты:')
    for i in range(len(xh)):
        print("y({0:.1f}) = {1:.6f}\t\t(ε = {2:.5e})".format(xh[i], yh[i], abs(eps[i])))

    ayh = adams(f, h, xh, yh)
    ayh2 = adams(f, h/2, xh2, yh2)

    eps = tolerance(ayh, ayh2, 4)

    print('\n\nМетод Адамса:')
    for i in range(len(xh)):
        print("y({0:.1f}) = {1:.6f}\t\t(ε = {2:.5e})".format(xh[i], ayh[i], abs(eps[i])))


if __name__ == "__main__":
    main()
