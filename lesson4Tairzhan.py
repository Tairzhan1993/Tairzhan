# x = int(input ("введите число:"))
# if x > 0:
#     print ("положительное число")
# elif x == 0:
#     print ("число является нулём")
# else:
#     print ("отрицательно число")

# user_input = input("Введите число от 1 до 5: ")
# try:
#     user_number = int(user_input)
#     if 1 <= user_number <= 5:
#         if user_number == 1:
#             print("Вы ввели число 1. Это один.")
#         elif user_number == 2:
#             print("Вы ввели число 2. Это два.")
#         elif user_number == 3:
#             print("Вы ввели число 3. Это три.")
#         elif user_number == 4:
#             print("Вы ввели число 4. Это четыре.")
#         else:
#             print("Вы ввели число 5. Это пять.")
#     else:
#         print("Число не входит в допустимый диапазон.")
# except ValueError:
#     print("Ошибка: Введите корректное число от 1 до 5.")

# # Получаем ввод от пользователя
# user_input = input("Введите число от 1 до 4: ")

# # Пытаемся преобразовать ввод пользователя в целое число
# try:
#     user_number = int(user_input)
    
#     # Проверяем, что введенное число находится в диапазоне от 1 до 4
#     if 1 <= user_number <= 4:
#         # Определяем четверть
#         if user_number == 1:
#             print("Введенное число находится в первой четверти.")
#         elif user_number == 2:
#             print("Введенное число находится во второй четверти.")
#         elif user_number == 3:
#             print("Введенное число находится в третьей четверти.")
#         elif user_number == 4:
#             print("Введенное число находится в четвертой четверти.")
#     else:
#         print("Число не входит в допустимый диапазон.")
# except ValueError:
#     print("Ошибка: Введите корректное число от 1 до 4.")


# user_input = input("Введите число: ")

# try:
    
#     user_number = int(user_input)
#     if user_number > 0 and user_number % 2 == 0:
#         print("Введенное число является положительным и четным.")
#     else:
#         print("Введенное число не является положительным и/или четным.")
# except ValueError:
#     print("Ошибка: Введите корректное число.")

# # Получаем ввод от пользователя
# user_input = input("Введите год: ")

# try:
#     # Преобразуем ввод пользователя в целое число
#     year = int(user_input)

#     # Проверяем, является ли год високосным
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         print(f"{year} год является високосным.")
#     else:
#         print(f"{year} год не является високосным.")
# except ValueError:
#     print("Ошибка: Введите корректный год.")


# # Получаем ввод от пользователя
# user_input = input("Введите ваш возраст: ")

# try:
#     age = int(user_input)
#     if age > 18 and age <= 45:
#         print("Вам можно пройти на матч.")
#     else:
#         print("Ваш возраст не соответствует условиям для прохода на матч.")
# except ValueError:
#     print("Ошибка: Введите корректный возраст.")
