import random
# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  
# строках записаны N целых чисел Ai. Последняя строка содержит число X

n = int(input("Введите количество элементов: "))
sp = [random.randint(0, 10) for m in range(n)]
x = int(input("Какое число ищем? - "))
result = min(sp)
temp = 0
print(sp)
for i in sp:
    temp = x - i
    if temp == 0:
        result = i
    elif abs(temp) < x-result:
        result = i
print(f"Ближе всего к числу {x} элемент списка со значением {result}")