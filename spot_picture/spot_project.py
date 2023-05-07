import turtle as t
from random import choice
from turtle import Screen, Turtle

tim = Turtle()
tim.shape("turtle")
screen = Screen()
screen.screensize(canvheight=200, canvwidth=200)

color_list = [
    (188, 74, 20),
    (56, 34, 13),
    (149, 26, 9),
    (237, 226, 77),
    (202, 164, 110),
    (236, 239, 243),
    (149, 75, 50),
    (232, 227, 214),
    (218, 218, 223),
    (108, 110, 127),
    (214, 153, 89),
    (140, 141, 152),
    (196, 59, 24),
]

t.colormode(255)


tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.goto(-150, 60)
tim.setheading(255)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen.exitonclick()
