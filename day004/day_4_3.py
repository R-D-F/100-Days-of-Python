# Banker Roulette
# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
length = len(names) -1

ran_int = random.randint(0, length)

print(f"{names[ran_int]} is going to buy the meal today!")
