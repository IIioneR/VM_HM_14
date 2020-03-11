import random

def random_number():
    return random.randint(-100, 100)

print(random_number())


def is_simple(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n


print(is_simple(5))