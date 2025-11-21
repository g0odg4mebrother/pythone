# zadanie1
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FooBar")
    elif i % 3 == 0:
        print("Foo")
    elif i % 5 == 0:
        print("Bar")
    else:
        print(i)

# zadanie2

try:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    result = num1 / num2
    print(f"Результат деления: {result}")
except ZeroDivisionError:
    print("Ошибка: Деление на ноль!")
except ValueError:
    print("Ошибка: Введите корректные числа!")


# zadanie3


numbers = [4, 8, 2, 10, 5, 8, 2]

unique_numbers = list(set(numbers))

unique_numbers.sort(reverse=True)

total_sum = sum(unique_numbers)

print(f"Без дубликатов: {unique_numbers}")
print(f"Сумма: {total_sum}")

# zadanie4

my_tuple = (1, "hello", 3.14, [1, 2], True)

print(f"Первый элемент: {my_tuple[0]}")
print(f"Последний элемент: {my_tuple[-1]}")

try:
    my_tuple[1] = "world"
except TypeError as e:
    print(f"Ошибка при изменении кортежа: {e}")

my_list = list(my_tuple)
my_list.append("новый элемент")
print(f"Новый список: {my_list}")

# zadanie5

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []
    
    def add_grade(self, grade):
        self.grades.append(grade)
    
    def get_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

student = Student("Иван")
student.add_grade(85)
student.add_grade(92)
student.add_grade(78)
print(f"Средний балл {student.name}: {student.get_average()}")

# zadanie6

students = {"Анна": 85, "Борис": 92, "Виктория": 78, "Григорий": 95}

students["Дмитрий"] = 88

students["Виктория"] += 5

print("Студенты с оценкой выше 90:")
for name, grade in students.items():
    if grade > 90:
        print(f"- {name}: {grade}")

average_grade = sum(students.values()) / len(students)
print(f"Средний балл группы: {average_grade:.2f}")