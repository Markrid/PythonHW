# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать 
# один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

length = int(input("Введите длину шоколадки? - "))
width = int(input("Введите ширину шоколадки? - "))
part = int(input("Сколько вы хотите отломить? Введите значение - "))

if part > length * width:
    print(f"Такое количество невозможно отломить, ведь сама шоколадка имеет лишь {length*width} кусочков")

if part % length == 0 or part % width == 0:
    print("Поздравляем! Учитывая условия задачи, вы сможете отломить такое количество и не останетесь голодным!")
else:
    print("К сожалению, вы останетесь голодным!")
