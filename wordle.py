import wordle_engine
import random
import sys

# Print a greeting
print(wordle_engine.welcome_string())

# Load the list of valid words
valid_words = wordle_engine.load_words("combined_wordlist.txt")
#print(valid_words)
# Use the target word provided on the command line, 
# or, choose a random word if no target word given.
if len(sys.argv) >= 2:
    target = sys.argv[1]
else:
    # TODO choose a random word from valid_words
    target = 'noles' # <== change this

guesses = []
full_word_dict = wordle_engine.create_letter_status()
attempts=6
while(attempts >0):
    guess = input("Make a guess ({}) :".format(wordle_engine.format_letters(full_word_dict))).lower()

    if len(guess) == 5 :
        guesses.append(wordle_engine.format_guess(target,guess))
        full_word_dict = wordle_engine.update_letter_status(full_word_dict,target,guess)
        k=1
        for word in guesses:
            print("{}. {}".format(k,word))
            k=k+1
        if guess == target:
            print("Congratulations, you won!")
            break
        else:
            print("Incorrect guess. You have {} guesses left.".format(attempts-1))
        attempts -=1
    else:
        print("Invalid guess. Please enter a 5-letter word from the word list.")    
else:
    print("You've run out of attempts. The word was:", target)
