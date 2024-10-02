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


# word_list = load('palindrome/words.txt') # http://greenteapress.com/thinkpython2/code/words.txt
word_list = load('palindrome/words_alpha.txt') # https://raw.githubusercontent.com/dwyl/english-words/refs/heads/master/words_alpha.txt
pallindrome_list = []

for word in word_list:
    if len(word) > 1 and word == word[::-1]:
        pallindrome_list.append(word)
    
print(f"\nNumber of palindromes found = {len(pallindrome_list)}\n")

# printing every pallindromes

''' we can do by looping through every word in the list,
    but there is more efficient way to do it '''

print(*pallindrome_list, sep='\n') # use the splat operator(*,**)
''' These operators are useful for handling variable-length argument lists and unpacking arguments from collections like lists, tuples, and dictionaries. '''
