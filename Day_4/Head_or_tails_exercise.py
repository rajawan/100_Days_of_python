from cgi import test
from importlib import import_module
import random

print("Welcome to our coin flip game")
test_seed=int(input("Create a strong seed number: "))
random.seed(test_seed)
number=random.randint(0,1)
#Create the logic for this game
if number==1:
    print("Heads")
else:
    print("tails")