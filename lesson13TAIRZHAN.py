# # задание 1
# class Car:
#     """Класс, представляющий автомобиль."""

#     def __init__(self, brand, model, year):
#         """Инициализация атрибутов автомобиля."""
#         self.brand = brand
#         self.model = model
#         self.year = year

#     def description(self):
#         """Вывод информации о машине."""
#         print(f"{self.year} {self.brand} {self.model}")

#         from car import Car


# my_car = Car(brand="Toyota", model="Camry", year=2022)


# my_car.description()

# # задание 2

# # person.py

# class Person:
#     """Класс, представляющий человека."""

#     def __init__(self, name, age):
#         """Инициализация атрибутов человека."""
#         self.name = name
#         self.age = age

# class Employee(Person):
#     """Класс, представляющий сотрудника."""

#     def __init__(self, name, age, salary):
#         """Инициализация атрибутов сотрудника."""
#         super().__init__(name, age)
#         self.salary = salary

#     def get_info(self):
#         """Вывод информации о сотруднике."""
#         print(f"Имя: {self.name}, Возраст: {self.age}, Зарплата: {self.salary}")

        
# from person import Employee


# employee = Employee(name="John Doe", age=30, salary=50000)


# employee.get_info()

# задание 3
# class Animal:
#     """Класс, представляющий животное."""

#     def speak(self):
#         """Метод для издания звука."""
#         pass  

# class Dog(Animal):
#     """Подкласс, представляющий собаку."""

#     def speak(self):
#         """Метод для издания звука собаки."""
#         return "Гав!"

# class Cat(Animal):
#     """Подкласс, представляющий кошку."""

#     def speak(self):
#         """Метод для издания звука кошки."""
#         return "Мяу!"

# from animal import Dog, Cat




# dog = Dog()
# cat = Cat()


# print("Звук собаки:", dog.speak())
# print("Звук кошки:", cat.speak())