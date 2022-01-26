# 🚨 Don't change the code below 👇
from ast import Break


height = int(input("What is your height "))
# 🚨 Don't change the code above 👆
#Write your code below this line 👇
ticket=0
# if number%2==0:
#   print("This is an even number")
# else:
#   print("This is an odd number")



if height>=120:
  print("You can ride the rollercoster")
  age=int(input("What is your age? "))
  if age <= 12:
    ticket=5
    print(f"Your ticket price ${ticket}")
  elif age <= 18:
    ticket=7
    print(f"Your ticket price ${ticket}")
  elif age<=55 and age>=45:
    ticket=0
    print(f"Your ticket price ${ticket}")
    Break
  else:
    ticket=12
    print(f"Your ticket price ${ticket}")
  want_photo=input("Do you want to took a photto? Y or N. ")
  if want_photo=="y":
    ticket += 3
  
  print(f"Your final ticket price is ${ticket}")

else:
  print("You cannot ride the rollercester") 

