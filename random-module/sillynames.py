import random

first = ('Pal', 'Sagnik', 'Shubham', 'Aryan', 'Aashutosh', 'Dealer', 'Kattappa', 'Pratik', 'Piyush', 'Tathagat', 'Zoro')

last = ('gandu', 'madarchod', 'betichod', 'bhosdiwala', 'bharwa', 'chikna', 'panauti')

firstname = random.choice(first)
lastname = random.choice(last)

print(f"{firstname} {lastname}")