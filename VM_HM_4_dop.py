def multi(n):
    while n > 1:
        i = 2
        f = 0
        while 1:
            if n % i == 0:
                n = n // i
                print(i, end=' ')
                f = 1
                break
            else:
                i += 1
        if f == 1:
            continue
    print()


multi(8)  # Написати функцію що розкладає число на множники: 18: 2*3*3


def bin(m):
    i = 2
    mass = []
    while m != 0:
        b = m % i
        mass.append(b)
        m = m // i
    print(mass[::-1])

bin(13) # функцію що переводить числа в двійкову систему: 13 = 1101


def bin2(m, k):
    if k < 11:
        i = k
        mass = []
        while m != 0:
            b = m % i
            mass.append(b)
            m = m // i
        print(mass[::-1])
    else:
        i = k
        mass = []
        while m != 0:
            b = m % i
            mass.append(b)
            m = m // i
        print(mass[::-1])


bin2(13, 11)

