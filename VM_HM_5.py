a = [123, 435, 431, 663, 321, 66, 21312, 21333]


def rotate(b):
    c = 0
    while b != 0:
        c *= 10
        dig = b % 10
        c += dig
        b = b // 10
    return c


print(list(map(rotate, a)))
# за допомогою map перетворити числа в списку на їх дзеркальні (123 -> 321)

b = ["Hello", "how", "are", "you", "I", "From", "Ukraine", "i", "like", "python"]


def insert5(n):
    return len(n) > 5


res = list(filter(insert5, b))
print(res)
# за дрпомогою filter залишити в списку слова довжина яких більше 5 букв

c = [i for i in range(1, 200) if i % 7 == 0]
print(c)
# Згенерувати список чисел від 0 до 200 що діляться на 7

mas = [0, 8, 2, 3, 17]


def listв(m):
    dob = 1
    for i in m:
        if i != 0:
            dob *= i
    m = [dob//i for i in m if i != 0]
    return m


print(listв(mas))


