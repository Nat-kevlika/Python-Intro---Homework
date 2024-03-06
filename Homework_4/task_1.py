import random

number_of_players = int(input("ჩაწერე მოთამაშეების რაოდენობა: "))
player_list = []

for i in range(1, number_of_players+1):
    pair1 = random.randint(1, 6)
    pair2 = random.randint(1, 6)

    print(pair1, pair2)
    #print(f"Player {i}: {pair1} and {pair2}")










