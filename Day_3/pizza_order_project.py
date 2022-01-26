print("Welcome to the python pizza delivery app")
#Get the pizza size from user
size=input("What size of pizza do you want? S, M, L\n ")
add_Pepperoni=input("Do you want pepperoni? Y or N\n ")
extra_chess=input("Do you want extra chess? Y or N\n ")
bill=0

if size=='s':
    bill=15
    if add_Pepperoni=='y':
        bill+=2
elif size=='m':
    bill=20
    if add_Pepperoni=='y':
        bill+=3

elif size=='l':
    bill=25
    if add_Pepperoni=='y':
        bill+=3
print("Invalid input")

if extra_chess=='y':
    bill+=1