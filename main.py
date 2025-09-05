from turtle import Screen, Turtle

#screen properties
screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake Xenzia")

#squares are 20 units length
starting_positions = [(0,0), (-20,0), (-40,0)]
for pos in starting_positions:  
    segment = Turtle("square")
    segment.color("white")
    segment.setposition(pos)




screen.exitonclick()