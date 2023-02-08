#Step 1 
import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

display = []

for char in chosen_word:
    display += "_"

guess = input("Guess a letter:\n").lower()

#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
### this first block of code was my first attemp and it worked but I had a feeling it was
### not the solution Dr. Angela Yu <3 was looking for. She mentioned that looking up range
### functions might help and I noticed that I did not have any range functions in my code,
### it took me a little bit but I think this is exactly what she wanted.
# display_number = -1
# for char in chosen_word:
#     display_number += 1
#     if char == guess:
#         display[display_number] = guess
for char in range(len(chosen_word)):
    if guess == chosen_word[char]:
        display[char] = guess

#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
print(display)