import math


def bisection_method(f, a, b, tolerance=1e-6):
    if f(a) * f(b) > 0:
        return math.nan

    i = 0
    while b - a >= tolerance or abs(f((a+b) / 2)) >= tolerance:
        c = (a + b) / 2

        if f(c) / f(a) > 0:
            a = c
        else:
            b = c

        i += 1

    return (a + b) / 2, i


def newtons_method(f, df, x0, tolerance=1e-6, hop_limit=1000):
    x = x0 - f(x0) / df(x0)
    for i in range(hop_limit):
        if abs(x - x0) < tolerance and abs(f(x)) < tolerance:
            break

        x0, x = x, x - f(x) / df(x)

    return x, i


def chord_method(f, a, b, tolerance=1e-6):
    c, c0 = (a+b)/2, math.inf

    i = 0
    while abs(c-c0) > tolerance or f(c) > tolerance:
        i += 1
        if f(a) * f(b) > 0:
            return math.nan, 0

        c0, c = c, (a*f(b) - b*f(a)) / (f(b) - f(a))

        if f(c) == 0:
            break
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c

    return c, i


def main():
    def f(x):
        return 7*x**5 + 3*x**2 - 2*x - 3

    def df(x):
        return 35*x**4 + 6*x - 2

    n = int(input('Number of real roots: '))

    for i in range(1, n+1):
        print('=' * 80)
        print('{}{} root range: '.format(i, ('st', 'nd', 'rd')[i] if i < 4 else 'th'), end='')
        a, b = map(float, input().split())

        print('Bisection method: {} ({} iterations)'.format(*bisection_method(f, a, b)))
        print('Chord method: {} ({} iterations)'.format(*chord_method(f, a, b)))
        print('Newton\'s method: {} ({} iterations)'.format(*newtons_method(f, df, (a+b)/2)))


if __name__ == '__main__':
    main()
