import random

def create_():
    cards = ['dil', 'it', 'chiriya', 'paan']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'chutiya', 'randi', 'raja', 'ekka'] # each value of values is for each card in cards
    gaddi = [f'{card} ka {value}' for value in values for card in cards] # creates all 52 cards in an order
    return gaddi 

def shuffling(gaddi):
    random.shuffle(gaddi) # ye gaddi phete-ga
    return gaddi


gaddi = create_()
shuffled_ = shuffling(gaddi) # shuffled deck
print("Shuffled Deck:")
print(shuffled_[:4]) # prints first four card of the shuffled deck | everytime it will be different