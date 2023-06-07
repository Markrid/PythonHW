# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень 
# B с помощью рекурсии.

def stepen(number, i):
    if i == 0:
        return 1
    return number * stepen(number, i-1)


print(stepen(3,3))