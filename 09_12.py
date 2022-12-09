import math

def f(x):
    return pow(math.e, x)


def F(x):
    return pow(math.e, x)


def Q(a, b):
    pom1 = (b-a) / 2
    pom2 = f(a) + f(b)
    return pom1 * pom2


def kwadrat(a, b):
    q = Q(a, b)
    I = F(a) - F(b)
    blad = abs(q - I) / abs(I)

    print(f'N = 1, {q}, blad')

    j = 1
    for j in range(31):
        N = pow(2, j)
        H = (b - a) / N
        q = 0

        for k in range(N):
            q = q + Q(a + (k*H), a+((k+1)*H))
        blad = abs(q - I) / abs(I)
        print(f'N= {math.log(N, 2)}, q= {q}, blad= {blad}')

kwadrat(4, 1)


