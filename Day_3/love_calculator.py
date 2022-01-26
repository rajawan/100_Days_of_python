# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combined_str=name1+name2
lower_case_str=combined_str.lower()

#find how many times TRUE word occours in the both name
t= lower_case_str.count("t")
r= lower_case_str.count("r")
u= lower_case_str.count("u")
e= lower_case_str.count("e")
#Add the value
true=t+r+u+e

#find how many times LOVE word occours in the both name
l= lower_case_str.count("l")
o= lower_case_str.count("o")
v= lower_case_str.count("v")
e= lower_case_str.count("e")

#Add the value
love= l+o+v+e

#Store the total score
score=str(true) + str(love)

#Print the score with desire messege using logical operator
if score < '10' or score > '90':
  print(f"Your score is {score}, you go together like coke and mentos. ")
elif score>='40' and score <='50':
  print(f"Your score is {score}, you are alright together")
else:
  print(f"Your score {score}")