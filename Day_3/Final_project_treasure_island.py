print("Welcome to my treasure island game project")
print("Your mission is to find the treasure.")
#create your own story to find treasure

option=input("Choose L for left or R right. ")

if option=='L':
    seocend_option=input("Choose S for swim and W for wait. ")
    if seocend_option=='W':
        third_option=input("Choose the right door\n. Y for yellow\n. R for red\n. B for blue.")
        if third_option=='Y':
            print("Hurray! You win the treasure")
        else:
            print("You die")
    else:
        print("You were eaten by Shark. And lost the game.")

else:
    print("Game over. you fall into a hall")