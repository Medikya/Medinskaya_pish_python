s = "aaabbbcccaaaddd"
result = ""
for char in s:
    if not result or char != result[-1]:
        result += char
print(result)