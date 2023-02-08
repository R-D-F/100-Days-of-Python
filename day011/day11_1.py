import random
import art
import os
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_human():
    human_hand.append(random.choice(cards))

def deal_computer():
    computer_hand.append(random.choice(cards))

def first_deal():
    deal_human()
    deal_human()
    deal_computer()
    deal_computer()

def show_info():
    print(f"Your cards: {human_hand}, current score: {sum(human_hand)}")
    print(f"Computer's first card {computer_hand[1]}")

def check_for_ace_human():
    if sum(human_hand) > 21: 
        for num in range(len(human_hand)):
            if sum(human_hand) > 21:
                if human_hand[num] == 11:
                    human_hand[num] = 1 

def check_for_ace_computer():
    if sum(computer_hand) > 21: 
        for num in range(len(computer_hand)):
            if sum(computer_hand) > 21:
                if computer_hand[num] == 11:
                    computer_hand[num] = 1

def dealer_function():
    check_for_ace_computer()
    while sum(computer_hand) < 17:
        deal_computer()
        check_for_ace_computer()

def start_game_function():
    human_hand.clear()
    computer_hand.clear()
    start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    os.system('cls')
    return start_game

def return_final():
    print(f"Your final hand: {human_hand}, final score: {sum(human_hand)}\nComputer's final hand: {computer_hand}, final score: {sum(computer_hand)}")

human_hand = []
computer_hand = []

while start_game_function() == 'y':
    print(art.logo)
    first_deal()
    check_for_ace_human()  
    show_info()
    
    if sum(human_hand) < 21:
        hit = input("Type 'y' to get another card, type 'n' to pass: ")
        while hit == 'y':
            deal_human()
            check_for_ace_human()
            show_info()
            if sum(human_hand) > 21:
                hit = 'n'
                return_final()
                print("You went over, You lose")
                
            elif sum(human_hand) < 21:
                hit = input("Type 'y' to get another card, type 'n' to pass: ")
            else:
                hit = 'n'

    dealer_function()
    return_final()
    if sum(human_hand) == 21:
        if sum(human_hand) == sum(computer_hand):
            print("Draw.")
        else:  
            print("You win with BlackJack!")
        
    elif sum(human_hand) > sum(computer_hand) and sum(human_hand) < 22: 
        print("You win!")
        
    elif sum(human_hand) < sum(computer_hand):
        print("You lose.")  

    elif sum(human_hand) ==  sum(computer_hand):
        print("Draw.")

    elif sum(computer_hand) > 21 and sum(human_hand) < 22:
        print("You win!")
    
    
