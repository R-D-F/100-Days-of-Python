### debugging
### Steps for debugging
### 1. Describe the Problem

############DEBUGGING#####################

# Describe Problem
### This function is meant to print "You got it" once i reaches the end of it's range. However the end of it's range is 19, not 20 because the range function is not inclusive. If you want i to print at i == 20, you will need to make the range range(1, 21)
# def my_function():
#   for i in range(1, 20):
#     if i == 20:
#       print("You got it")
# my_function()

# Reproduce the Bug
### To reproduce this bug consistently you could take out the rand int funciton and instead set dice_num equal to 1-6 and see when the error occurs, if you do this you will find that the error happens when dice_num is equal to 6. This is because the dice_imgs list is indexed starting at 0 so the max value is dice_imgs[5]. When randint selects the value of 6 the program gets the out of range bug. To fix this all you need to do is change dice_num to equal randint(0, 5) because randint is inclusive.

# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])

# # Play Computer
### The problem here is that when you put in the year 1994 nothing happens. by playing computer you can immagine year as equal to 1994, if statement: 1994 is greater than 1980 but it is not less than 1994 so it skips that if statement. elif: 1994 is  not greater than 1994 so it skips that too. The answer is to make either the if statement or the elif statement inclusive. OR you could add an else statement that says "cusp" or something. 

# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

# # Fix the Errors
### THIS IS NOT INDENTED CORRECTLY! Press tab on print. Also the program is trying to run the > operation on a string. You need to change the age input to an integer. Also need to add an "f" at the begining of the print statement to turn it into an fstring

# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")

# #Print is Your Friend
### If you throw a print(pages) you will get the correct number of pages as an output. So we know that is not the problem. If you print(word_per_page) you will get the value of 0 which means that the initialized value is not being updated. Check back to where you assign the value of word_per_page with an input and you see that it is a double equal not a single. This is a comparison that returns a boolian. Not assigning the value as you want. Just delete an equals sign and you are on you way.

# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger
### if you fo into pythontutor and use visualize execution. You will see that because b_list.append(new_item) is not within the for loop it only executes once with the last value in the list. Press tab on b_list.append()
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
    b_list.append(new_item)

    print(b_list)


mutate([1,2,3,5,8,13])