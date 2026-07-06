import turtle
screen = turtle.Screen()
my_turtle = turtle.Turtle()

for _ in range(4):
    my_turtle.forward(100)
    my_turtle.right(90)

screen.exitonclick()
