import tkinter as tk
import random

# Размеры окна
WIDTH = 500
HEIGHT = 500
CELL_SIZE = 20

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Змейка")
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()

        self.snake = [(100, 100), (90, 100), (80, 100)]  # Начальная змейка
        self.food = self.create_food()
        self.direction = "Right"

        self.root.bind("<KeyPress>", self.change_direction)
        self.update_game()

    def create_food(self):
        x = random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE
        y = random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
        return (x, y)

    def change_direction(self, event):
        key = event.keysym
        if key == "Up" and self.direction != "Down":
            self.direction = "Up"
        elif key == "Down" and self.direction != "Up":
            self.direction = "Down"
        elif key == "Left" and self.direction != "Right":
            self.direction = "Left"
        elif key == "Right" and self.direction != "Left":
            self.direction = "Right"

    def update_game(self):
        head_x, head_y = self.snake[0]

        if self.direction == "Up":
            head_y -= CELL_SIZE
        elif self.direction == "Down":
            head_y += CELL_SIZE
        elif self.direction == "Left":
            head_x -= CELL_SIZE
        elif self.direction == "Right":
            head_x += CELL_SIZE

        new_head = (head_x, head_y)

        # Проверка на столкновение
        if (
            head_x < 0 or head_x >= WIDTH or
            head_y < 0 or head_y >= HEIGHT or
            new_head in self.snake
        ):
            self.game_over()
            return

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.food = self.create_food()
        else:
            self.snake.pop()

        self.draw_objects()
        self.root.after(100, self.update_game)

    def draw_objects(self):
        self.canvas.delete("all")
        for x, y in self.snake:
            self.canvas.create_rectangle(x, y, x + CELL_SIZE, y + CELL_SIZE, fill="green")

        food_x, food_y = self.food
        self.canvas.create_rectangle(food_x, food_y, food_x + CELL_SIZE, food_y + CELL_SIZE, fill="red")

    def game_over(self):
        self.canvas.create_text(WIDTH // 2, HEIGHT // 2, text="Game Over", fill="white", font=("Arial", 24))

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
