import argparse

def parse_line(row, line_no):
    def warn(msg):
        print("Ошибка в строке " + str(line_no) + ": " + msg)
        print("   Строка: " + ";".join(row))

    # Пробуем преобразовать все поля в числа
    try:
        year = int(row[0])
        month = int(row[1])
        day = int(row[2])
        hour = int(row[3])
        minute = int(row[4])
        temperature = int(row[5])
    except (ValueError, IndexError):
        warn("невозможно прочитать числовые данные")
        return None

    return {
        "month": month,
        "temp": temperature,
    }


parser = argparse.ArgumentParser(
    description="Приложение для вычисления статистики температуры из CSV-файла."
)

parser.add_argument(
    "-f",
    "--file",
    help="Входной CSV-файл",
    required=False
)

parser.add_argument(
    "-m",
    "--month",
    type=int,
    help="Номер месяца (1..12) для вывода статистики только по нему",
    required=False
)

args = parser.parse_args()

# Если не указан файл — показать справку и выйти
if args.file is None:
    parser.print_help()
    exit()

filename = args.file
month_filter = args.month

# Проверка корректности месяца, если задан
if month_filter is not None:
    if month_filter < 1 or month_filter > 12:
        print("Ошибка: номер месяца должен быть от 1 до 12.")
        exit()

# Считываем данные
line_datas = []

with open(filename) as f:
    line_number = 0
    for line in f:
        line_number += 1
        line = line.strip()

        if line == "":
            continue

        row = line.split(";")
        line_data = parse_line(row, line_number)
        if line_data is None:
            exit()  # останавливаемся при первой ошибке
        line_datas.append(line_data)

# Если данных нет
if len(line_datas) == 0:
    print("Нет корректных данных для обработки.")
    exit()

# Группируем температуры по месяцам
monthly_temps = {}
for i in range(1, 13):
    monthly_temps[i] = []

for record in line_datas:
    m = record["month"]
    t = record["temp"]
    # Добавляем только если месяц в допустимом диапазоне
    if 1 <= m <= 12:
        monthly_temps[m].append(t)

# Функция для подсчёта статистики
def compute_stats(temps):
    if len(temps) == 0:
        return None
    total = 0
    for t in temps:
        total = total + t
    avg = total / len(temps)
    min_t = temps[0]
    max_t = temps[0]
    for t in temps:
        if t < min_t:
            min_t = t
        if t > max_t:
            max_t = t
    return {
        "avg": avg,
        "min": min_t,
        "max": max_t
    }

# Случай: вывод только одного месяца
if month_filter is not None:
    temps = monthly_temps[month_filter]
    if len(temps) == 0:
        print("В месяце " + str(month_filter) + " нет данных.")
    else:
        stat = compute_stats(temps)
        print("")
        print("Статистика для месяца " + str(month_filter) + ":")
        print("СРЕДНЯЯ:      " + str(round(stat["avg"], 2)))
        print("МИНИМАЛЬНАЯ:  " + str(stat["min"]))
        print("МАКСИМАЛЬНАЯ: " + str(stat["max"]))
    exit()

# Случай: вывод всех месяцев
print("")
print("Статистика по месяцам:")
print("----------------------------------------")
for month in range(1, 13):
    temps = monthly_temps[month]
    if len(temps) == 0:
        print("Месяц " + str(month) + ": данных нет")
    else:
        stat = compute_stats(temps)
        print("Месяц " + str(month) + ": ср=" + str(round(stat["avg"], 2)) +
              ", мин=" + str(stat["min"]) +
              ", макс=" + str(stat["max"]))

# Годовая статистика
all_temps = []
for m in range(1, 13):
    all_temps = all_temps + monthly_temps[m]

year_stat = compute_stats(all_temps)
print("")
print("================ГОД=================")
print("СРЕДНЯЯ:      " + str(round(year_stat["avg"], 2)))
print("МАКСИМАЛЬНАЯ: " + str(year_stat["max"]))
print("МИНИМАЛЬНАЯ:  " + str(year_stat["min"]))
print("====================================")