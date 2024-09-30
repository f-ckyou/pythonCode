import random

def roll_dice():
    return random.randint(1,6) # returning a random integer b/w 1 and 6

for i in range(5): # dice is rolling five times: 0,1,2,3,4 not 5 
    print(f"{i} dice rolled: {roll_dice()}")