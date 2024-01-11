# задание 1
# def add(x, y):
#     """Сложение"""
#     return x + y

# def subtract(x, y):
#     """Вычитание"""
#     return x - y

# def multiply(x, y):
#     """Умножение"""
#     return x * y

# def divide(x, y):
#     """Деление"""
#     if y != 0:
#         return x / y
#     else:
#         return "Деление на ноль недопустимо"
    
    
# from Match_operation import add, subtract, multiply, divide


# num1 = float(input("Введите первое число: "))
# num2 = float(input("Введите второе число: "))


# sum_result = add(num1, num2)
# diff_result = subtract(num1, num2)
# prod_result = multiply(num1, num2)
# div_result = divide(num1, num2)


# print(f"Сумма: {sum_result}")
# print(f"Разность: {diff_result}")
# print(f"Произведение: {prod_result}")
# print(f"Деление: {div_result}")

# # задание 2
# def count_words(text):
#     """Подсчитывает количество слов в тексте."""
#     if not text:
#         return 0

#     words = text.split()
#     return len(words)

# def capitalize_first_letter(sentence):
#     """Преобразует первую букву каждого слова в предложении в заглавную."""
#     words = sentence.split()
#     capitalized_words = [word.capitalize() for word in words]
#     return ' '.join(capitalized_words)

# def reverse_text(text):
#     """Обращает порядок символов в тексте."""
#     return text[::-1]


# from Data_operations import count_words, capitalize_first_letter, reverse_text


# user_text = input("Введите текст: ")


# word_count = count_words(user_text)
# capitalized_sentence = capitalize_first_letter(user_text)
# reversed_text = reverse_text(user_text)


# print(f"Количество слов в тексте: {word_count}")
# print(f"Предложение с заглавной первой буквой: {capitalized_sentence}")
# print(f"Обращенный текст: {reversed_text}")

# задание 3
# student.py

# class Student:
#     """Класс, представляющий студента."""

#     def __init__(self, name, age):
#         """Инициализация атрибутов студента."""
#         self.name = name
#         self.age = age

#     def display_info(self):
#         """Вывод информации о студенте."""
#         print(f"Имя: {self.name}, Возраст: {self.age}")

        
# from student import Student


# student1 = Student("Иван", 20)


# student1.display_info()

# задание 4
# import math

# class Circle:
#     """Класс, представляющий круг."""

#     def __init__(self, radius):
#         """Инициализация атрибутов круга."""
#         self.radius = radius

#     def area(self):
#         """Вычисление площади круга."""
#         return math.pi * self.radius ** 2
    
#     class Rectangle:
#     """Класс, представляющий прямоугольник."""

#     def __init__(self, width, height):
#         """Инициализация атрибутов прямоугольника."""
#         self.width = width
#         self.height = height

#     def area(self):
#         """Вычисление площади прямоугольника."""
#         return self.width * self.height
    
    
# from shapes.Circle import Circle
# from shapes.Rectangle import Rectangle


# circle = Circle(radius=5)
# rectangle = Rectangle(width=4, height=6)


# print(f"Площадь круга: {circle.area():.2f}")
# print(f"Площадь прямоугольника: {rectangle.area()}")

# задание 5

