import load_dictionary

word_list = load_dictionary.load('palindrome/words.txt')

anagram_list = []

''' input a single word to find its anagram(s) '''
name = 'dealer'.lower()

''' sort names & find anagrams '''
name_sorted = sorted(name)
for word in word_list:
    word = word.lower()
    if word != name:
        if sorted(word) == name_sorted:
            anagram_list.append(word)

''' print all the anagrams '''
print()
if len(anagram_list) == 0:
    print("need a larger dictionary or a new input!")
else:
    print("Anagrams =", *anagram_list, sep='\n')