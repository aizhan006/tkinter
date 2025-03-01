import tkinter as tk
import random
from tkinter import messagebox
import time

# Данные о лекарствах
data = {
    "Парацетамол": {
        "Класс": "Анальгетик",
        "Показания": "Головная боль, жар, боль в мышцах",
        "Дозировка": "500 мг каждые 6 часов",
        "Побочные эффекты": "Тошнота, аллергия, нарушение функции печени"
    },
    "Ибупрофен": {
        "Класс": "НПВС",
        "Показания": "Боль, воспаление, жар",
        "Дозировка": "200-400 мг каждые 4-6 часов",
        "Побочные эффекты": "Боль в животе, изжога, тошнота"
    }
}


def show_loading_screen():
    loading_frame.pack(expand=True, fill='both')
    root.update()
    time.sleep(2)  # Имитация загрузки
    loading_frame.pack_forget()
    show_title_screen()


def show_title_screen():
    title_frame.pack(expand=True, fill='both')


def start_app():
    title_frame.pack_forget()
    main_screen.pack(expand=True, fill='both')


def search_med():
    med_name = entry.get()
    med_info = data.get(med_name)
    result_frame.pack_forget()
    if med_info:
        result_text.set(f"📌 {med_name}\n\n"
                        f"🧪 Класс: {med_info['Класс']}\n"
                        f"✅ Показания: {med_info['Показания']}\n"
                        f"💊 Дозировка: {med_info['Дозировка']}\n"
                        f"⚠ Побочные эффекты: {med_info['Побочные эффекты']}")
        result_frame.pack(pady=10)
    else:
        result_text.set("❌ Лекарство не найдено.")
        result_frame.pack(pady=10)


def show_medicine_info(med_name):
    med_info = data[med_name]
    messagebox.showinfo(med_name, f"🧪 Класс: {med_info['Класс']}\n\n"
                                  f"✅ Показания: {med_info['Показания']}\n\n"
                                  f"💊 Дозировка: {med_info['Дозировка']}\n\n"
                                  f"⚠ Побочные эффекты: {med_info['Побочные эффекты']}")


def show_game_screen():
    game_window = tk.Toplevel(root)
    game_window.title("Мини-игра")
    game_window.geometry("400x300")
    game_label = tk.Label(game_window, text="Мини-игра: составь название лекарства", font=("Arial", 14))
    game_label.pack(pady=10)

    word = random.choice(list(data.keys()))
    shuffled_word = list(word)
    random.shuffle(shuffled_word)
    shuffled_word = ''.join(shuffled_word)

    question_label = tk.Label(game_window, text=f"Составьте слово: {shuffled_word}", font=("Arial", 12))
    question_label.pack(pady=5)

    entry_game = tk.Entry(game_window, font=("Arial", 12))
    entry_game.pack(pady=5)

    def check_answer():
        if entry_game.get() == word:
            messagebox.showinfo("Правильно!", "Вы правильно составили название лекарства!")
        else:
            messagebox.showerror("Ошибка", "Неправильно! Попробуйте ещё раз.")

    check_button = tk.Button(game_window, text="✅ Проверить", font=("Arial", 12), command=check_answer)
    check_button.pack(pady=5)


root = tk.Tk()
root.title("MedFarm")
root.geometry("400x600")
root.configure(bg="#E0F7FA")

# Экран загрузки
loading_frame = tk.Frame(root, bg="#E0F7FA")
loading_label = tk.Label(loading_frame, text="Загрузка...", font=("Arial", 24, "bold"), fg="#00796B", bg="#E0F7FA")
loading_label.pack(expand=True)

# Титульный экран
title_frame = tk.Frame(root, bg="#E0F7FA")
title_label = tk.Label(title_frame, text="💊 MedFarm", font=("Arial", 24, "bold"), fg="#00796B", bg="#E0F7FA")
title_label.pack(pady=20)
start_button = tk.Button(title_frame, text="Начать", font=("Arial", 14), command=start_app)
start_button.pack()

# Главный экран
main_screen = tk.Frame(root, bg="#E0F7FA")
search_label = tk.Label(main_screen, text="🔍 Поиск", font=("Arial", 18, "bold"), fg="#00796B", bg="#E0F7FA")
search_label.pack(pady=10)
entry = tk.Entry(main_screen, font=("Arial", 14))
entry.pack(pady=5)
search_button = tk.Button(main_screen, text="🔎 Найти", font=("Arial", 14), command=search_med)
search_button.pack(pady=5)

result_text = tk.StringVar()
result_frame = tk.Frame(main_screen, bg="#E0F7FA")
result_label = tk.Label(result_frame, textvariable=result_text, font=("Arial", 12), wraplength=350, justify="left",
                        fg="#00796B", bg="#E0F7FA")
result_label.pack(pady=5)

med_list_frame = tk.Frame(main_screen, bg="#E0F7FA")
for med in data.keys():
    btn = tk.Button(med_list_frame, text=med, font=("Arial", 12), command=lambda m=med: show_medicine_info(m))
    btn.pack(pady=5)
med_list_frame.pack(pady=10)

# Кнопка "Мини-игра"
game_button = tk.Button(main_screen, text="🎮 Мини-игра", font=("Arial", 14), command=show_game_screen)
game_button.pack(pady=10)

show_loading_screen()
root.mainloop()
