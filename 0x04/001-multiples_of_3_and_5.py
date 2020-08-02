""" If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000. """
sum = 0


def mul3and5(below):
    for number in range(1, below):
        if number % 3 == 0 or number % 5 == 0:
            global sum
            sum += number
    return sum


print(mul3and5(1000))
