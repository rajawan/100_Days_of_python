import turtle as t
import random


my_turtle=t.Turtle()
t.colormode(255)

#Draw shape Challenge 2

# def draw_shape(num_of_slides):
#     angle=360/num_of_slides
#     for _ in range(num_of_slides):
#         my_turtle.forward(100)
#         my_turtle.right(angle)

# for i in range(3,10):
#     draw_shape(i)

#Draw random walk
def random_colors():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_color = (r,g,b)
    return random_color


# directions=[0,90,180,237]
# for _ in range(200):
#     my_turtle.color(random_colors())
#     my_turtle.forward(38)
#     my_turtle.setheading(random.choice(directions))
my_turtle.pensize(3)
for _ in range(200):
    my_turtle.color(random_colors())
    my_turtle.circle(100)
    current_heading=my_turtle.heading()
    my_turtle.setheading(current_heading+70)

screen=t.Screen()
screen.exitonclick()