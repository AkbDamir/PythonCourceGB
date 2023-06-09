from csv import reader, DictReader


def creating():
    file = 'phone.csv'
    with open(file, 'w', encoding='utf-8') as data:
        data.write(f'Фамилия,Имя,Номер\n')


def writing_csv(info):
    file = 'phone.csv'
    with open(file, 'a', encoding='utf-8') as data:
        data.write(f'{info[0]},{info[1]},{info[2]}\n')


def reading_csv(file):
    # возвращает данные в виде строки
    # with open(file, encoding='utf-8') as data:
    # content = data.read()
    # return content

    # возвращает данные в виде списка
    # with open(file, encoding='utf-8') as data:
    # res = list(reader(data))
    # return res

    with open(file, encoding='utf-8') as data:
        res = list(DictReader(data))
    return res


def get_info():
    info = []
    # last_name = input("Введите фамилию: ")
    # first_name = input("Введите имя: ")
    last_name = 'Иванов'
    first_name = 'Иван'
    info.append(last_name)
    info.append(first_name)
    phone_number = ''
    flag = False
    while not flag:
        try:
            # phone_number = input("Введите номер: ")
            phone_number = '12345678911'
            if len(phone_number) != 11:
                print("В номере должно быть 11 цифр")
            else:
                phone_number = int(phone_number)
                flag = True

        except:
            print("В номере должны быть только цифры")

    info.append(phone_number)
    return info


def record_info():
    info = get_info()
    writing_csv(info)
