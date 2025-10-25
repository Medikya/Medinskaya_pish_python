def shift_m(matrix, shift):
    result = []
    for row in matrix:
        if shift == 0:
            result.append(row[:])
        else:
            result.append(row[-shift:] + row[:-shift])
    return result
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
shift = 1
result = shift_m(matrix, shift)
for row in result:
    print(row)