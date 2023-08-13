def Make_dict():    # Берет данные из phone.txt и возвращает их в виде списка абонентов
    phone_file = open('phone.txt', 'r', encoding='UTF-8')
    phone_reading = phone_file.readlines()
    phone_file.close()
    phone_list = [item.strip().split(';') for item in phone_reading]
    phone_dict_item = lambda x: {"ФИО":x[0].strip(), "Номер тел.":x[1].strip(), "Комментарий":x[2].strip()}
    return list(map(phone_dict_item, phone_list))

def Finding_by():   # Ищет и выводит на экран карточку абонента
    dict_find= Make_dict()
    finding = input("Введите данные для поиска: ")
    data_for_change = False
    for item in dict_find:
        if finding in item.values():
            data_for_change = item
            print(item)
    if data_for_change == False:
        print("Данные не найдены")
        Finding_by()
    Start_()
        
def Save_in_txt_file(ph_dict):    # Сохраняет список абонентов в файл в виде строки
    phone_txt = open('phone.txt', 'w', encoding='UTF-8')
    new_dict_str = ''.join(map(lambda x: ";".join(x.values())+"\n", ph_dict))
    phone_txt.write(new_dict_str.strip())
    phone_txt.close()
    print("Данные обновлены")
    Start_()

def Changing_data():   # Вносит изменения в карточку абонента
    dict_cd= Make_dict()
    def Sub_change_data(i_scd , dict__scd):    # Меняет карточку абонента на основе введенных данных
        choice_scd = input("Какое поле требуется изменить? Введите вариант:\n\t1 - ФИО\n\t2 - Номер телефона\n\t3 - Комментарий\n\n\t4 - Назад\n\t5 - В начало\n:")
        match choice_scd:
            case "1":
                new_fio = input("Введите новые ФИО абонента: ")
                dict__scd[i_scd]["ФИО"] = new_fio
                print(f"Новая карточка абонента: \n{dict__scd[i_scd]}")
            case "2":
                new_number = input("Введите новый телефон: ")
                dict__scd[i_scd]["Номер тел."] = new_number
                print(f"Новая карточка абонента: \n{dict__scd[i_scd]}")
            case "3":
                new_comment = input("Введите новый комментарий: ")
                dict__scd[i_scd]["Комментарий"] = new_comment
                print(f"Новая карточка абонента: \n{dict__scd[i_scd]}")
            case "4":
                Changing_data()
            case "5":
                Start_()
            case _:
                Sub_change_data(i_scd , dict__scd)

    def Send_to_file(dict_cd):     # Запрос подтверждение сохраняем новые данные в файл или нет?
        save_choice = input("\nСохранить изменения в справочник?\n\t1 - Да\n\t2 - Нет\n:")
        match save_choice:
            case "1":
                Save_in_txt_file(dict_cd)
            case "2":
                Changing_data()
            case _:
                Send_to_file(dict_cd)
        Start_()

    finding = input("Введите данные для поиска: ")
    data_for_change = False
    for i in range(len(dict_cd)):
        if finding in dict_cd[i].values():
            data_for_change = dict_cd[i]
            print(dict_cd[i])
            Sub_change_data(i , dict_cd)
            Send_to_file(dict_cd)
    if data_for_change == False:
        print("Данные не найдены")
        Changing_data()

def New_card():    # Создаёт и заносит в файл новую карточку абонента
    def Add_in_file(name_, phone_, comment_):    # Добавляет данные в файл
        send_str = f"\n{name_};{phone_};{comment_}"
        ph_file = open("phone.txt", "a", encoding="UTF-8")
        ph_file.write(send_str)
        ph_file.close()
        print("Новый контакт успешно добавлен!")
        Start_()

    name = input("Введите ФИО абонента: ")
    phone = input("Введите телефон абонента: ")
    comment = input("Введите комментарий абонента: ")
    print(f"[ФИО: {name.strip()}, Номер тел.: {phone.strip()}, Комментарий: {comment.strip()}]\n↑ Всё верно введено? Сохранить в базу?\n\
1 - Да\n2 - Нет, есть ошибки\n3 - В начало")
    ans = input(": ")
    match ans:
        case "1":
            Add_in_file(name, phone, comment)
        case "2":
            New_card()
        case "3":
            Start_()
        case _:
            New_card()

def Del_card():   # Удаляет карточку абонента из базы
    dict_dc= Make_dict()
    def Del_and_send_to_file():    # Запрос-подтверждение удаляем данные из файла или нет?
        save_choice = input("\nУдалить абонента из справочника?\n\t1 - Да\n\t2 - Нет\n\t3 - В начало\n:")
        match save_choice:
            case "1":
                Save_in_txt_file(dict_dc)
            case "2":
                Del_card()
            case "3":
                Start_()
            case _:
                Del_and_send_to_file()
        
    finding = input("Введите данные для поиска карточки абонента: ")
    data_for_change_del = ""
    for i_d in range(len(dict_dc)):
        if finding in dict_dc[i_d].values():
            data_for_change_del = i_d
            print(dict_dc[i_d])
    if data_for_change_del == "":
        print("Данные не найдены")
        Del_card()
    dict_dc.pop(data_for_change_del) 
    Del_and_send_to_file()

def Start_():   # Стартовая ф-я выбираем действия с программой

    choice_fn = input("\nВыберите действия со справочником:\n\t1 - Вывести все данные\n\t\
2 - Поиск абонента по данным\n\t3 - Внести изменения в справочник\n\t\
4 - Добавить контакт\n\t5 - Удалить контакт\n\t6 - Закрыть справочник\n\
:")
    match choice_fn:
        case "1":
            [print(f"— ФИО:{i['ФИО']}, Номер тел.:{i['Номер тел.']}, Комментарий:{i['Комментарий']}") for i in Make_dict()]
            Start_()
        case "2":
            Finding_by()
        case "3":
            Changing_data()
        case "4":
            New_card()
        case "5":
            Del_card()
        case "6":
            return
        case _:
            print("Введите числа от 1 до 3")
            Start_()

Start_() # Делайте окно терминала повыше