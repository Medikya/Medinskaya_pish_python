def sum_digits(n):
    total = 0
    while n != 0:
        total = total + n % 10
        n = n // 10             
    return total
print(sum_digits(155))