import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

user_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
computer_choice=random.randint(0,2)

if user_choice==computer_choice:
    print("It's Draw")
elif user_choice==0 and computer_choice==2:
    print("You win")
elif user_choice==2 and computer_choice==0:
    print("You loss")