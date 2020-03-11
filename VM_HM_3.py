import random

numbers = [15, 3, 64, 33, 22, 12, 45]
min = numbers[0]
for i in numbers:
    if i < min:
        min = i
print(min)

min2 = numbers[0]
counter = 0
while counter < len(numbers):
    if numbers[counter] < min2:
        min2 = numbers[counter]
    counter += 1
print(min2)# 1.Знайти мінімальне число в списку

sum = 0
for i in numbers:
    if i % 3 == 0:
        sum += i
print(sum)

counter = 0
sum2 = 0
while counter < len(numbers):
    if numbers[counter] % 3 == 0:
        sum2 += numbers[counter]
    counter += 1
print(sum2)# 2.Знайти суму всіх чисел в списку що діляться на 3

b = []
for i in range(10, 30):
    b.append(i ** 2)
print(b)

d = []
counter = 10
while counter < 30:
    d.append(counter**2)
    counter += 1
print(d)# 3.Вивести квадрати чисел від 10 до 30

counter = 0
sum = 0
for i in numbers:
    sum += i
    counter += 1
print(sum / counter)

counter = 0
sum2 = 0
while counter < len(numbers):
    sum2 += numbers[counter]
    counter += 1
print(sum2 / counter)# 4.Вивести середнє значення в списку

n = int(input("enter the n "))
if n > 2:
    sum = 0
    for i in range(1, n + 1):
        sum += 1 / i
    print(sum)
else:print("enter more than 2 ")

if n > 2:
    sum2 = 0
    counter = 1
    while counter < n+1:
        sum2 += 1/counter
        counter += 1
    print(sum2) # 5.Число n>2 вводиться з клавіатури, порахувати 1 + 1/2 + 1/3 + ... + 1/n
else:print("enter more than 2 ")

ran = 3
matruc = []

for i in range(ran):
    matruc.append([])
    for j in range(ran):
        matruc[i].append(random.randint(1, 10))
    print(matruc[i]) # 6.Згенерувати квадратну матрицю з довільними числами
print("___________________")
sumMain = 0
for i in range(ran):
    for j in range(ran):
        sumMain += matruc[j][i]
    sumMain -= matruc[i][i]
    matruc[i][i] = sumMain
    sumMain = 0
    print(matruc[i]) # 7.Отриману матрицю в 6му завдання перетворити так щоб діагональний елемент дорівнював сумі елементів по вертикалі

