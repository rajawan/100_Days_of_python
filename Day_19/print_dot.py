from turtle import Turtle, Screen
import turtle
color=[(153, 14, 63), (190, 153, 21), (165, 46, 130), (17, 139, 65), (29, 85, 177), (163, 92, 27)]
myturtle=Turtle()
myturtle.setheading(220)
myturtle.forward(350)
myturtle.setheading(0)
for i in range(10):
    myturtle.dot(20)
    myturtle.forward(50)


screen=Screen()
screen.exitonclick()