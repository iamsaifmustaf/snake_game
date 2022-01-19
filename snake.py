from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0



class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def exit_game(self):
        exit()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_square(position)

    def add_square(self,position):
        ##add new square to snake
        square = Turtle()
        square.shape("square")
        square.color("white")
        square.pu()
        square.speed(0)
        square.goto(position)
        self.snake_body.append(square)
    
    def extend(self):
        self.add_square(self.snake_body[-1].pos())

    def move(self):
        for square_num in range(len(self.snake_body) - 1, 0 , -1):
            self.snake_body[square_num].goto(self.snake_body[square_num - 1].pos())

        self.head.forward(MOVE_DISTANCE)

    def move_right(self):
        if self.head.heading() == LEFT:
            return()
        self.head.setheading(RIGHT)
    
    def move_up(self):
        if self.head.heading() == DOWN:
            return()
        self.head.setheading(UP)
                
    def move_left(self):
        if self.head.heading() == RIGHT:
            return()
        self.head.setheading(LEFT)
    
    def move_down(self):
        if self.head.heading() == UP:
            return()
        self.head.setheading(DOWN)
