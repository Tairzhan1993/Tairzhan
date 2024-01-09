# задание 1

# matrix_a = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# matrix_b = [
#     [9, 8, 7],
#     [6, 5, 4],
#     [3, 2, 1]
# ]


# def add_matrices(mat_a, mat_b):
#     result = []
#     for i in range(len(mat_a)):
#         row = []
#         for j in range(len(mat_a[0])):
#             row.append(mat_a[i][j] + mat_b[i][j])
#         result.append(row)
#     return result


# print("Матрица A:")
# for row in matrix_a:
#     print(row)

# print("\nМатрица B:")
# for row in matrix_b:
#     print(row)


# result_matrix = add_matrices(matrix_a, matrix_b)


# print("\nРезультат сложения матриц A и B:")
# for row in result_matrix:
#     print(row)



# задание 2

# catalog_dict = {
#     'кино': ['фильм1', 'фильм2', 'фильм3'],
#     'музыка': ['альбом1', 'альбом2', 'альбом3']
# }


# def add_catalog(genre, catalog_name):
    
#     if genre in catalog_dict:
        
#         catalog_dict[genre].append(catalog_name)
#         print(f"Каталог '{catalog_name}' успешно добавлен в жанр '{genre}'.")
#     else:
#         print(f"Жанр '{genre}' отсутствует в каталоге.")


# print("Исходный словарь:")
# print(catalog_dict)


# add_catalog('кино', 'новый_фильм')
# add_catalog('музыка', 'новый_альбом')
# add_catalog('спорт', 'новый_каталог_спорт')


# print("\nОбновленный словарь:")
# print(catalog_dict)

# задание 3

# books_dict = {
#     'Книга1': {'Автор': 'Автор1', 'Год выпуска': 2020, 'Жанр': 'Фантастика'},
#     'Книга2': {'Автор': 'Автор2', 'Год выпуска': 2015, 'Жанр': 'Детектив'},
#     'Книга3': {'Автор': 'Автор1', 'Год выпуска': 2018, 'Жанр': 'Роман'},
#     'Книга4': {'Автор': 'Автор3', 'Год выпуска': 2022, 'Жанр': 'Поэзия'},
# }


# def search_by_author(author):
#     found_books = []
#     for book, info in books_dict.items():
#         if info['Автор'] == author:
#             found_books.append((book, info))
#     return found_books


# print("Исходный словарь:")
# for book, info in books_dict.items():
#     print(f"{book}: {info}")


# author_search_result = search_by_author('Автор1')


# print("\nРезультат поиска по автору 'Автор1':")
# for book, info in author_search_result:
#     print(f"{book}: {info}")

# задание 4

# students_grades = {
#     'Студент1': [85, 90, 78, 92, 88],
#     'Студент2': [75, 88, 92, 84, 90],
#     'Студент3': [90, 85, 89, 78, 95],
    
# }


# def calculate_average(grades):
#     if not grades:
#         return 0  
#     return sum(grades) / len(grades)


# def calculate_all_averages(students_grades):
#     averages = {}
#     for student, grades in students_grades.items():
#         averages[student] = calculate_average(grades)
#     return averages


# print("Исходный словарь с оценками:")
# for student, grades in students_grades.items():
#     print(f"{student}: {grades}")


# average_grades = calculate_all_averages(students_grades)


# print("\nСредние оценки студентов:")
# for student, average_grade in average_grades.items():
#     print(f"{student}: {average_grade}")

# задание 5
