import random

def get_random_quote(file_path):
    with open(file_path, 'r') as file: 
        quote_list = file.readlines() 

    quote_list = [quote.strip() for quote in quote_list]

    return random.choice(quote_list)


file_path = 'random-module/quotes.txt' 

show_quote = get_random_quote(file_path)

print(f"Quote of the Day: \n'{show_quote}'")
