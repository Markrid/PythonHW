import random
# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены
# только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.Эти кусты
# обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai
# ягод.В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего
# модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.Напишите программу для нахождения максимального числа
# ягод, которое может собрать за один заход собирающий модуль,находясь перед некоторым кустом заданной во входном файле
# грядки.

def PickBarries(list):
    result = [0,0,0]
    for i in range(len(list)):
        result[0] += list[i]
        if list[i] > result[1]:
            result[1] = list[i]
            result[2] = i
    return result

print(f"\nПрограмма самостоятельно генерирует количество кустов на клумбе и производит сбор ягод. \nВ конце вычисляет сколько всего ягод собрано и где было больше всего. \nДля продолжения нажмите ENTER...")
input()
gardenBed1 = []
for i in range(random.randint(3, 10)):
    gardenBed1.append(random.randint(1, 30))
gardenBed2 = []
for i in range(random.randint(3, 5)):
    gardenBed2.append(random.randint(1, 15))
gardenBed3 = []
for i in range(random.randint(3, 20)):
    gardenBed3.append(random.randint(1, 60))

print("Введите номер клумбы 1, 2 или 3")
number = int(input())
if number == 1:
    print(f"Сгенерированная клумба: {gardenBed1}")
    result = PickBarries(gardenBed1)
elif number == 2:
    print(f"Сгенерированная клумба: {gardenBed2}")
    result = PickBarries(gardenBed2)
else:
    print(f"Сгенерированная клумба: {gardenBed3}")
    result = PickBarries(gardenBed3)

print(f"Всего собрано: {result[0]} ягод(ы). \nМаксимум ягод на кусте № {result[2]+1}, количество - {result[1]} ягод(ы)")
