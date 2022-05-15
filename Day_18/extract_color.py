
import random
import turtle as turtle_module
tim=turtle_module.Turtle()
turtle_module.colormode(255)
color_list=[(153, 14, 63), (190, 153, 21), (165, 46, 130), (17, 139, 65), (29, 85, 177), (163, 92, 27)]


tim.speed('fastest')
tim.hideturtle()
tim.setheading(220)
tim.penup()
tim.forward(350)
tim.setheading(0)
num_of_dot=100

for i in range(1,num_of_dot+1):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)
    if i%10==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen=turtle_module.Screen()
screen.exitonclick()