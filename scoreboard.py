"""
Scoreboard Class

Handles the display and updating of the score, as well as the game over message.
"""

from turtle import Turtle

ALIGNEMENT = "left"
FONT = 'Arial'

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(-60, 270)
        self.hideturtle()
        self.update_scoreboard()
    
    def update_score(self):
        """Increase the score by 1 and update the display."""
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        """Write the current score on the screen."""
        self.write(f"Score: {self.score}", move=False, align=ALIGNEMENT, font=(FONT, 16, "normal"))

    def game_over(self):
        """Display the game over message."""
        self.goto(-60, 0)
        self.write("GAME OVER :(", move=False, align=ALIGNEMENT, font=(FONT, 18, "normal"))
