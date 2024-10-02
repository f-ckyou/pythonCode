''' 
- another way to time the program is to use time.time(), which returns an epoch timestamp ( since January 1, 1970, 00:00:00 UTC )
'''


import time
start_time = time.time()

''' The sys module in Python provides functions and variables to interact with the Python interpreter and the system environment '''
import sys

''' 
Whenever you load an external file, your program should automatically
check for I/O issues, like missing files or incorrect filenames, and let you
know if there is a problem.
'''
def load(text_file):
    # Open a text file & return a list of lowercase strings
    try:
        with open(text_file) as file:
            loaded_txt = file.read().strip().split('\n')
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as e:
        print(f'{e}\nError opening {text_file}', file=sys.stderr)
        sys.exit()

word_list = load('palindrome/words2.txt') # http://greenteapress.com/thinkpython2/code/words.txt


# find word pair palingrams
def find_pallingrams():
    pallingram_list = []
    ''' 
        - Sets, in particular, are significantly faster than lists when using the in keyword. 
        - Sets use a hashtable for very fast lookups. With hashing, strings of text are converted to unique numbers that are much smaller than the referenced text and much more efficient to search.
    '''
    words = set(word_list)
    for word in words:
        end = len(word)
        reverse_word = word[::-1]
        if end > 1:
            for i in range(end):
                if word[i:] == reverse_word[:end-i] and reverse_word[end-i:] in word_list:
                    pallingram_list.append((word, reverse_word[end-i:]))
                # Check for the second form of palingram: word[:i] == reverse[end-i:]
                if word[:i] == reverse_word[end-i:] and reverse_word[:end-i] in word_list:
                    pallingram_list.append((reverse_word[:end-i], word))
    return pallingram_list

palingrams = find_pallingrams()
palingrams_sorted = sorted(palingrams)  # Sort the pairs alphabetically by the first word

# display list of palingrams
print(f"\nNumber of palingrams = {len(palingrams_sorted)}")

for first,second in palingrams_sorted: # Loop through and print each palingram pair
    print(f"{first} {second}")

end_time = time.time()
print(f"Runtime for this program was {end_time - start_time} seconds")