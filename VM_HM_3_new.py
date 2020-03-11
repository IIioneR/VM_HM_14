import random

numbers = [15, 3, 64, 33, 22, 12, 45]
min = numbers[0]
for i in numbers:
    if i < min:
        min = i
print(min)
counter = 0
while counter < len(numbers):
    if numbers[counter] < min:
        min = numbers[counter]
    counter += 1
print(min)# 1.Знайти мінімальне число в списку

sum = 0
for i in numbers:
    if i % 3 == 0:
        sum += i
print(sum)

while counter < len(numbers):
    if numbers[counter] % 3 == 0:
        sum = numbers[counter]
    counter += 1
print(sum)# 2.Знайти суму всіх чисел в списку що діляться на 3

b = []
с = []
for i in range(10, 30):
    b.append(i ** 2)
print(b)

counter = 10
while counter < 10:
    b.append(b[counter] ** 2)
    counter += 1
print(b)# 3.Вивести квадрати чисел від 10 до 30

counter = 0
sum = 0
for i in numbers:
    sum += i
    counter += 1
print(sum / counter)
while counter < len(numbers):
    sum += numbers[counter]
    counter += 1
print(sum / counter)# 4.Вивести середнє значення в списку

n = int(input("enter the n "))
sum = 0
for i in range(1, n + 1):
    sum += 1 / i
print(sum)
while counter < n:
    sum += 1/numbers[counter]
    counter += 1
print(sum) # 5.Число n>2 вводиться з клавіатури, порахувати 1 + 1/2 + 1/3 + ... + 1/n


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
    sumMain -= matruc[i][i]    #Суммирует каждый столбик
    matruc[i][i] = sumMain #приравнивает диагональные элементы к сумме столбца n
    sumMain = 0 #Обнуляет сумму для повторного подсчета
    print(matruc[i]) # 7.Отриману матрицю в 6му завдання перетворити так щоб діагональний елемент дорівнював сумі елементів по вертикалі

