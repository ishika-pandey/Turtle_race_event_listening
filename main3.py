import turtle
from turtle import Turtle, Screen
from random import randint
tim= Turtle()
turtle.colormode(255)
current= tim.heading()
tim.speed("fastest")

def size_of_gap(n):
    global current
    for i in range(int(360/n)):
        r=randint(0,255)
        g = randint(0, 255)
        b = randint(0, 255)
        tim.color(r,g,b)
        tim.circle(100)
        current += n
        tim.setheading(current)
size_of_gap(5)
    #tim.heading() += tim.heading()+i
screen= Screen()
screen.exitonclick()
