a = int(input('Введите число а'))
b = int(input('Введите число b'))
сумма = 0
for i in range(a, b + 1):
    сумма = сумма + i * i
print(сумма)