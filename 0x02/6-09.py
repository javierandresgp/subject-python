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


mcd(4, 6)
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
mcm(18, 24)


def primeNumber(number):
    countFactors = 0
    for factor in range(1, number + 1):
        if number % factor == 0:
            countFactors += 1
    if countFactors == 2:
        return True
    else:
        return False


def primeNumberList(limit):
    primeList = []
    for number in range(2, limit + 1):
        if primeNumber(number) == True:
            primeList.append(number)
    return (primeList)


def gcf(a, b):
    primeNumbers = primeNumberList(10)
    factorsList = []
    for prime in primeNumbers:
        if a % prime == 0 and b % prime == 0:
            factorsList.append(prime)
    res = 1
    for factor in factorsList:
        res *= factor
    print('The Greatest Common Factor (GCF) the {} and {} is: {}'.format(a, b, res))


gcf(4, 6)
gcf(18, 24)


def lcm(a, b):
    primeNumbers = primeNumberList(10)
    factorList = []
    for prime in primeNumbers:
        if a % prime == 0:
            factorList.append(prime)
        if b % prime == 0:
            factorList.append(prime)
        res = 1
        print(factorList)
        for factor in factorList:
            res *= factor
    print('The Least Common Multiple (LCM) the {} and {} is: {}'.format(a, b, res))


lcm(4, 6)
lcm(18, 24)
