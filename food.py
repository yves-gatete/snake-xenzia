"""Food Class

Represents the food for the snake. Inherits from Turtle and randomly places itself on the screen.
"""

from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """Move the food to a new random location on the screen."""
        x_coordinate = random.randint(-280, 280)
        y_coordinate = random.randint(-280, 280)
        self.goto(x_coordinate, y_coordinate)