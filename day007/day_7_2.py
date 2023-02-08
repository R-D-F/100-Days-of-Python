#Step 1 
import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks (""). Then you can tell the usert they've won.

display = []

for char in chosen_word:
    display += "_"

### this is the eazy solution using the join function which we haven't learned yet

# while ''.join(display) != chosen_word:
#     guess = input("Guess a letter:\n").lower()


#     for char in range(len(chosen_word)):
#         if guess == chosen_word[char]:
#             display[char] = guess

#     print(display)
# print("You win!")

### this is the hard solution using a for loop to creat a list of the letters in the chosen word then compare that list to the display. Now that I think about it you could do this the opposite way as well by creating a string out of the display and seeing if that string matches the chosen word. Actually I am sure that is what she wants so im gonna do that one sec.
# chosen_word_list = []
# for char in chosen_word:
#     chosen_word_list += char

# while display != chosen_word_list:
#     guess = input("Guess a letter:\n").lower()


#     for char in range(len(chosen_word)):
#         if guess == chosen_word[char]:
#             display[char] = guess

#     print(display)
        
# print("You win!")

### im pretty sure this is what she wants. nvm she wants us to use the IN function. Man there are a lot of ways to accomplis the same thing. That is good because I was about to try for a long time to get the display to update to a string, and check if that string was = to the chosen word. I still think it is possible but it would not have been pretty.



# while "_" in display:
#     guess = input("Guess a letter:\n").lower()


#     for char in range(len(chosen_word)):
#         if guess == chosen_word[char]:
#             display[char] = guess

#     print(display)
        
# print("You win!")

### okay im going to try the not pretty solution again I think I can do it.
### It is a little ugly but it does work. just involves resetting display_string back to an empty string every time you need to assign it value or else the string just becomes a conglomeration of letters and blanks ("_")

# display_str = ""

# while display_str != chosen_word:
#     guess = input("Guess a letter:\n").lower()


#     for char in range(len(chosen_word)):
#         if guess == chosen_word[char]:
#             display[char] = guess
#             display_str = ""
#             for char in display:
#                 display_str += char


#     print(display)
        
# print("You win!")

### despite me doing 5 different solutions she has a slightly different one

end_of_game = False

while end_of_game == False:
    guess = input("Guess a letter:\n").lower()


    for char in range(len(chosen_word)):
        if guess == chosen_word[char]:
            display[char] = guess

    print(display)

    if "_" not in display:
        end_of_game = True
        
print("You win!")
