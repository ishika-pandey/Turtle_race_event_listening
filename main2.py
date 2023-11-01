import turtle
from turtle import Turtle, Screen
from random import choice, randint
tim= Turtle()
tim.pensize(15)
turtle.colormode(255)
tim.speed("fastest")
for i in range(200):
    number=[0,90,180,270]
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    tim.pencolor(r, g, b)
    tim.forward(30)
    tim.right(choice(number))

screen= Screen()
screen.exitonclick()