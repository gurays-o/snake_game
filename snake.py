from turtle import Turtle

STARTING_LENGTH = 3
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_container = []
        self.head = None
        self.create_snake()

    def add_segment(self, position):
        new_turtle = Turtle("square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(position)
        self.snake_container.append(new_turtle)

    def create_snake(self):
        for i in range(STARTING_LENGTH):
            position = (i * -20, 0)
            self.add_segment(position)
            self.head = self.snake_container[0]

    def grow(self):
        self.add_segment(self.snake_container[-1].position())

    def move(self):
        segments = len(self.snake_container) - 1
        # segments: count of snake segments which will follow each other, i.e. all segments but the head of snake.
        for i in range(segments):
            self.snake_container[segments - i].goto(self.snake_container[segments - 1 - i].position())
        self.head.forward(MOVE_DISTANCE)

    def reset_snake(self):
        for seg in self.snake_container:
            seg.goto(1000, 1000)
            seg.hideturtle()
        self.snake_container.clear()
        self.create_snake()

    def up(self):
        current_heading = self.head.heading()
        if current_heading != DOWN:
            self.head.setheading(UP)

    def down(self):
        current_heading = self.head.heading()
        if current_heading != UP:
            self.head.setheading(DOWN)

    def left(self):
        current_heading = self.head.heading()
        if current_heading != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        current_heading = self.head.heading()
        if current_heading != LEFT:
            self.head.setheading(RIGHT)
