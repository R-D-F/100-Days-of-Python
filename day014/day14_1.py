from game_data import data
import random
import art
import os

def most_folower_function(profile_1, profile_2):
    if profile_1['follower_count'] > profile_2['follower_count']:
        return "a"
    elif profile_2['follower_count'] > profile_1['follower_count']:
        return "b"

def game():
    user_score = 0
    game_over = False
    profile_a = random.choice(data)
    profile_b = random.choice(data)
    while game_over != True:
        
        print(art.logo)
        profile_b = random.choice(data)
        while profile_a == profile_b:
            profile_b = random.choice(data)
        if user_score > 0:
            print(f"You're right! Current score: {user_score}")

        print(f"Compare A: {profile_a['name']}, a {profile_a['description']}, from {profile_a['country']}.")
        print(art.vs)
        print(f"Compare B: {profile_b['name']}, a {profile_b['description']}, from {profile_b['country']}.")
        user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
        if user_choice == most_folower_function(profile_a, profile_b):
            user_score += 1
            os.system('cls')
            profile_a = profile_b
            game_over = False
        else:
            os.system('cls')
            print(art.logo)
            print(f"{profile_a['name']} has {profile_a['follower_count']}M followers and {profile_b['name']} has {profile_b['follower_count']}M followers.\nGame over, you lose")
            print(f"Final score: {user_score}")
            game_over = True

game()