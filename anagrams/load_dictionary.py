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

