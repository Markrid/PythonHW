# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов 
# нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.


start = int(input("Введите начальное значение: "))
step = int(input("Введите шаг прогрессии: "))
volume = int(input("Введите количество элементов: "))

sp = [int(start+i*step) for i in range(volume)]

print(sp)