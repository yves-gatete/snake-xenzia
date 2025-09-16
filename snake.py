"""
Snake Class

Handles the creation, movement, growth, and direction of the snake.
Segments are Turtle objects stored in a list. The head is always self.segments[0].
"""

from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        """Initialize the snake with starting segments and set the head."""
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Create the initial snake body from starting positions."""
        for pos in STARTING_POSITIONS:
            self.add_segment(pos)

    def add_segment(self, position):
        """Add a new segment to the snake at the given position."""
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def grow(self):
        """Grow the snake by adding a segment to the tail."""
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Move the snake forward by updating each segment's position."""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Change direction to up unless currently moving down."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Change direction to down unless currently moving up."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Change direction to left unless currently moving right."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Change direction to right unless currently moving left."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)