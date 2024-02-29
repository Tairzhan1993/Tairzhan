# задание 1
# import tkinter as tk
# from tkinter import ttk


# def update_label(event):
#     selected_item = listbox.get(listbox.curselection()) 
#     label.config(text=selected_item)                     

# root = tk.Tk()
# root.title("Выбор элементов")


# list_frame = tk.Frame(root)
# list_frame.pack(side=tk.LEFT, padx=10, pady=10)


# listbox = tk.Listbox(list_frame, width=20, height=5)
# listbox.pack()


# for item in ["Элемент 1", "Элемент 2", "Элемент 3", "Элемент 4", "Элемент 5"]:
#     listbox.insert(tk.END, item)


# listbox.bind("<<ListboxSelect>>", update_label)


# combo_frame = tk.Frame(root)
# combo_frame.pack(side=tk.RIGHT, padx=10, pady=10)


# label = tk.Label(combo_frame, text="")
# label.pack()


# combo = ttk.Combobox(combo_frame, values=["Опция 1", "Опция 2", "Опция 3"])
# combo.pack()


# root.mainloop()