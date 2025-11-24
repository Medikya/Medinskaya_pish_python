import re
text = "Сегодня 20 градусов, завтра будет 18 градусов, а вчера было 22 градуса."
digit_strings = re.findall(r'\d+', text)
numbers = [int(s) for s in digit_strings]
print(numbers)