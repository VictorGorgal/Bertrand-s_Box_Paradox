import random

BOXES = [['Gold', 'Gold'],  # Box number 1
         ['Gold', 'Silver'],  # Box number 2
         ['Silver', 'Silver']]  # Box number 3

SAMPLE_SIZE = 10_000

both_gold = 0  # stores the total amount of times the algorithm picked both gold coins
only_one_gold = 0  # stores the total amount of times the algorithm pickes a gold coin and afterwards picked the silver coin

first_gold = 0  # stores the total amount of times the first coin was Gold, regardless for the next coin picked


for _ in range(SAMPLE_SIZE):
    box_number = random.randint(0, 2)  # choses randomly the coin
    coin_picked = random.randint(0, 1)

    box_picked = BOXES[box_number]  # loads the box
    coin = box_picked[coin_picked]  # gets the first coin picked

    if coin == 'Gold':
        next_coin = 0 if coin_picked == 1 else 1  # picks the other coin in the box a.k.a. if picked idx 1, next coin is idx 0

        coin = box_picked[next_coin]  # gets the second coin picked from the loaded box

        if coin == 'Gold':
            both_gold += 1  # if both are gold, increment
        else:
            only_one_gold += 1  # if the first coin is gold and the other is silver, increment

        first_gold += 1

        
print('After picking a Gold coin:')
print(f'{both_gold / first_gold * 100 :.3f}% of the times the second coin was Gold')
print(f'{only_one_gold / first_gold * 100 :.3f}% of the times the second coin was Silver')
