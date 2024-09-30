import random
import string
# learn import os

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length)) # generator expression
    return password


password = generate_password(10)
print(f"Generated password: {password}")

# A generator expression is a compact way to create an iterable using a for loop directly within another expression, like in this case within join()

with open('random-module/generated_passwords.txt', 'a') as file:
    file.write(password + '\n')