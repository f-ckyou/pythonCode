import random

def roll_dice():
    return random.randint(1,6)

for i in range(5):
    print(f"{i} dice rolled: {roll_dice()}")