from math import sin
import copy

xx, yy = [], []


def f(x):
    return 0.5 * x * sin(3 * x)


x = list(range(1, 10, 2))
y = list(map(f, x))


f, g = [], copy.copy(y)

for i in range(n-1):
    ger = []
    for j in range(n-i-1):
        ger.append((gg[j+1] - gg[j])/(xx[j+1+i] - xx[j]))
    ff.append(ger)
    gg = []
    for j in ger: gg.append(j)

otvet = ""
otvet += str(yy[0])
for i in range(n-1):
    otvet += " + ("+str(ff[i][0])
    for j in range(i+1):
        otvet += "*(x-"+str(xx[j])+")"
    otvet += ")"

print("Інтерполяційний поліном Pn(x) у формі Ньютона \n" + otvet)
