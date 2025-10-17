def summ_eq_mult(x):
    str_x = str(x)
    sum = 0
    mult = 1
    for char in str_x:
        sum = sum + int(char)
        mult = mult * int(char)
    return sum == mult
print(summ_eq_mult(45897))