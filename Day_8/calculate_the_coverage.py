import math
def paint_calc(height,width,coverage):
    area=height*width
    num_of_cans=math.ceil(area/coverage)
    print(f"you will need {num_of_cans} cans for paint ")

height=int(input("Enter your Wall height: \n"))
width=int(input("Enter your wall weight: \n"))
coverage=5
paint_calc(height=height,width=width,coverage=coverage)