# задание 1
# from datetime import datetime, timedelta

# class Event:
#     def __init__(self, name, date):
#         self.name = name
#         self.date = date

# class Calendar:
#     def __init__(self):
#         self.events = []

#     def add_event(self, event):
#         self.events.append(event)

#     def remove_event(self, event_name):
#         self.events = [e for e in self.events if e.name != event_name]

#     def events_on_date(self, date):
#         return [event for event in self.events if event.date == date]

#     def upcoming_events(self, days=90):
#         today = datetime.now()
#         end_date = today + timedelta(days=days)
#         upcoming_events = [event for event in self.events if today <= event.date <= end_date]
#         upcoming_events.sort(key=lambda x: x.date)
#         return upcoming_events


# calendar = Calendar()


# event1 = Event("Встреча с другом", datetime(2023, 12, 1))
# event2 = Event("Презентация проекта", datetime(2023, 12, 15))
# event3 = Event("Праздничный обед", datetime(2024, 1, 5))

# calendar.add_event(event1)
# calendar.add_event(event2)
# calendar.add_event(event3)


# upcoming_events = calendar.upcoming_events()
# for event in upcoming_events:
#     print(f"{event.name} - {event.date}")

# задание 2
# def calculate_total_value(self):
#         """Рассчитывает общую стоимость товара в инвентаре."""
#         return self.quantity * self.price


# item1 = InventoryItem("Лаптоп", 10, 800)  
# item2 = InventoryItem("Мышь", 50, 20)


# item1.increase_quantity(5)
# item2.increase_quantity(10)


# item1.decrease_quantity(3)
# item2.decrease_quantity(60)  

# total_value = item1.calculate_total_value() + item2.calculate_total_value()
# print(f"Общая стоимость товара в инвентаре: ${total_value}")

# задание 3
# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.subjects = {}
    
#     def add_grade(self, subject, grade):
#         """Добавляет оценку по предмету."""
#         if subject not in self.subjects:
#             self.subjects[subject] = []
#         self.subjects[subject].append(grade)
    
#     def add_grades(self, subject, grades):
#         """Добавляет список оценок по предмету."""
#         if subject not in self.subjects:
#             self.subjects[subject] = []
#         self.subjects[subject].extend(grades)
    
#     def calculate_average_grade(self):
#         """Вычисляет средний балл студента."""
#         total_grades = 0
#         total_subjects = 0

#         for subject, grades in self.subjects.items():
#             total_grades += sum(grades)
#             total_subjects += len(grades)

#         if total_subjects == 0:
#             return 0  

#         return total_grades / total_subjects


# student1 = Student("Иван Иванов")
# student1.add_grade("Математика", 90)
# student1.add_grades("Физика", [85, 88, 92])
# student1.add_grade("Литература", 78)

# average_grade = student1.calculate_average_grade()
# print(f"Средний балл студента {student1.name}: {average_grade}")

# задание 4
# class TicTacToe:
#     def __init__(self):
#         self.board = [" "] * 9  

#     def display_board(self):
#         """Отображает текущее состояние игрового поля."""
#         for i in range(0, 9, 3):
#             print(f"{self.board[i]} | {self.board[i+1]} | {self.board[i+2]}")
#             if i < 6:
#                 print("---------")

#     def make_move(self, position, player):
#         """Делает ход игрока."""
#         if 1 <= position <= 9 and self.board[position-1] == " ":
#             self.board[position-1] = player
#             return True
#         else:
#             print("Неверный ход. Попробуйте еще раз.")
#             return False

#     def check_winner(self):
#         """Проверяет, есть ли победитель."""
#         win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

#         for condition in win_conditions:
#             if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] != " ":
#                 return True, self.board[condition[0]]

#         return False, None

#     def is_board_full(self):
#         """Проверяет, заполнено ли игровое поле."""
#         return " " not in self.board


# game = TicTacToe()

# current_player = "X"
# winner = False

# while not winner and not game.is_board_full():
#     game.display_board()
#     try:
#         position = int(input(f"Игрок {current_player}, введите номер ячейки (1-9): "))
#     except ValueError:
#         print("Введите корректное число.")
#         continue

#     if game.make_move(position, current_player):
#         winner, winning_player = game.check_winner()
#         if winner:
#             print(f"Победил игрок {winning_player}!")
#         else:
#             current_player = "O" if current_player == "X" else "X"

# if not winner:
#     print("Ничья!")