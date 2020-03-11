

import random


def random_number(number):
    mas = [random.randint(-100, 100) for i in range(number)]
    return mas



def is_simple(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n

def check_simple(mas):
    mas_simple = []
    mas_nosimple = []
    for i in mas:
        if is_simple(i):
            mas_simple.append(i)
        else:
            mas_nosimple.append(i)
    print(mas)
    return ("simple" + str(mas_simple)), ("nosimple" + str(mas_nosimple))

print(check_simple(random_number(5)))