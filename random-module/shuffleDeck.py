import random

def create_():
    cards = ['dil', 'it', 'chiriya', 'paan']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'chutiya', 'randi', 'raja', 'ekka']
    gaddi = [f'{card} ka {value}' for value in values for card in cards]
    return gaddi

def shuffling(gaddi):
    random.shuffle(gaddi)
    return gaddi


gaddi = create_()
shuffled_ = shuffling(gaddi)
print("Shuffled Deck:")
print(shuffled_[:5]) 