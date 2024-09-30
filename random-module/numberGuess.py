import random

def start():
    number_to_guess = random.randint(1,20) # randomly creating any integer b/w 1 to 20
    inpt = None
    attempt = 0

    while inpt != number_to_guess: # loop will not end until the user input matches with the randomly selected integer
        inpt = int(input("Guess a number b/w 1 and 20: "))
        attempt += 1;
        if inpt < number_to_guess: # user needs to increase the value of his guessed integer
            print("Go high!")
        elif inpt > number_to_guess:
            print("Go less!")      # user needs to decrease the value of his guessed integer

    print(f"You did in {attempt} attempts.")

start()