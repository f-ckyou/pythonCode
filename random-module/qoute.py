import random

def get_random_quote(file_path):
    with open(file_path, 'r') as file: 
        # The readlines() method separates lines based on newline characters because that is how lines are defined in text files and store them in a list
        quote_list = file.readlines() 

    '''
     .strip() method
     it removes any leading and trailing whitespace from a string
    '''
    quote_list = [quote.strip() for quote in quote_list]  # creates a new list by iterating over an existing list (quote_list) and applying the strip() method to each element

    return random.choice(quote_list)    # returns any random element from the list, every element is a "qoute"


file_path = 'random-module/quotes.txt' # https://gist.github.com/robatron/a66acc0eed3835119817

print(get_random_quote(file_path))