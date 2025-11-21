#zadanie1 
class Car:
    def __init__(self, model="", year=0, manufacturer="", engine_volume=0.0, color="", price=0.0):
        self._model = model
        self._year = year
        self._manufacturer = manufacturer
        self._engine_volume = engine_volume
        self._color = color
        self._price = price
    
    def input_data(self):
        try:
            self._model = input("Введите название модели: ")
            self._year = int(input("Введите год выпуска: "))
            self._manufacturer = input("Введите производителя: ")
            self._engine_volume = float(input("Введите объем двигателя (л): "))
            self._color = input("Введите цвет машины: ")
            self._price = float(input("Введите цену ($): "))
        except ValueError:
            print("Ошибка ввода данных! Проверьте правильность введенных значений.")
    
    def display_data(self):
        """Метод для вывода данных"""
        print(f"""
        === ИНФОРМАЦИЯ ОБ АВТОМОБИЛЕ ===
        Модель: {self._model}
        Год выпуска: {self._year}
        Производитель: {self._manufacturer}
        Объем двигателя: {self._engine_volume} л
        Цвет: {self._color}
        Цена: ${self._price:,.2f}
        """)
    
    def get_model(self):
        return self._model
    
    def get_year(self):
        return self._year
    
    def get_manufacturer(self):
        return self._manufacturer
    
    def get_engine_volume(self):
        return self._engine_volume
    
    def get_color(self):
        return self._color
    
    def get_price(self):
        return self._price
    
    def set_model(self, model):
        self._model = model
    
    def set_year(self, year):
        if year > 1885: 
            self._year = year
        else:
            print("Некорректный год выпуска!")
    
    def set_manufacturer(self, manufacturer):
        self._manufacturer = manufacturer
    
    def set_engine_volume(self, engine_volume):
        if engine_volume > 0:
            self._engine_volume = engine_volume
        else:
            print("Объем двигателя должен быть положительным!")
    
    def set_color(self, color):
        self._color = color
    
    def set_price(self, price):
        if price >= 0:
            self._price = price
        else:
            print("Цена не может быть отрицательной!")

#zadanie2

class Book:
    def __init__(self, title="", year=0, publisher="", genre="", author="", price=0.0):
        self._title = title
        self._year = year
        self._publisher = publisher
        self._genre = genre
        self._author = author
        self._price = price
    
    def input_data(self):
        """Метод для ввода данных"""
        try:
            self._title = input("Введите название книги: ")
            self._year = int(input("Введите год выпуска: "))
            self._publisher = input("Введите издателя: ")
            self._genre = input("Введите жанр: ")
            self._author = input("Введите автора: ")
            self._price = float(input("Введите цену ($): "))
        except ValueError:
            print("Ошибка ввода данных! Проверьте правильность введенных значений.")
    
    def display_data(self):
        print(f"""
        === ИНФОРМАЦИЯ О КНИГЕ ===
        Название: {self._title}
        Год выпуска: {self._year}
        Издатель: {self._publisher}
        Жанр: {self._genre}
        Автор: {self._author}
        Цена: ${self._price:,.2f}
        """)
    
    def get_title(self):
        return self._title
    
    def get_year(self):
        return self._year
    
    def get_publisher(self):
        return self._publisher
    
    def get_genre(self):
        return self._genre
    
    def get_author(self):
        return self._author
    
    def get_price(self):
        return self._price
    
    def set_title(self, title):
        self._title = title
    
    def set_year(self, year):
        if year > 0:
            self._year = year
        else:
            print("Некорректный год выпуска!")
    
    def set_publisher(self, publisher):
        self._publisher = publisher
    
    def set_genre(self, genre):
        self._genre = genre
    
    def set_author(self, author):
        self._author = author
    
    def set_price(self, price):
        if price >= 0:
            self._price = price
        else:
            print("Цена не может быть отрицательной!")

#zadanie2

