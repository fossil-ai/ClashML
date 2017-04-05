'''
Faisal Mohammad

Version 0.0

This is the data collection module for obtaining data from Royale TV (this was done manually).
The data retrieved regarding both players' cards and the outcome is used to create the sample data for analysis
via grouping cards to attribute groups ('features' ).

ATTRIBUTES:

0) DEFENSE - High health

1) BRAWLERS - Cards that attack one troop/building at a time ie. PEKKA

2) HARD-HITTERS - High attack damage

3) FLYING - Aerial troops

4) GROUND - Ground troops

5) DAMAGE-SPELLS - Spell cards that cause damage or increase damage ie. Lightning, Fireball

6) STUN-SPELLS - Spells that slow down/stun/freeze movement

7) SPLASH - Cards which cause splash damage

8) CHEAP - Cards with low elixer cost (1-2)

9) MODERATE - Cards with moderate elixer cost (3-4)

10) HIGH - Cards with high elixer cost (5+)

11) AIR-DAMAGE - Cards that can inflict damage to flying troops

12) BUILDING-BUSTERS - Cards that specifically attack building cards/towers

13) BUILDING - Building cards such as X-Bow, towers, etc.

14) MULTI - Cards that either spawn with multiple troops or create multiple troops (3 or more)

15) TRICKY - Card has some unique attribute to it ie. Princess long range, Miner spawn freedom, etc.


SAMPLE DATA WILL BE STRUCTURED AS FOLLOWS:

X = [PLAYER 1 ATTRIBUTES, PLAYER 2 ATTRIBUTES, WINNER] - Size of sample data is: N = (2 * # of Attributes) + 1

'''

cardDict = {'mirror': 29, 'graveyard': 34, 'bombtower': 10, 'guards': 49, 'rage': 64, 'furnace': 47, 'barbarians': 40,
            'elitebarbarians': 36, 'speargoblin': 24, 'minipekka': 38, 'icegolem': 17, 'valkyrie': 61, 'threemusk': 51, 'firespirits': 46,
            'cannon': 9, 'fireball': 58, 'clone': 8, 'poison': 2, 'rocket': 11, 'skeletons': 41, 'battleram': 37, 'musketeer': 19,
            'megaminion': 65, 'log': 21, 'hogrider': 27, 'collector': 52, 'heal': 66, 'knight': 73, 'bomber': 6, 'icespirit': 5,
            'wizard': 57, 'tombstone': 56, 'tornado': 22, 'executioner': 31, 'bandit': 48, 'infernotower': 67,
            'icewizard': 45, 'archer': 54, 'balloon': 60, 'miner': 26, 'royalgiant': 3, 'golem': 71, 'darkprince': 23, 'mortar': 0,
            'arrows': 72, 'bats': 16, 'nightwitch': 70, 'electrowizard': 55, 'witch': 69, 'giantpekka': 35, 'barbarianhut': 30,
            'lightning': 42, 'zap': 32, 'minions': 28, 'minionhorde': 63, 'dartgoblin': 44, 'goblinhut': 68, 'infernodragon': 18,
            'sparky': 39, 'tesla': 59, 'prince': 14, 'lavahound': 62, 'skeletonarmy': 33, 'babydragon': 50, 'goblinbarrel': 15,
            'giantskeleton': 25, 'freeze': 43, 'lumberjack': 13, 'xbow': 1, 'bowler': 12, 'goblingang': 20, 'princess': 7, 'goblins': 53,
            'giant':4}

