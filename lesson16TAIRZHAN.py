# задание 1
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def introduce(self):
#         print(f"Привет, меня зовут {self.name} и мне {self.age} лет.")


# person1 = Person("Иван", 25)
# person1.introduce()

# person2 = Person("Мария", 30)
# person2.introduce()


# задание 2

# class Product:
#     def __init__(self, name, initial_price=0.0):
#         self.name = name
#         self.description = ""
#         self.price = initial_price

#     def add_description(self, description):
        
#         self.description = description

#     def set_price(self, price):
        
#         if price >= 0:
#             self.price = price
#         else:
#             print("Цена не может быть отрицательной.")

#     def display_product_info(self):
        
#         print(f"Название: {self.name}")
#         print(f"Описание: {self.description}")
#         print(f"Цена: ${self.price:.2f}")


# product1 = Product("Ноутбук", 1200.0)
# product1.add_description("Мощный ноутбук с высокой производительностью.")
# product1.display_product_info()

# print("\n")

# product2 = Product("Смартфон", 500.0)
# product2.add_description("Современный смартфон с отличной камерой.")
# product2.set_price(550.0)  
# product2.display_product_info()


# Задание 3
# class Book:
#     def __init__(self, title, author, publication_year):
#         self.title = title
#         self.author = author
#         self.publication_year = publication_year
#         self.is_available = True

#     def checkout(self):
#         if self.is_available:
#             print(f"Книга '{self.title}' взята в аренду.")
#             self.is_available = False
#         else:
#             print(f"Извините, книга '{self.title}' уже взята в аренду.")

#     def checkin(self):
#         if not self.is_available:
#             print(f"Книга '{self.title}' успешно возвращена.")
#             self.is_available = True
#         else:
#             print(f"Книга '{self.title}' уже находится в библиотеке.")

#     def display_info(self):
#         availability = "доступна" if self.is_available else "недоступна"
#         print(f"Название: {self.title}")
#         print(f"Автор: {self.author}")
#         print(f"Год публикации: {self.publication_year}")
#         print(f"Статус: {availability}")


# book1 = Book("Мастер и Маргарита", "Михаил Булгаков", 1967)
# book1.display_info()
# book1.checkout()

# print("\n")

# book2 = Book("1984", "Джордж Оруэлл", 1949)
# book2.display_info()
# book2.checkout()
# book2.checkin()
# book2.checkout()
