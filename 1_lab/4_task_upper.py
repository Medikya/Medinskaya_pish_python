a = input()
возрастание = True

for i in range(len(a) - 1):
    if a[i] >= a[i + 1]:
        возрастание = False
        break

if возрастание:
    print("Да")
else:
    print("Нет")