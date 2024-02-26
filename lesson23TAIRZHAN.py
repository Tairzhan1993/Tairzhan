# задание 1

# import tkinter as tk


# def greet():
#     label_text.set("Привет, " + name_entry.get() + "!")


# def farewell():
#     label_text.set("Пока, " + name_entry.get() + "!")


# root = tk.Tk()
# root.title("Простой интерфейс")


# name_label = tk.Label(root, text="Введите ваше имя:")
# name_label.pack()


# name_entry = tk.Entry(root)
# name_entry.pack()


# label_text = tk.StringVar()


# greeting_label = tk.Label(root, textvariable=label_text)
# greeting_label.pack()


# hello_button = tk.Button(root, text="Привет", command=greet)
# hello_button.pack()


# goodbye_button = tk.Button(root, text="Пока", command=farewell)
# goodbye_button.pack()


# root.mainloop()

# задание 2


# def copy_text():
#     text_area.delete(1.0, tk.END)  
#     text = text_entry.get()         
#     text_area.insert(tk.END, text)  


# root = tk.Tk()
# root.title("Текстовое поле и текстовая область")


# text_entry = tk.Entry(root, width=50)
# text_entry.pack()


# text_area = tk.Text(root, width=50, height=10)
# text_area.pack()


# copy_button = tk.Button(root, text="Копировать текст", command=copy_text)
# copy_button.pack()


# root.mainloop()