#Metoda bisekcji - metoda znajdowania danego miejsca w przedziale poprzez dzielenie go na coraz mniejsze
#przedziały spełniające podany warunek
#Pojęcie inkluzji - formalne określenie zawierania się (w szczególności przedziału)


def f(x):
    return (x + 4) * pow((x-7), 3)


a = int(input("Podaj dolną granicę: "))
b = a - 1

while b <= a:
    b = int(input("Podaj górną granicę: "))

e = 0.001

if f(a) * f(b) > 0:
    print("Miejsce zerowe nie znajduje się w przedziale")
else:
    licznik = 0
    while b-a > e:
        x = (b + a) / 2
        if f(b) * f(x) < 0:
            a = x
        else:
            b = x
        licznik += 1

    mz = (a + b) / 2
    print(f'Miejsce zerowe: {mz} ilość powtórzeń: {licznik}')
