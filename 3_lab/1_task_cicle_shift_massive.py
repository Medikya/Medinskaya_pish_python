def cyclic_shift(lst, k):
    if k == 0:
        return lst[:]
    return lst[-k:] + lst[:-k]
my_list = [1, 2, 3, 4, 5]
shift = 2
result = cyclic_shift(my_list, shift)
print("Результат:", result)