# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке
# возрастания все те числа, которые встречаются в обоих наборах. Пользователь вводит 2 числа. n — кол-во элементов
# первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

sp_1 = []
sp_2 = []
n = int(input("Введите количество элементов первого набора: "))
m = int(input("Введите количество элементов второго набора: "))
print("Через ENTER введите значания элементов первого набора")
for i in range(n):
    sp_1.append(int(input()))
print("Через ENTER введите значания элементов второго набора")
for n in range(m):
    sp_2.append(int(input()))

print(f"Вы ввели два набора: 1 - {sp_1} \n \t \t     2 - {sp_2}")
temp = sp_1 + sp_2
temp.sort()
result = set(temp)
print(f"Результат: {result}")
