# Задача 2: Найдите сумму цифр трехзначного числа.

number = int(input('Введите трехзначное число: '))

count = 0

count = count + (number % 10) + (number // 10 % 10) + (number // 100)

print(f'Сумма цифр в числе: {number} , равна {count}')
