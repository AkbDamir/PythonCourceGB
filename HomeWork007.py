# Задача 34:
text = input('Жги Винни: ').lower().split()
lst = [sum(letter in 'аяуюоеёэиы' for letter in phrase) for phrase in text]

if len(set(lst)) == 1:
    res = "Парам пам-пам"
else:
    res = "Пам парам"
print(res)

# Задача 36:
def print_operation_table(operation, num_rows=6, num_columns=6):
    for i in range(1, num_rows +1):
        res = [str(operation(i, j)) for j in range(1, num_columns +1)]
        print(" ".join(res))

print_operation_table(lambda x, y: x * y)