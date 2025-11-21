
def task1():
    
    print("=" * 50)
    print("1. Задача на циклы (FooBar):")
    print("=" * 50)
    for i in range(1, 51):
        if i % 3 == 0 and i % 5 == 0:
            print("FooBar")
        elif i % 3 == 0:
            print("Foo")
        elif i % 5 == 0:
            print("Bar")
        else:
            print(i)

def task2():
    
    print("\n" + "=" * 50)
    print("2. Задача на исключения (Деление чисел):")
    print("=" * 50)
    
    def divide_numbers():
        try:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
            result = num1 / num2
            print(f"Результат деления: {result}")
        except ZeroDivisionError:
            print("Ошибка: Деление на ноль невозможно!")
        except ValueError:
            print("Ошибка: Введите корректные числа!")
    
    divide_numbers()

def task3():
    print("\n" + "=" * 50)
    print("3. Задача на списки:")
    print("=" * 50)
    
    numbers = [4, 8, 2, 10, 5, 8, 2]
    print(f"Исходный список: {numbers}")
    
    unique_numbers = list(set(numbers))
    print(f"Список без дубликатов: {unique_numbers}")
    
    sorted_numbers = sorted(unique_numbers, reverse=True)
    print(f"Отсортированный список: {sorted_numbers}")
    
    total_sum = sum(sorted_numbers)
    print(f"Сумма элементов: {total_sum}")

def task4():

    print("\n" + "=" * 50)
    print("4. Задача на кортежи:")
    print("=" * 50)
    
    my_tuple = (10, "hello", 3.14, [1, 2, 3], {"key": "value"})
    print(f"Исходный кортеж: {my_tuple}")
    
    print(f"Первый элемент: {my_tuple[0]}")
    print(f"Последний элемент: {my_tuple[-1]}")
    
    try:
        my_tuple[1] = "world"
    except TypeError as e:
        print(f"Ошибка при попытке изменения кортежа: {e}")
    
    my_list = list(my_tuple)
    my_list.append("новый элемент")
    print(f"Список после добавления: {my_list}")

def task5():

    print("\n" + "=" * 50)
    print("5. Задача на ООП (Класс Student):")
    print("=" * 50)
    
    class Student:
        def __init__(self, name):
            self.name = name
            self.grades = []
        
        def add_grade(self, grade):
            """Добавляет оценку в список"""
            if 0 <= grade <= 100:
                self.grades.append(grade)
                print(f"Оценка {grade} добавлена для студента {self.name}")
            else:
                print("Оценка должна быть в диапазоне от 0 до 100")
        
        def get_average(self):
            """Возвращает средний балл"""
            if not self.grades:
                return 0
            return sum(self.grades) / len(self.grades)
        
        def __str__(self):
            return f"Студент: {self.name}, Оценки: {self.grades}, Средний балл: {self.get_average():.2f}"
    
    student1 = Student("Иван Петров")
    student1.add_grade(85)
    student1.add_grade(92)
    student1.add_grade(78)
    student1.add_grade(105) 
    print(student1)
    
    student2 = Student("Мария Сидорова")
    student2.add_grade(95)
    student2.add_grade(88)
    print(student2)

def task6():

    print("\n" + "=" * 50)
    print("6. Задача на словарь (Студенты и оценки):")
    print("=" * 50)
    
    students = {"Анна": 85, "Борис": 92, "Виктория": 78, "Григорий": 95}
    print(f"Исходный словарь: {students}")
    
    students["Дмитрий"] = 88
    print(f"После добавления Дмитрия: {students}")
    
    students["Виктория"] += 5
    print(f"После увеличения оценки Виктории: {students}")
    
    high_achievers = [name for name, grade in students.items() if grade > 90]
    print(f"Студенты с оценкой выше 90: {high_achievers}")
    
    average_grade = sum(students.values()) / len(students)
    print(f"Средний балл группы: {average_grade:.2f}")

if __name__ == "__main__":
    task1()
    task2()
    task3()
    task4()
    task5()

    task6()
