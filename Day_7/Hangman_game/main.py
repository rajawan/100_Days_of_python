import random
from Hangman_art import stages
from Hangman_words import word_list
chosen_word=random.choice(word_list)
word_length=len(chosen_word)
display=["_" for letter in chosen_word ]
end_of_game=True
lives=6
while end_of_game:
    guess=input("Guess a letter: ").lower()
    for position in range(word_length):
        if chosen_word[position] ==guess:
            display[position]=guess
    if guess not in chosen_word:
        print(f'you choose {guess} not in the word')
        lives-=1
        if lives == 0:
            end_of_game=False
            print("You lose")
    print(f"{''.join(display)}")
    if "_" not in display:
        end_of_game=False
        print("You Win")
    print(stages[lives])