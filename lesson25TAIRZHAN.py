# # # задание 1
# # # import tkinter as tk


# # # def update_label():
# # #     selected_options = [option.get() for option in check_var]  
# # #     label.config(text="Выбранные опции: " + ", ".join(selected_options))  


# # # root = tk.Tk()
# # # root.title("Выбор опций")


# # # check_frame = tk.Frame(root)
# # # check_frame.pack(padx=10, pady=10)


# # # check_var = [tk.StringVar() for _ in range(3)]


# # # options = ["Опция 1", "Опция 2", "Опция 3"]
# # # check_buttons = [tk.Checkbutton(check_frame, text=option, variable=check_var[i], onvalue=option, offvalue="", command=update_label) for i, option in enumerate(options)]


# # # for button in check_buttons:
# # #     button.pack(anchor=tk.W)


# # # label = tk.Label(root, text="Выбранные опции:")
# # # label.pack(anchor=tk.W, padx=10, pady=(20, 0))


# # # root.mainloop()

# # Задание 2

# # import tkinter as tk


# # def update_label():
# #     selected_options = []
# #     for group in check_groups:
# #         for button in group:
# #             if button.get():
# #                 selected_options.append(button["text"])
# #     label.config(text="Выбранные опции: " + ", ".join(selected_options))


# # root = tk.Tk()
# # root.title("Выбор опций")


# # check_groups = []


# # frame1 = tk.Frame(root)
# # frame1.pack(padx=10, pady=10, anchor=tk.W)


# # var1 = [tk.BooleanVar() for _ in range(3)]


# # options1 = ["Опция 1", "Опция 2", "Опция 3"]
# # check_buttons1 = [tk.Checkbutton(frame1, text=option, variable=var1[i], onvalue=True, offvalue=False, command=update_label) for i, option in enumerate(options1)]


# # check_groups.append(check_buttons1)


# # for button in check_buttons1:
# #     button.pack(anchor=tk.W)


# # frame2 = tk.Frame(root)
# # frame2.pack(padx=10, pady=10, anchor=tk.W)


# # var2 = [tk.BooleanVar() for _ in range(2)]


# # options2 = ["Опция А", "Опция Б"]
# # check_buttons2 = [tk.Checkbutton(frame2, text=option, variable=var2[i], onvalue=True, offvalue=False, command=update_label) for i, option in enumerate(options2)]


# # check_groups.append(check_buttons2)


# # for button in check_buttons2:
# #     button.pack(anchor=tk.W)


# # label = tk.Label(root, text="Выбранные опции:")
# # label.pack(anchor=tk.W, padx=10, pady=(20, 0))


# # root.mainloop()

# Задание 3
# import tkinter as tk
# from tkinter import ttk


# def handle_selection():
#     selected_options = []
#     for option, value in options.items():
#         if value.get():
#             selected_options.append(option)
#     result_label.config(text=f"Выбранные опции: {', '.join(selected_options)}")


# root = tk.Tk()
# root.title("Выбор опций")


# options = {}


# for i, (option_text, style) in enumerate([("Опция 1", "primary"), ("Опция 2", "danger"), ("Опция 3", "success"), ("Опция 4", "warning")]):
#     options[option_text] = tk.BooleanVar()
#     check_button = ttk.Checkbutton(root, text=option_text, variable=options[option_text], style=f.TCheckbutton, command=handle_selection)
#     check_button.grid(row=i, column=0, sticky="w", padx=10, pady=5)


# result_label = ttk.Label(root, text="Выбранные опции: ")
# result_label.grid(row=len(options), column=0, sticky="w", padx=10, pady=5)


# style = ttk.Style()
# style.configure("primary.TCheckbutton", foreground="blue")
# style.configure("danger.TCheckbutton", foreground="red")
# style.configure("success.TCheckbutton", foreground="green")
# style.configure("warning.TCheckbutton", foreground="orange")


# root.mainloop()
