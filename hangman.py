# implementing a guessing game like hangman

import random
import os
from hangman_conditions import single_letter_check, stages      

print("Let's play Hangman!!")
name = input("Enter your name: ")
print("\nAll the best, {}!!\n".format(name))

# Hangman ends at 7 wrong guesses
wrong_guess_limit = 7       

selected_word = ""

# calling file containing words and selecting a random word - words.txt
with open(os.path.abspath('.\\Hangman\\words.txt'), "r") as word:   
    words1 = word.read()
    wordl = words1.split()
    selected_word = random.choice(wordl)            

# To store the previous guessed by the player
prev_guess=""

# would display the letter not guessed and letters guessed in serial order
s=list("*"*len(selected_word))                      
print(" ".join(s))
while "".join(s) != selected_word:
    print()
    
    # check if the string input has a single character and repeat procedure if letter entered is not a single character
    next_guess = single_letter_check("ar")          
    if single_letter_check(next_guess):
        if next_guess in selected_word:
            print("\nYou've guessed it right!!")
            for index, letter in enumerate(selected_word):     
                if letter == next_guess:
                    s[index] = letter                   
            print(" ".join(s))
            print(wrong_guess_limit)
            prev_guess += next_guess+" "                
            print("Previous guesses: ", prev_guess)
        else:
            print("\nWrong entry!")
            wrong_guess_limit -= 1
            prev_guess += next_guess+" "
            print("Previous guesses: ", prev_guess)
            print(" ".join(s))
            print(wrong_guess_limit)
            print(stages(wrong_guess_limit))                    
        if wrong_guess_limit == 0:
            print("Your chances are done!")
            break
else:
    print("You guessed it right!")                          
# prints when loop doesn't break out, i.e, user entered the word correctly
