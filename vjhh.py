from tkinter import *
from tkinter import ttk

def calculate(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        if operation == "+":
            result.set(num1 + num2)
        elif operation == "-":
            result.set(num1 - num2)
        elif operation == "*":
            result.set(num1 * num2)
        elif operation == "/":
            if num2 != 0:
                result.set(num1 / num2)
            else:
                result.set("Error (division by 0)")
    except ValueError:
        result.set("Error")

root = Tk()
root.geometry("400x400")  # Set window width and height
root.title("MY CALCULATOR")

# Title label
label = ttk.Label(root, text="My Calculator", font=("Arial", 16, "bold"))
label.pack(pady=10)

# Input fields
entry1 = ttk.Entry(root, width=12, font=("Arial", 16), justify="center")
entry1.pack(pady=5)

entry2 = ttk.Entry(root, width=12, font=("Arial", 16), justify="center")
entry2.pack(pady=5)

# Result field
result = StringVar()
label_result = ttk.Label(root, textvariable=result, font=("Arial", 18, "bold"))
label_result.pack(pady=10)

# Buttons for operations
frame_buttons = Frame(root)
frame_buttons.pack(pady=10)

btn_style = {"width": 6, "height": 3, "font": ("Arial", 16, "bold")}  # Button style

btn_add = Button(frame_buttons, text="+", command=lambda: calculate("+"), **btn_style)
btn_add.grid(row=0, column=0, padx=5, pady=5)

btn_sub = Button(frame_buttons, text="-", command=lambda: calculate("-"), **btn_style)
btn_sub.grid(row=0, column=1, padx=5, pady=5)

btn_mul = Button(frame_buttons, text="*", command=lambda: calculate("*"), **btn_style)
btn_mul.grid(row=1, column=0, padx=5, pady=5)

btn_div = Button(frame_buttons, text="/", command=lambda: calculate("/"), **btn_style)
btn_div.grid(row=1, column=1, padx=5, pady=5)

root.mainloop()
