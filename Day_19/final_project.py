from turtle import Turtle,Screen
import random
is_race_on=False

color=['red','green','blue','yellow','orange','purple']
y_position=[-70,-40,-10,20,50,80]
screen=Screen()
screen.setup(500,400)
choice=screen.textinput(title='Enter Your bid',prompt='Which turtle will win the race? Enter a color? ')
all_turtle=[]
for index in range(0,6):
    tim=Turtle(shape='turtle')
    tim.penup()
    tim.color(color[index])
    tim.goto(x=-220,y=y_position[index])
    all_turtle.append(tim)

if choice:
    is_race_on=True

while is_race_on:
    for turtle in all_turtle:
        turtle.forward(random.randint(0,10))
        wining_color=turtle.pencolor()
        if turtle.xcor()>230:
            is_race_on=False
            if wining_color==choice:
                print(f'{choice } win the race')
            else:
                print(f'{wining_color} win the race')
            


screen.exitonclick()