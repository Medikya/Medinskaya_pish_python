data = "Иван Иванов, 20, Математика; Петров Петр, 21, Физика; Сидоров Сидр, 22, Химия"
students = data.split("; ")
for student in students:
    parts = student.split(", ")
    name = parts[0]
    age = parts[1]
    faculty = parts[2]
    print("Имя:", name)
    print("Возраст:", age)
    print("Факультет:", faculty)
    print() 