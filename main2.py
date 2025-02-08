import tkinter as tk
from tkinter import messagebox, simpledialog

# Основное окно
window = tk.Tk()
window.title("Крестики-Нолики")
window.geometry("400x450")
window.configure(bg="lightblue")

# Переменные
current_player = "X"
buttons = []
score = {"X": 0, "O": 0}
win_count = 3

def reset_game():
    global current_player
    current_player = "X"
    for row in buttons:
        for btn in row:
            btn["text"] = ""
    update_score_label()

def update_score_label():
    score_label.config(text=f"Счет: X - {score['X']} | O - {score['O']}")

def check_winner():
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            return buttons[i][0]["text"]
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            return buttons[0][i]["text"]

    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return buttons[0][0]["text"]
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return buttons[0][2]["text"]

    return None

def check_draw():
    return all(btn["text"] != "" for row in buttons for btn in row)

def on_click(row, col):
    global current_player

    if buttons[row][col]["text"] != "":
        return

    buttons[row][col]["text"] = current_player

    winner = check_winner()
    if winner:
        score[winner] += 1
        messagebox.showinfo("Игра окончена", f"Игрок {winner} победил!")
        update_score_label()
        reset_game()
    elif check_draw():
        messagebox.showinfo("Игра окончена", "Ничья!")
        reset_game()
    else:
        current_player = "O" if current_player == "X" else "X"

# Выбор символа игрока
def choose_symbol():
    global current_player
    choice = simpledialog.askstring("Выбор символа", "Выберите ваш символ (X или O):").upper()
    if choice in ["X", "O"]:
        current_player = choice
    else:
        messagebox.showerror("Ошибка", "Неверный ввод! Пожалуйста, выберите X или O.")
        choose_symbol()

# Кнопка сброса
reset_button = tk.Button(window, text="Сбросить игру", font=("Arial", 14), command=reset_game)
reset_button.grid(row=3, column=0, columnspan=3, pady=10)

score_label = tk.Label(window, text="Счет: X - 0 | O - 0", font=("Arial", 14), bg="lightblue")
score_label.grid(row=4, column=0, columnspan=3)

# Создание сетки кнопок
for i in range(3):
    row = []
    for j in range(3):
        btn = tk.Button(window, text="", font=("Arial", 20), width=5, height=2,
                        command=lambda r=i, c=j: on_click(r, c))
        btn.grid(row=i, column=j, padx=5, pady=5)
        row.append(btn)
    buttons.append(row)

choose_symbol()  # Запрос выбора символа

window.mainloop()

# ### Изменения и улучшения:
# 1. **Кнопка сброса** — добавлена кнопка, которая сбрасывает игру.
# 2. **Вариант ничьей** — добавлена проверка ничьей.
# 3. **Улучшение интерфейса** — изменен фон и добавлены отступы для кнопок.
# 4. **Выбор для игрока** — добавлена возможность выбрать символ (X или O)
# перед началом игры.
# 5. **Счетчик побед** — добавлен счетчик побед для каждого игрока.
# 6. **Игра до трех побед** — можно доработать, чтобы отслеживать количество побед
# и завершать игру, когда один из игроков достигнет трех побед.