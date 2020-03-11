

import random


def random_number(number):
    mas = [random.randint(-100,100) for i in range(number)]
    return mas



def is_simple(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n

