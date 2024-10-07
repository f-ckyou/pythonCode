import math

'''
num = input("Enter an integer: ")

# exception handling
try:
    number = int(num)
    print(f"Entered Integer is: {number}")

    
    if number < 2:
        print("Not prime")  
    else:
        is_prime = True
        for i in range(2, int(math.sqrt(number)) + 1):  
            if number % i == 0:
                is_prime = False
                break  
        
        if is_prime:
            print("Prime")
        else:
            print("Not prime")

except ValueError:
    print("Invalid Input")

'''

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# Lists to hold primes and non-primes
primes = []
non_primes = []

# Check numbers in the range only once
for i in range(100):
    if is_prime(i):
        primes.append(i)
    else:
        non_primes.append(i)

print("Prime numbers:", primes)
print("Non-prime numbers:", non_primes)
 