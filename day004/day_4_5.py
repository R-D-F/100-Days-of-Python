rock = '''
    ROCK
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    PAPER
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    SCISSORS
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
from time import sleep

human = input("what do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n")

human = int(human)

computer = random.randint(0,2)


if human == 0 or human == 1 or human == 2:
    print("")
else:
    print("You chose")
    sleep(.5)
    print(".")
    sleep(.5)
    print(".")
    sleep(.5)
    print(".")
    print("poorly...")
    quit()

map = [["Draw", "You Win!", "You Lose"],["You Lose", "Draw", "You Win!"], ["You Win!", "You Lose", "Draw"]]
rps_list = [rock, paper, scissors]

print(f"You have chosen:")
sleep(.5)

print(f"{rps_list[human]}")
sleep(.5)
sleep(.5)


print("The computer chooses")
sleep(.5)
print(".")
sleep(.5)
print(".")
sleep(.5)
print(".")
sleep(2)
print(rps_list[computer])
print(map[computer][human])

