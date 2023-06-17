data_contact = "contact.txt"


def menu():
    print("Что вы хотите сделать:\n "
          "\t1 - показать все контакты\n"
          "\t2 - найти контакт\n"
          "\t3 - добавить контакт\n"
          "\t4 - удалить контакт\n"
          "\t5 - изменить контакт")
    select = int(input())
    if select == 1:
        show_all_records(data_contact)
    elif select == 2:
        surname = input("Введите искомые данные: ")
        search(surname)
    elif select == 3:
        add_contact(data_contact)
    elif select == 4:
        del_contact(data_contact)
    elif select == 5:
        edit_contact(data_contact)


def show_all_records(file):
    with open(file, "r", encoding="utf-8") as f:
        print(f.read())


def search(name):
    with open(data_contact, "r", encoding="utf-8") as f:
        temp = list(f.readlines())
        sp = [el.strip() for el in temp]
        flag = True
        for i in sp:
            if name.upper() in i.upper():
                 print(i)
                 flag = False
        if flag:
            print(f"Контакт с данными >{name}< отсутствует.")



def add_contact(file):
    with open(file, "a", encoding="utf-8") as f:
        sp = input("Введите через пробел фамилию, имя, отчество, возраст и телефон:\n")
        f.writelines(f"{sp};\n")
        print("Контакт успешно добавлен!")


def del_contact(file):
    with open(file, "r", encoding="utf-8") as f:
        temp = list(f.readlines())
        sp = [el.strip() for el in temp]   
        for i in range(len(sp)):
            print(f"{i+1} - {sp[i]}")
        del_number = int(input("Введите порядковый номер контакта, который хотите удалить: "))
        del sp[del_number-1]

    with open(file, "w", encoding="utf-8") as f:
        for i in sp:
            f.writelines(f"{i}\n")
        print("Удаление прошло успешно!")


def edit_contact(file):
    with open(file, "r", encoding="utf-8") as f:
        temp = list(f.readlines())
        sp = [el.strip() for el in temp]   
        for i in range(len(sp)):
            print(f"{i+1} - {sp[i]}")
        edit_number = int(input("Введите порядковый номер контакта, который хотите изменить: "))
        del sp[edit_number-1]
        contact = input("Введите через пробел новые фамилию, имя, отчество, возраст и телефон:\n")
        sp.insert(edit_number-1, contact + ";")
        
    with open(file, "w", encoding="utf-8") as f:
        for i in sp:
            f.writelines(f"{i}\n")
        print("Изменение прошло успешно!")
  

menu()
