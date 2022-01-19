from turtle import Turtle
import random


class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.pu()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.new_food_location()

    def new_food_location(self):
        random_x = random.randint(-250, 250)
        random_y = random.randint(-250,250)
        self.goto(random_x,random_y)