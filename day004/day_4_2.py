#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
import random
#Write the rest of your code below this line 👇

random_int = random.randint(1, 100) 
rand_random_int = random_int % 2
if rand_random_int == 1:
    print("Tails")
else:
    print("Heads")
