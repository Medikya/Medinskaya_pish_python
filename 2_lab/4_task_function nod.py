def nod(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a
print(nod(66, 21))