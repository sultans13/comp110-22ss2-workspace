"""EX01 - Chardle - A cute step toward Wordle.""" 


__author__ = "730485451"
from operator import indexOf


five_character_word: str = input("Enter a 5-character word:")
if len(five_character_word) != 5:
    print(exit)
single_character: str = input("Enter a single character:")
if len(single_character) != 1:
    print(exit)
times: int = 0
print("Searching for " + single_character + " in " + five_character_word)
if five_character_word[0] == single_character:
    print(single_character + " found at index [0] ")
    times += 1 
if five_character_word[1] == single_character:
    print(single_character + " found at index [1] ")
    times += 1
if five_character_word[2] == single_character:
    print(single_character + " found at index [2] ")
    times += 1
if five_character_word[3] == single_character:
    print(single_character + " found at index [3] ")
    times += 1
if five_character_word[4] == single_character:
    print(single_character + " found at index [4] ")
    times += 1 
number_of_matching: int = str(times) 
if times == 0: 
    print("No instances of " + single_character + " found in " + five_character_word) 
if times == 1:
    print(number_of_matching + " intance of " + single_character + " found in " + five_character_word)
else:
    print(number_of_matching + " intances of " + single_character + " found in " + five_character_word)






