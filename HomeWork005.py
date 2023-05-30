# Задача 26:
a = int(input('Введите число А: '))
b = int(input('Введите число В: '))
def expon(a, b):
    # res = 1
    #     for i in range(b):
    #         res *= a
    #     return res
    if b == 1:
        return a
    return a * expon(a, b - 1)
print(expon(a, b))

# Задача 28:

a = int(input('Введите число А: '))
b = int(input('Введите число В: '))
def my_sum(a, b):
    # while b > 0:
    #     a += 1
    #     b -= 1
    # return a
    if b == 0:
        return a
    return 1 + my_sum(a, b - 1)

print(my_sum(a, b))
