# задание 1
# import math

# def calculate_circle_area(radius):
#     """Вычисляет площадь круга по заданному радиусу."""
#     if radius < 0:
#         return "Радиус не может быть отрицательным."
    
#     area = math.pi * radius ** 2
#     return area


# задание 2
# def is_prime(number):
#     """Проверяет, является ли число простым."""
#     if number < 2:
#         return False  

#     for i in range(2, int(number**0.5) + 1):
#         if number % i == 0:
#             return False  

#     return True


# user_number = int(input("Введите число: "))


# if is_prime(user_number):
#     print(f"{user_number} - простое число.")
# else:
#     print(f"{user_number} - не простое число.")

# задание 3
# def calculate_triangle_area(base_length, height):
#     """Вычисляет площадь треугольника."""
#     if base_length <= 0 or height <= 0:
#         return "Длина основания и высота треугольника должны быть положительными числами."

#     area = 0.5 * base_length * height
#     return area


# base_length = float(input("Введите длину основания треугольника: "))
# height = float(input("Введите высоту треугольника: "))


# triangle_area = calculate_triangle_area(base_length, height)
# print(f"Площадь треугольника с основанием {base_length} и высотой {height} равна {triangle_area:.2f}.")

# задание 4

# from datetime import datetime, timedelta

# def get_date_after_seven_days():
#     """Возвращает дату через 7 дней от текущей даты."""
#     current_date = datetime.now()
#     date_after_seven_days = current_date + timedelta(days=7)
#     return date_after_seven_days


# current_date = datetime.now()
# date_after_seven_days = get_date_after_seven_days()


# print(f"Текущая дата: {current_date.strftime('%Y-%m-%d')}")
# print(f"Дата через 7 дней: {date_after_seven_days.strftime('%Y-%m-%d')}")

# задание 5
# from datetime import datetime

# def calculate_date_difference(date1, date2):
#     """Вычисляет разницу между двумя датами."""
#     try:
        
#         date1 = datetime.strptime(date1, "%Y-%m-%d")
#         date2 = datetime.strptime(date2, "%Y-%m-%d")

        
#         difference = abs(date2 - date1)

        
#         return difference
#     except ValueError:
#         return "Некорректный формат даты. Используйте формат 'YYYY-MM-DD'."

# # задание 6

# from datetime import datetime

# def get_day_of_week(date_str):
#     """Возвращает день недели для заданной даты."""
#     try:
        
#         date_obj = datetime.strptime(date_str, "%Y-%m-%d")

        
#         day_of_week = date_obj.weekday()

        
#         days_of_week = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
#         day_name = days_of_week[day_of_week]

#         return day_name
#     except ValueError:
#         return "Некорректный формат даты. Используйте формат 'YYYY-MM-DD'."

# задание 7

# import random

# def roll_dice():
#     """Генерирует случайное число от 1 до 6, как на игральной кости."""
#     return random.randint(1, 6)


# target_number = random.randint(1, 6)


# print("Добро пожаловать в игру 'Бросок кости'!")


# input("Нажмите Enter, чтобы бросить кость...")


# result = roll_dice()


# print(f"Выпало число: {result}")


# if result == target_number:
#     print(f"Поздравляем! Вы угадали загаданное число: {target_number}.")
# else:
#     print(f"Увы, не угадали. Загаданное число было: {target_number}.")