cardAttrDict = {'valkyrie': [1, 4, 7, 9], 'threemusk': [1, 4, 10, 11, 14], 'furnace': [7, 9, 13, 14],
                'speargoblins': [14, 11, 8, 4, 1],
                'poison': [5, 7, 9, 11], 'rage': [5, 8], 'minipekka': [1, 2, 4, 9], 'icegolem': [8, 12, 4, 1, 6],
                'elitebarbarians': [1, 2, 4, 10], 'cannon': [0, 1, 9, 13], 'guards': [1, 14, 9, 4],
                'battleram': [1, 2, 4, 9, 12],
                'barbarians': [1, 4, 10, 14], 'mirror': [14, 15], 'fireball': [5, 9, 7, 11], 'musketeer': [1, 4, 9, 11],
                'clone': [14, 9, 15], 'firespirits': [4, 7, 8, 11, 14], 'megaminion': [1, 3, 2, 11, 9],
                'graveyard': [14, 5, 10],
                'bombtower': [0, 7, 10, 13], 'rocket': [2, 5, 10, 11], 'skeletons': [14, 8, 4, 1], 'log': [5, 8],
                'hogrider': [4, 9, 12],
                'collector': [13, 10], 'knight': [0, 9, 4], 'heal': [9], 'tombstone': [14, 13, 9, 4],
                'wizard': [11, 10, 7, 4],
                'infernotower': [1, 0, 10, 11, 13], 'tornado': [5, 6, 7, 9, 11], 'icespirit': [11, 8, 6, 4],
                'bandit': [2, 1, 4, 9, 15],
                'bomber': [9, 7, 4], 'executioner': [0, 4, 7, 10, 11], 'archer': [1, 4, 9, 11], 'mortar': [0, 13, 7, 9],
                'miner': [4, 9, 12, 1, 0, 15],
                'golem': [0, 1, 4, 10, 12], 'balloon': [0, 2, 3, 7, 10, 12], 'icewizard': [4, 6, 7, 9, 11],
                'royalgiant': [0, 12, 10, 4],
                'darkprince': [9, 4, 1, 2], 'arrows': [5, 7, 9, 11], 'barbarianhut': [14, 10, 4, 1, 13],
                'electrowizard': [6, 4, 11, 9, 1],
                'witch': [14, 11, 10, 7, 4], 'nightwitch': [14, 11, 9, 4, 2, 1], 'bats': [8, 3, 14, 11, 1],
                'giantpekka': [0, 1, 2, 4, 10],
                'skeletonarmy': [14, 9, 4], 'minionhorde': [14, 11, 10, 3, 1], 'lavahound': [0, 3, 7, 10, 12, 15],
                'lightning': [2, 5, 7, 10, 11], 'dartgoblin': [4, 1, 9, 11], 'zap': [5, 6, 11, 8],
                'sparky': [0, 2, 4, 7, 10],
                'infernodragon': [0, 3, 1, 9, 11, 15], 'babydragon': [0, 3, 7, 9, 11],
                'goblinhut': [14, 13, 11, 10, 4, 1],
                'goblinbarrel': [1, 4, 14, 9], 'tesla': [1, 13, 11, 9], 'prince': [0, 1, 2, 4, 10],
                'minions': [1, 3, 9, 11, 14],
                'freeze': [9, 6], 'goblingang': [14, 1, 4, 9, 11], 'xbow': [13, 10, 0], 'bowler': [0, 7, 4, 10],
                'giantskeleton': [0, 1, 4, 10, 15],
                'lumberjack': [2, 1, 4, 9, 15], 'princess': [4, 7, 9, 11, 15], 'giant': [0, 4, 10, 12],
                'goblins': [14, 4, 8, 1]}

####### CREATE DATA ARRAY #######

data = [0] * 149  # this is for brute_data.txt
attr_data = [0] * 33  # this is for attr_data

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

####### INSERT INTO data ARRAY#######

for x in card_x:
	data[cardDict[x]] = 1
for y in card_y:
	data[cardDict[y] + 74] = 1

data[148] = winner

file = open("brute_data", "a")
file.write(str(data).strip('[]') + "\n")
file.close()

###### INSERT INTO attr_data ARRAY#####

for x in card_x:
	for attr in cardAttrDict[x]:
		attr_data[attr] += 1

for y in card_y:
	for attr in cardAttrDict[y]:
		attr_data[attr + 16] += 1

attr_data[32] = winner

file = open("attr_data", "a")
file.write(str(attr_data).strip('[]') + "\n")
file.close()


############### INPUT SAMPLE TO TEST SCRIPT ###############################
# Enter Player X's 8 cards, separate each card-name with a whitespace ' ' #
# giant collector graveyard wizard megaminion miner witch valkyrie        #
# Enter Player Y's 8 cards, separate each card-name with a whitespace ' ' #
# giant witch rage zap knight minions skeletonarmy log                    #
# Enter 1 if Player X won, or Enter 0 if Player Y won                     #
# 1                                                                       #
###########################################################################