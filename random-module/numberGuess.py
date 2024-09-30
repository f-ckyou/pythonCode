import random

def start():
    number_to_guess = random.randint(1,20)
    inpt = None
    attempt = 0

    while inpt != number_to_guess:
        inpt = int(input("Guess a number b/w 1 and 20: "))
        attempt += 1;
        if inpt < number_to_guess:
            print("Go high!")
        elif inpt > number_to_guess:
            print("Go less!")

    print(f"You did in {attempt} attempts.")

start()