class Stadium:
    def __init__(self, name="", opening_date="", country="", city="", capacity=0):
        self._name = name
        self._opening_date = opening_date
        self._country = country
        self._city = city
        self._capacity = capacity
    
    def input_data(self):
        try:
            self._name = input("Введите название стадиона: ")
            self._opening_date = input("Введите дату открытия (дд.мм.гггг): ")
            self._country = input("Введите страну: ")
            self._city = input("Введите город: ")
            self._capacity = int(input("Введите вместимость: "))
        except ValueError:
            print("Ошибка ввода данных! Проверьте правильность введенных значений.")
    
    def display_data(self):
        """Метод для вывода данных"""
        print(f"""
        === ИНФОРМАЦИЯ О СТАДИОНЕ ===
        Название: {self._name}
        Дата открытия: {self._opening_date}
        Страна: {self._country}
        Город: {self._city}
        Вместимость: {self._capacity:,} человек
        """)
    
    def get_name(self):
        return self._name
    
    def get_opening_date(self):
        return self._opening_date
    
    def get_country(self):
        return self._country
    
    def get_city(self):
        return self._city
    
    def get_capacity(self):
        return self._capacity
    
    def set_name(self, name):
        self._name = name
    
    def set_opening_date(self, opening_date):
        self._opening_date = opening_date
    
    def set_country(self, country):
        self._country = country
    
    def set_city(self, city):
        self._city = city
    
    def set_capacity(self, capacity):
        if capacity > 0:
            self._capacity = capacity
        else:
            print("Вместимость должна быть положительной!")





def demonstrate_classes():
    
    print("=" * 60)
    print("ДЕМОНСТРАЦИЯ РАБОТЫ КЛАССОВ")
    print("=" * 60)
    
    print("\n1. ДЕМОНСТРАЦИЯ КЛАССА 'АВТОМОБИЛЬ'")
    print("-" * 40)
    
    car1 = Car()
    print("Введите данные об автомобиле:")
    car1.input_data()
    car1.display_data()
    
    print("Использование методов доступа:")
    print(f"Модель: {car1.get_model()}")
    print(f"Цена: ${car1.get_price():,.2f}")
    
    car1.set_price(25000)
    car1.set_color("Синий")
    print("\nПосле изменения данных:")
    car1.display_data()
    
    print("\n2. ДЕМОНСТРАЦИЯ КЛАССА 'КНИГА'")
    print("-" * 40)
    
    book1 = Book()
    print("Введите данные о книге:")
    book1.input_data()
    book1.display_data()
    
    print("Использование методов доступа:")
    print(f"Автор: {book1.get_author()}")
    print(f"Жанр: {book1.get_genre()}")
    
    book1.set_price(15.99)
    book1.set_genre("Роман")
    print("\nПосле изменения данных:")
    book1.display_data()
    
    print("\n3. ДЕМОНСТРАЦИЯ КЛАССА 'СТАДИОН'")
    print("-" * 40)
    
    stadium1 = Stadium()
    print("Введите данные о стадионе:")
    stadium1.input_data()
    stadium1.display_data()
    
    print("Использование методов доступа:")
    print(f"Город: {stadium1.get_city()}")
    print(f"Вместимость: {stadium1.get_capacity():,} человек")
    
    stadium1.set_capacity(80000)
    stadium1.set_name("Новый стадион")
    print("\nПосле изменения данных:")
    stadium1.display_data()

def quick_demo():
    
    print("\n" + "=" * 60)
    print("БЫСТРАЯ ДЕМОНСТРАЦИЯ (без ввода данных)")
    print("=" * 60)
    
    car = Car("Toyota Camry", 2022, "Toyota", 2.5, "Белый", 30000)
    book = Book("Преступление и наказание", 1866, "Русский вестник", "Роман", "Ф.М. Достоевский", 12.99)
    stadium = Stadium("Лужники", "31.07.1956", "Россия", "Москва", 81000)
    
    car.display_data()
    book.display_data()
    stadium.display_data()

if __name__ == "__main__":
    
    demonstrate_classes()
    

    quick_demo()
