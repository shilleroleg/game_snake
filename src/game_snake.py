import tkinter as tk
import time
from random import randint, choice

WIDTH = 500
HEIGHT = 400


class Snake:
    def __init__(self):
        self.sell_width = 10
        self.dx = -self.sell_width
        self.dy = 0

        self.snake_body = [[WIDTH/2, HEIGHT/2],
                           [WIDTH/2+self.sell_width, HEIGHT/2],
                           [WIDTH/2 + 2*self.sell_width, HEIGHT/2]]

        # canvas.bind('<Up>', lambda event: self.change_direction(0, -2))
        # canvas.bind('<Down>', lambda event: self.change_direction(0, 2))
        # canvas.bind('<Left>', lambda event: self.change_direction(-2, 0))
        # canvas.bind('<Right>', lambda event: self.change_direction(2, 0))
        canvas.bind('<Button-1>', lambda event: self.change_direction(0, -self.sell_width))

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

    def move(self):
        snake_head = self.snake_body[0]
        new_head = [snake_head[0] + self.dx, snake_head[1] + self.dy]

        self.snake_body.insert(0, new_head)
        self.snake_body.pop()
        canvas.delete("all")
        self.draw_snake(self.snake_body)

    def change_direction(self, *args):
        # print(args[0])
        self.dx = args[0]
        self.dy = args[1]
        # self.dx = 0
        # self.dy = -2

    def grow(self):
        pass

    def check_border(self):
        snake_head = self.snake_body[0]
        if snake_head[0] <= 0 or \
                snake_head[0] >= WIDTH or \
                snake_head[1] <= 0 or \
                snake_head[1] >= HEIGHT:
            return True
        else:
            return False


def motion():

    snake.move()

    if snake.check_border():
        game_over()
    else:
        root.after(100, motion)


def start_game():
    global snake
    snake = Snake()
    motion()


def game_over():
    # FIXME Don't work correctly
    canvas.create_text(WIDTH/2, HEIGHT/2, text="Game over!!!", justify="center", font="Verdana 14")
    time.sleep(2)
    # canvas.delete(game_over_text)
    start_game()


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
