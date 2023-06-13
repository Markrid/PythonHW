# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках 
# не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть,
# если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного 
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. 
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все 
# в порядке и “Пам парам”, если с ритмом все не в порядке.



def ritm(song: str):
    vocab = "УЕЭОАЫЁЯИЮ"
    count=0
    gl = []
    for el in song:
        if el in vocab: count += 1
        elif el == " ": 
            gl.append(count)
            count=0
    if len(set(gl)) == 1: print("Парам пам-пам!")
    else: print("Пам парам!")


stroka = input("Введите стихотворение, каждая новая строка отделяется пробелом, а слова - тире: ").upper() + " "

ritm(stroka)