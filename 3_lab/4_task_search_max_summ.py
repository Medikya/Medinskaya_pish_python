def max_sum_podmassiv(array, k):
    current_sum = sum(array[:k])
    max_sum = current_sum
    max_index = 0
    for i in range(k, len(array)):
        current_sum += array[i] - array[i - k]
        if current_sum > max_sum:
            max_sum = current_sum
            max_index = i - k + 1
    return array[max_index:max_index + k]
if __name__ == "__main__":
    array = [1, -2, 3, 4, -1, 2, 1, -5, 4]
    k = 3
    result = max_sum_podmassiv(array, k)
    print(result)