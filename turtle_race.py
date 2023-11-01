from turtle import Turtle,Screen
import random

screen=Screen()
bet=screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter the color: ")
screen.setup(width=500,height=800)
y=300
colours=["red","orange","yellow","green","blue","purple"]
turtle_list=[]
for i in range(6):
    tim=Turtle(shape="turtle")
    tim.color(colours[i])
    tim.penup()
    tim.goto(-230,y)
    y -= 100
    turtle_list.append(tim)

if bet:
    start=True


while start:
    for i in turtle_list:

        if i.xcor()>210:
            win=i.pencolor()
            if win==bet:
                print(f"You've won.The {i.pencolor()} colour turtle won the race" )
            else:
                print(f"You've lost.The {i.pencolor()} colour turtle won the race")
            start=False
        distance = random.randint(5, 15)
        i.forward(distance)

screen.exitonclick()