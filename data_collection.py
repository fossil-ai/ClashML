import numpy as np

'''
Faisal Mohammad

Version 0.0

This is the data collection module for obtaining data from Royale TV (this was done manually)

'''


cardDict = {'Mortar': 44, 'X-Bow': 51, 'Poison': 54, 'Royal Giant': 11, 'Night Princess': 65, 'Ice Spirit': 7,
            'Bomber': 9, 'Princess': 8, 'Clone': 59, 'Cannon': 49, 'Bomb Tower': 39, 'Rocket': 37, 'Bowler': 12,
            'Lumberjack': 19, 'Prince': 5, 'Goblin Barrel': 46, 'Bats': 71, 'Ice Golem': 70, 'Inferno Dragon': 62,
            'Musketeer': 33, 'Goblin Gang': 72, 'Log': 57, 'Tornado': 58, 'Dark Prince': 18, 'Spear Goblin': 23,
            'Giant Skeletons': 26, 'Miner': 22, 'Hog Rider': 4, 'Minions': 27, 'Mirror': 53, 'Barbarian Hut': 35,
            'Executioner': 69, 'Zap': 56, 'Skeleton Army': 14, 'Graveyard': 60, 'Giant Pekka': 24,
            'Elite Barbarians': 73, 'Battle Ram': 45, 'P.E.K.K.A': 2, 'Sparky': 20, 'Barbarians': 6, 'Skeletons': 17,
            'Lightning': 36, 'Freeze': 52, 'Dart Goblin': 68, 'Ice Wizard': 10, 'Fire Spirits': 21, 'Furnace': 50,
            'Bandit': 64, 'Guards': 1, 'Baby Dragon': 3, 'Three Musketeers': 25, 'Elixer Collector': 38, 'Goblins': 29,
            'Archer': 0, 'Electro Wizard': 63, 'Tombstone': 48, 'Wizard': 34, 'Fireball': 42, 'Tesla': 43, 'Balloon': 15,
            'Valkyrie': 28, 'Lava Hound': 16, 'Minion Horde': 74, 'Rage': 55, 'Mega Minion': 67, 'Heal': 61,
            'Inferno Tower': 40, 'Goblin Hut': 41, 'Witch': 31, 'Night Witch': 66, 'Golem': 32, 'Arrows': 47,
            'Knight': 13}

# CREATE PLAYER X ARRAY (74 entries for cards plus one for skills)

x_cards = input("Enter Player X's 8 cards, separate each card-name with DOUBLE whitespace '  ' \n")
x_wins = input("Enter number of total wins and three crown wins \n")

x_cardlist = x_cards.split("  ")
x_winlist = x_wins.split("  ")

if(len(x_cardlist) != 8 or len(x_winlist) != 2):
	raise ValueError('Enter ONLY 8 cards and ONLY 2 win numbers')

x_data = [0] * 75
for cardName in x_cardlist:
	x_data[cardDict[cardName]] = 1
x_data[74] = int(x_wins[1])/int(x_wins[0])


y_cards = input("Enter Player X's 8 cards, separate each card-name with DOUBLE whitespace '  ' \n")
y_wins = input("Enter number of total wins and three crown wins with DOUBLE whitespaces '  '\n")
y_cardlist = y_cards.split("  ")
y_winlist = y_wins.split("  ")

if(len(y_cardlist) != 8 or len(y_winlist) != 2):
	raise ValueError('Enter ONLY 8 cards and ONLY 2 win numbers')

y_data = [0] * 75
for cardName in y_cardlist:
	y_data[cardDict[cardName]] = 1
y_data[74] = int(y_wins[1])/int(y_wins[0])


