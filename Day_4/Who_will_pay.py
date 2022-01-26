import random

name_string=input("Enter everybody's name separated by coma: ")
#make a list from the string using split function
names=name_string.split(",")
#select a name randomly using random function 
random_number=random.randint(0,len(names)-1)
payer_name=names[random_number]
print(f"{payer_name} is going to buy the meal today!")
