human_hand = [11, 11]

if sum(human_hand) > 21: 
    for num in range(len(human_hand)):
        print(num)
        if sum(human_hand) > 21:
            print(num)
            if human_hand[num] == 11:
                human_hand[num] = 1
print(human_hand)
print(sum(human_hand))