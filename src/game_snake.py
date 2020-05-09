import tkinter as tk
from random import randint, choice

WIDTH = 500
HEIGHT = 400

# TODO Запретить змейке разворачиваться на 360 градусов
# TODO Запретить змее пересекать саму себя
# TODO Проверять чтояблоко создается не внутри змеи

class Snake:
    def __init__(self):
        self.sell_width = 10
        self.dx = -self.sell_width
        self.dy = 0

        self.snake_body = [[WIDTH/2, HEIGHT/2],
                           [WIDTH/2+self.sell_width, HEIGHT/2],
                           [WIDTH/2 + 2*self.sell_width, HEIGHT/2]]
        # self.snake_head = self.snake_body[0]

        canvas.bind('<Up>', lambda event: self.change_direction(0, -self.sell_width))
        canvas.bind('<Down>', lambda event: self.change_direction(0, self.sell_width))
        canvas.bind('<Left>', lambda event: self.change_direction(-self.sell_width, 0))
        canvas.bind('<Right>', lambda event: self.change_direction(self.sell_width, 0))
        canvas.focus_set()

        self.draw_snake(self.snake_body)

    def draw_snake(self, snake_body):
        color = "lawn green"
        count = 0
        for body in snake_body:
            canvas.create_rectangle(body,
                                    body[0] + self.sell_width, body[1] + self.sell_width,
                                    fill=color,
                                    tags="snake_id_" + str(count))
            count += 1

    def erase_snake(self):
        count = 0
        for _ in self.snake_body:
            canvas.delete("snake_id_" + str(count))
            count += 1

    def move(self):
        snake_head = self.snake_body[0]
        new_head = [snake_head[0] + self.dx, snake_head[1] + self.dy]

        self.snake_body.insert(0, new_head)
        self.snake_body.pop()
        self.erase_snake()
        self.draw_snake(self.snake_body)

    def change_direction(self, *args):
        self.dx = args[0]
        self.dy = args[1]

    def grow(self):
        print(self.snake_body)
        g_dx = self.snake_body[-2][0] - self.snake_body[-1][0]
        g_dy = self.snake_body[-2][1] - self.snake_body[-1][1]

        self.snake_body.append([self.snake_body[-1][0] + g_dx, self.snake_body[-1][1] + g_dy])
        self.draw_snake(self.snake_body)

    def check_border(self):
        snake_head = self.snake_body[0]
        if snake_head[0] < 0 or \
                snake_head[0] >= WIDTH or \
                snake_head[1] < 0 or \
                snake_head[1] >= HEIGHT:
            return True
        else:
            return False

    def check_collision_apple(self):
        snake_head = self.snake_body[0]
        coord_apple = canvas.coords(apple)
        if snake_head[0] == coord_apple[0] and \
                snake_head[1] == coord_apple[1]:
            return True
        else:
            return False


def motion():
    snake.move()

    if snake.check_border():
        game_over()
    elif snake.check_collision_apple():
        print("Collision")
        snake.grow()
        canvas.delete('apple')
        create_apple()
        root.after(120, motion)
    else:
        root.after(120, motion)


def start_game():
    global snake
    canvas.delete("all")
    snake = Snake()
    create_apple()
    motion()


def game_over():
    canvas.create_text(WIDTH/2, HEIGHT/2, text="Game over!!!", justify="center", font="Verdana 14")
    canvas.update()
    root.after(2000, start_game())


def create_apple():
    global apple
    x = randint(snake.sell_width * 2, WIDTH - snake.sell_width * 2)
    y = randint(snake.sell_width * 2, HEIGHT - snake.sell_width * 2)
    # Отбрасываем остаток, что бы яблоко всегда располагалось в клетках, по которым движется змейка
    x -= x % 10
    y -= y % 10

    apple = canvas.create_rectangle(x, y,
                                    x + snake.sell_width, y + snake.sell_width,
                                    fill="orange red", tags="apple")


def main():
    global root, canvas
    global menu

    root = tk.Tk()

    canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
    canvas.pack(side='bottom')

    # menu = Menu()

    start_game()

    root.mainloop()


if __name__ == '__main__':
    main()
