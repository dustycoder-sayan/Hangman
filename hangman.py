# implementing a guessing game like hangman

import random
import os
from hangman_conditions import single_letter_check, stages

print("Let's play Hangman!!")
name = input("Enter your name: ")
print("\nAll the best, {}!!\n".format(name))

wrong_guess_limit = 7       # Hangman ends at 7 wrong guesses

selected_word = ""
with open(os.path.abspath('.\\Hangman\\words.txt'), "r") as word:   # calling file containing words - words.txt
    words1 = word.read()
    wordl = words1.split()
    selected_word = random.choice(wordl)            # selecting random word form the file


prev_guess=""                                       # To store the letters already entered by player
s=list("*"*len(selected_word))
print(" ".join(s))
while "".join(s) != selected_word:
    print()
    next_guess = single_letter_check("ar")
    if single_letter_check(next_guess):
        if next_guess in selected_word:
            print("\nYou've guessed it right!!")
            for index, letter in enumerate(selected_word):      # replace entered correct letters in the word expressed with *
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
            print(stages(wrong_guess_limit))                    # prints hangman stage by stage
        if wrong_guess_limit == 0:
            print("Your chances are done!")
            break
else:
    print("You guessed it right!")                          # prints when loop doesn't break out, i.e, user entered the word correctly
