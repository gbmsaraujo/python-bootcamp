from turtle import Turtle, Screen

tim = Turtle()
tim.shape("arrow")
tim.color("red")

def draw_square():
    for _ in range(4):
        tim.forward(100)
        tim.right(90)


for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()


screen = Screen()
screen.exitonclick()
