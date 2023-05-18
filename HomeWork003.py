# Задача 16:
n = int(input('Введите первое число: '))
lst = []
for i in range(1, n+1):
    lst.append(i)

x = int(input('Введите второе число: '))
print(lst.count(x))

# Задача 18:
n = int(input('Введите первое число: '))
lst = []
for i in range(1, n+1):
    lst.append(i)

x = int(input('Введите второе число: '))
for k in lst:
    if k == x-1:
        print(k)
    else:
        continue

# *Задача 20:
my_dict = {
'АВЕИНОРСТ' : 1,
'ДКЛМПУ' : 2,
'БГЁЬЯ' : 3,
'ЙЫ' : 4,
'ЖЗХЦЧ' : 5,
'ШЭЮ' : 8,
'ФЩЪ' : 10,
'AEIOULNSTR' : 1,
'DG' : 2,
'BCMP' : 3,
'FHVWY' : 4,
'K' : 5,
'JX' : 8,
'QZ' : 10
}

word = input('Введите ваше слово: ')
word = word.upper()
lst = []
for letter in word:
    for key, value in my_dict.items():
        if letter in key:
            lst.append(value)
        else:
            continue

print(sum(lst))