"""Escribir una función que calcule el máximo común divisor de dos números y otra que calcule el mínimo común múltiplo."""


def mcd(a, b):
    aList = []
    bList = []
    cList = []
    for i in range(1, a + 1):
        if a % i == 0:
            aList.append(i)
    for i in range(1, b + 1):
        if b % i == 0:
            bList.append(i)
    for i in aList:
        for j in bList:
            if i == j:
                cList.append(j)
    res = max(cList)
    print(f'El máximo común divisor (MCD) de {a} y {b} es: {res}')


mcd(18, 24)


def mcm(a, b):
    aList = []
    bList = []
    cList = []
    for i in range(1, 11):
        aList.append(a * i)
    for i in range(1, 11):
        bList.append(b * i)
    for i in aList:
        for j in bList:
            if i == j:
                cList.append(j)
    res = min(cList)
    print(f'el mínimo común múltiplo (MCM) de {a} y {b} es: {res}')


mcm(4, 6)

"""
def gcf(a, b)
gcf(18, 24)
def lcm(a, b)
lcm(4, 6)
"""
