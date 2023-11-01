from turtle import Turtle, Screen,colormode
import random
colormode(255)

tim= Turtle()
for n in range(3,11):
    r= random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tim.color(r,g,b)
    for i in range(n):
        tim.forward(100)
        tim.right(360/n)
screen = Screen()
screen.exitonclick()

