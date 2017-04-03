'''
Faisal Mohammad

Version 0.0

This is the data collection module for obtaining data from Royale TV (this was done manually)

'''

cardDict = {'mirror': 29, 'graveyard': 34, 'bombtower': 10, 'guards': 49, 'rage': 64, 'furnace': 47, 'barbarians': 40,
            'elitebarbarians': 36, 'speargoblin': 24, 'minipekka': 38, 'icegolem': 17, 'valkyrie': 61, 'threemusk': 51, 'firespirits': 46,
            'cannon': 9, 'frieball': 58, 'clone': 8, 'poison': 2, 'rocket': 11, 'skeletons': 41, 'battleram': 37, 'musketeer': 19,
            'megaminion': 65, 'log': 21, 'hogrider': 27, 'collector': 52, 'heal': 66, 'knight': 73, 'bomber': 6, 'icespirit': 5,
            'wizard': 57, 'nightprincess': 4, 'tombstone': 56, 'tornado': 22, 'executioner': 31, 'bandit': 48, 'infernotower': 67,
            'icewizard': 45, 'archer': 54, 'balloon': 60, 'miner': 26, 'royalgiant': 3, 'golem': 71, 'darkprince': 23, 'mortar': 0,
            'arrows': 72, 'bats': 16, 'nightwitch': 70, 'electrowizard': 55, 'witch': 69, 'giantpekka': 35, 'barbarianhut': 30,
            'lightning': 42, 'zap': 32, 'minions': 28, 'minionhorde': 63, 'dartgoblin': 44, 'goblinhut': 68, 'infernodragon': 18,
            'sparky': 39, 'tesla': 59, 'prince': 14, 'lavahound': 62, 'skeletonarmy': 33, 'babydragon': 50, 'goblinbarrel': 15,
            'giantskeleton': 25, 'freeze': 43, 'lumberjack': 13, 'xbow': 1, 'bowler': 12, 'goblingang': 20, 'princess': 7, 'goblins': 53}

####### CREATE DATA ARRAY #######

data = [0] * 149

####### INPUT MANUAL DATA #######

cardX = input("Enter Player X's 8 cards, separate each card-name with a whitespace ' '\n")
cardY = input("Enter Player Y's 8 cards, separate each card-name with a whitespace ' '\n")
winner_str = input("Enter 1 if Player X won, or Enter 0 if Player Y won\n")

####### PARSE INPUT STRINGS #######

card_x = cardX.split(" ")
print(card_x)
card_y = cardY.split(" ")
print(card_y)

winner = int(winner_str)

####### INSERT INTO DATA ARRAY#######

for x in card_x:
	data[cardDict[x]] = 1
for y in card_y:
	data[cardDict[y] + 74] = 1

data[148] = winner

file = open("data","a")
file.write(str(data).strip('[]') + "\n")
file.close()








