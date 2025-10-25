def razvorot_blocks(array, block_size):
    result = []
    for i in range(0, len(array), block_size):
        block = array[i:i + block_size]
        if len(block) == block_size:
            result.extend(block[::-1])
        else:
            result.extend(block)
    return result
array = [1, 2, 3, 4, 5, 6, 7]
block_size = 3
result = razvorot_blocks(array, block_size)
print(result)