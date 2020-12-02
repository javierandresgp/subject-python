""" Escribir funciones que resuelvan los siguientes problemas: """


def is_it_even(n):
    """ Dado un número entero n, indicar si es o no par. """
    if n % 2 == 0:
        return True
    return False

def is_it_prime(n):
    """ Dado un número entero n, indicar si es o no primo. """
    if n == 2:
        return True
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            print(n % i)
#            return False
#        return True


if __name__ == "__main__":
""" print(is_it_even(10))
    print(is_it_even(21))
    print(is_it_prime(-1))
    print(is_it_prime(0))
    print(is_it_prime(1))
    print(is_it_prime(2))
    print(is_it_prime(3))
    print(is_it_prime(4))
    print(is_it_prime(5))
    print(is_it_prime(6))
    print(is_it_prime(7))
    print(is_it_prime(8))
""" print(is_it_prime(9))
