
c = 1
m = pow(2, 100) * pow(3, 3) * pow(5, 2)
a = 1 + 2 * pow(2, 5) * pow(3, 2) * pow(5, 2)

def gen(x):
    global c
    global m
    global a
    return (a * x + c) % m

x = float(input("podaj zarodek: "))
tab = list()
suma = 0

for i in range(10000):
    x = float(gen(x))
    u = (x * float(1)) / float(m)
    tab.append(u)
    suma += u
    print(u)

srednia = float(suma / 10000.1)
print("\nsrednia:", srednia)
