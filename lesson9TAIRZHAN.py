# # Создаем словарь с информацией о студентах
# students = {
#     'Иванов': {'Возраст': 20, 'Курс': 2, 'Средний балл': 4.5},
#     'Петров': {'Возраст': 21, 'Курс': 3, 'Средний балл': 4.0},
#     'Сидорова': {'Возраст': 19, 'Курс': 1, 'Средний балл': 4.8}
# }

# # Функция для вывода информации о студенте по имени
# def print_student_info(name):
#     if name in students:
#         info = students[name]
#         print(f'Имя: {name}, Возраст: {info["Возраст"]}, Курс: {info["Курс"]}, Средний балл: {info["Средний балл"]}')
#     else:
#         print(f'Студент с именем {name} не найден.')

# # Функция для удаления студента по имени
# def delete_student(name):
#     if name in students:
#         del students[name]
#         print(f'Студент {name} удален.')
#     else:
#         print(f'Студент с именем {name} не найден.')

# # Пример использования функций
# print_student_info('Иванов')

# # Удаление студента по имени
# delete_student('Петров')

# # Вывод информации о студентах после удаления
# print('\nИнформация о студентах после удаления:')
# for name in students:
#     print_student_info(name)



# # Создаем список элементов
# list_of_elements1 = [1, 2, 3, 4, 5]
# list_of_elements2 = [3, 4, 5, 6, 7]

# # Создаем множества из списков
# set1 = set(list_of_elements1)
# set2 = set(list_of_elements2)

# # Определение пересечения двух множеств
# intersection = set1.intersection(set2)

# # Определение объединения двух множеств
# union = set1.union(set2)

# # Вывод результатов
# print(f"Множество 1: {set1}")
# print(f"Множество 2: {set2}")

# print(f"\nПересечение: {intersection}")
# print(f"Объединение: {union}")


# countries_and_cities = {}

# while True:
#     country = input("Введите название страны (или 'exit' для завершения): ")
    
#     if country.lower() == 'exit':
#         break
    
#     cities_input = input("Введите города через запятую: ")
#     cities = [city.strip() for city in cities_input.split(',')]
    
#     countries_and_cities[country] = cities

# # Вывод полученного словаря
# print("\nСловарь стран и городов:")
# for country, cities in countries_and_cities.items():
#     print(f"{country}: {', '.join(cities)}")

Name = "Tairzhan"