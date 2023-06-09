import random

# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

n = int(input("Введите размер списка: "))
sp = [random.randint(-10,30) for _ in range(n)]

minimum = int(input("Введите минимальное значение: "))
maximum = int(input("Введите максимальное значение: "))
result = []
for i in range(len(sp)):
    if minimum<sp[i]<maximum:
        result.append(i)

print(sp)
print(f"Индексы элементов по заданным параметрам - {result}")
