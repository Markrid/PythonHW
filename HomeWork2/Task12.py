import random
# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

x = random.randint(0, 1000)
y = random.randint(0, 1000)

# Если хотим ввести самостоятельно
#x = int(input())
#y = int(input())

# Использовать для проверки
#print(x, y)

sum = x + y
product = x*y
print(f"Сумма чисел - {sum}, их произведение - {product}.")

first = 0
second = 0
flag=0

for i in range(1000):
    for n in range(1000):
        #print(i,n)
        if i + n == sum and i * n == product:
            first = i
            second = n
            flag = 1
    if flag:
        break
                   
print(f"Петя задумал два числа: {first} и {second}")