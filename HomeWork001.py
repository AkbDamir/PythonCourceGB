
print('Задание 1')

name = input('Введите ваше имя: ')
password = input('Введите ваш пароль: ')
age = input('Введите ваш возраст: ')
print(f'Ваши данные для входа в аккаунт: имя - {name}, пароль - {password}, возраст - {age}.')


print('Задание 2')

import time

sec = int(input('Введите время в секундах: '))
time = time.strftime("%H:%M:%S", time.gmtime(sec))
print(f'{sec} секунд равно: {time}')


print('Задание 3')

num = input('Введите ваше число: ')
n = int(num)
nn = int(num * 2)
nnn = int(num * 3)
print(n + nn + nnn)


print('Задание 4')

proseeds = int(input('Введите выручку фирмы: '))
cost = int(input('Введите издержки фирмы: '))
total = proseeds - cost
if proseeds > cost:
    print(f'Финансовый результат - прибыль. Ее величина: {total}')
else:
    print(f'Финансовый результат - убыток. Его величина: {total}')

profitability = total / proseeds
print(f'Рентабельность выручки = {profitability}')

employee = int(input('Введите численность сотрудников фирмы: '))
profit_emp = total / employee
print(f'Прибыль фирмы в расчете на одного сотрудника = {profit_emp}')
