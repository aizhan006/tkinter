import tkinter as tk
from tkinter import messagebox

def calculate_dose():
    try:
        weight = float(entry_weight.get())
        dose_per_kg = float(entry_dose.get())
        concentration = float(entry_concentration.get())

        total_dose = weight * dose_per_kg
        volume = total_dose / concentration

        result_label.config(text=f"Общая доза: {total_dose:.2f} мг\nОбъем раствора: {volume:.2f} мл")
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректные числовые значения!")

# Создание окна
root = tk.Tk()
root.title("Калькулятор дозировки лекарств")
root.geometry("350x250")

# Вводные данные
tk.Label(root, text="Вес пациента (кг):").pack()
entry_weight = tk.Entry(root)
entry_weight.pack()

tk.Label(root, text="Доза на кг (мг/кг):").pack()
entry_dose = tk.Entry(root)
entry_dose.pack()

tk.Label(root, text="Концентрация (мг/мл):").pack()
entry_concentration = tk.Entry(root)
entry_concentration.pack()

# Кнопка расчёта
btn_calculate = tk.Button(root, text="Рассчитать", command=calculate_dose)
btn_calculate.pack(pady=10)

# Вывод результата
result_label = tk.Label(root, text="Результат будет здесь", font=("Arial", 12, "bold"))
result_label.pack()

root.mainloop()
