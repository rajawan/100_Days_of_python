import random
user_card=[]
computer_card=[]
is_game_over=False
def del_card():
    cards=[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card=random.choice(cards)
    return card
for _ in range(2):
    user_card.append(del_card())
    computer_card.append(del_card())
def sum(cards):
    score=0
    for num in cards:
        score+=num
    return score

def calculate_score(card_list):
    if sum(card_list)==21:
        return 0
    if 11 in card_list and sum(card_list)>21:
        card_list.remove(11)
        card_list.append(1)
    return sum(card_list)
while not is_game_over:
    user_score=calculate_score(user_card)
    computer_score=calculate_score(computer_card)
    print(f'{user_card} your Score is: {user_score}')
    print(f'computer first card {computer_card[0]}')
    if user_score==0 or computer_score==0 or user_score>21:
        is_game_over=True
    else:
        user_choice=input("Type 'y' to get another card: ")
    if user_choice=='y':
        user_card.append(del_card())
    else:
        is_game_over=True

while computer_score!=0 and computer_score<17:
    computer_card.append(del_card())
    computer_score=calculate_score(computer_card)

def compare_score(user_score,com_score):
    if user_score==com_score:
        print("It's draw")
    elif com_score==0:
        print("computer wins the game")
    elif user_score==0:
        print("User Wins the game")
    elif user_score>21:
        print("Computer wins the game")
    elif com_score>21:
        print("User Wins the game")
    elif user_score>com_score:
        print("User Win")
    else:
        print("Computer win")

compare_score(user_score,computer_score)
print(computer_score)