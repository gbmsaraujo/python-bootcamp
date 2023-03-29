import turtle
from turtle import Turtle, Screen
from random import choice, randint

tim = Turtle()
turtle.colormode(255)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)

    return r, g, b


directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")


def random_walk():
    for i in range(100):
        tim.color(random_color())
        tim.forward(30)
        tim.setheading(choice(directions))


random_walk()

screen = Screen()
screen.exitonclick()
