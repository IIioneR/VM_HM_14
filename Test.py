# Знайти найменше число в списку
mas = [231, 53, 5, 3, 22]
a = mas[0]
for i in mas:
    if i < a:
        a = i
print(a)

# Вивести в циклі всі парні числа до 100,
# крім 6, 8, 86 якщо число 90 зустрінеться в
# списку то перервати його роботу
for i in range(2, 100, 2):
    bad_numbers = [6, 8, 86]
    if i in bad_numbers:
        continue
    if i == 90:
        break
    print(i, end=" ")

# Написати функцію що перевіряє
# чи є строка правильно записаний email
from re import *

def get_address(address):
    res = True
    pattern = compile('(^|\s)[-a-z0-9_.]+@([-a-z0-9]+\.)+[a-z]{2,6}(\s|$)')
    is_valid = pattern.match(address)
    if is_valid:
        print("correct")
        return res
    else:
        print("wrong")
        return False

print(get_address("hello@ukr.net"))

# Скільки існує комбінацій пароля 4 символів, якщо відомо що друга
# цифра 4, 5 або 7, перша не 0, третя менша 6 а четверта більша 7
count = 0
for i in range(1,10):
    for j in range(4,8):
        if j != 6:
            for k in range(0,6):
                for l in range(8,10):
                    count += 1
print(count)


# За допомогою filter залишити в списку тільки числа кранні 5
mass2 = [5, 10, 22, 25, 36, 40, 90, 98, 115, 129, 332]


def crat(m):
    return m % 5 == 0


print(list(filter(crat, mass2)))

# Написати декоратор обмежувач, тобто коли функція хоче повернути
# число більше ніж 10000, то декоратор замінює це число на 9999.
def decorator(f):
    def wrapper(*args, **kwargs):
        res = f(*args, **kwargs)
        if res > 10000:
            print(9999)
        else:
            print(res)
        return res
    return wrapper


@decorator
def max(n):
    return n


print(max(1252))

# Дано список цілих чисел, порахувати скільки чисел з
# цього списку мають парну кількість цифр
mas3 = [23, 532, 23, 55, 654643, 732]
count = 0
for i in mas3:
    if int(len(str(i)) % 2 == 0):
        count += 1

print(str(mas3)+" -> "+str(count))


# Дано ціле число що містить тільки цифри 9 і 6, використовуючи всього одну
# заміну цифри в числі знайти максимальне число.
n = 96999696999
a = ''
count = 0
for i in str(n):
    if i == '6' and count != 1:
        i = '9'
        count += 1
    x = a.join(i)
    print(x, end ='')


# Дано ціле число n, згенерувати список довжиною n,
# сума елементів якого яких рівна 0. (Числа повинні бути унікальні)
import random

n = 10
mas4 = list(set([random.randint(1, 1000) for i in range(n-1)]))
print(mas4.append(-sum(mas4)))
print(mas4)

# Дано не порожній список, кожне число в цьому списку зявляється
# 2 рази, крім одного - знайти це число.
mas5 = [2, 10, 5, 6, 12, 10, 2, 12, 6]
for i in range(len(mas5)):
    cond = 1
    for j in range(len(mas5)):
        if mas5[i] == mas5[j] and i != j:
            cond = 0
            break
    if cond == 1:
        print(mas5[i])

# Дано дві строки, перевірити чи є вони анаграмою.
# Тобто чи з першої строки можна получить
# іншу за допомогою перестановок букв.
str1 = 'vbabvo'
str2 = 'ovvabb'

lista = list(str1)
listb = list(str2)

lista.sort()
listb.sort()

def prov(s1,s2):
    cond = True
    i = 0
    while i < len(lista):
        if lista[i] == listb[i]:
            i += 1
        else:
            return False

    return cond

print(prov(lista, listb))

#Перевірити правильність відкриття/закриття дужок
n = ["(", "[", "]", ")"]
firts = ["(","[","{"]
end = [")", "]", "}"]
cond = {
    "(": ")",
    "[": "]",
    "{": "}"
    }

res = False
i = 0
s = []
while i < len(n) and n[0] in firts:
    if n[i] in firts:
        s.append(n[i])
    if n[i] in end:
        for j in cond:
            if n[i] == cond[j]:
                s.pop(-1)

    if len(s) == 0:
        res = True
    i += 1
print(res)
# Створити функцію що приймає два аргументи, перший список додатніх цілих
# исел, другий довільне ціле додатнє чило.
# Задача знайти всі можливі комбінації
# ( можливе повторення чивел )
# чисел в списку так щоб сума їх дорівнювала другому аргументу:
# наприклад функція приймає список [ 2, 3, 5] і другий аргумент 8
# на виході потрібно получить такі 3 комбінації [2,2,2,2], [2,3,3], [3,5].
# (Якщо без повторення цифр то ще +3б) (задача рекурсивна﻿)
# ЗАДАЧА НЕПОВНА



n1 = 8
a1 = [2, 3, 5]
b = []

def number_to_0(n, a):

    if n == 0:
        return 0
    else:
        for i in range(len(a)):
            print(a[i], end=' ')
            return number_to_0(n-a[i], a)



print(number_to_0(n1, a1))

#Є файл з даними учнів у форматі Прізвище;ім’я;зріст Написати функцію що
# зчитує дані з файлу, функцію що добавляє учня до файлу, функцію що
# перевіряє чи є валідним формат даних що вводить користувач.

words_info = list()
par = ["surname", "name", "growth"]
for i in par:
    data = input("Enter the " + i)
    words_info.append(data + ",")

#є валідним формат даних що вводить користувач
def check(info):
    words = []
    for line in info:
        words.append(line.replace(',', ""))

    return words[0].isalpha() and words[1].isalpha() and words[2].isnumeric()

# функцію що добавляє учня до файлу
def write_line(file):
    with open(file, 'a') as file:
        file.writelines("\n")
        file.writelines(words_info)

# зчитує дані з файлу
def read_line(file):
    result = []
    with open(file, 'r') as file:
        for line in file.readlines():
            person_words = line.split(',')
            person_words[2] = person_words[2].replace('\n', '')
            person = {
                "surname": person_words[0],
                "name": person_words[1],
                "growth": person_words[2]
            }
            result.append(person)
    return result


print(write_line('Students'))
print(check(words_info))
print(read_line('Students'))

