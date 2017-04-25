import json
import os

currDir = os.getcwd()

'''
Faisal Mohammad

Version 0.0

This is the data collection module for obtaining data from Royale TV (this was done manually).
The data retrieved regarding both players' cards and the outcome is used to create the sample data for analysis
via grouping cards to attribute groups ('features' ).

ATTRIBUTES VERSION 2 :

0) TOTAL-HEALTH     - Total hit points of each card
1) ELIXER-COST      - Average elixer cost of deck
2) TOTAL-ADPS       - Total attack damage per second
3) BUILDINGS        - # of building cards
4) SPLASH           - # of splash damage cards
5) STUNNERS         - # of cards with a stun/freeze effect
6) TRICKY           - # of cards with unique perks (princess, miner, clone)
7) MULTI            - # of multi-spawn cards
8) AIR-DAMAGE       - # of cards who can attack air troops
9) BUILDING-BUSTERS - # of cards who attack only building cards
10) DAMAGE-SPELLS   - # of card spells that cause damage

SAMPLE DATA WILL BE STRUCTURED AS FOLLOWS:

X = [PLAYER 1 ATTRIBUTES, PLAYER 2 ATTRIBUTES, WINNER] - Size of sample data is: N = (2 * # of Attributes) + 1

ATTRIBUTES VERSION 1:

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

# POSSIBLE ATTRS - MOD DAMAGE, LOW DAMAGE, MOD HEALTH, LOW HEALTH

SAMPLE DATA WILL BE STRUCTURED AS FOLLOWS:

X = [PLAYER 1 ATTRIBUTES, PLAYER 2 ATTRIBUTES, WINNER] - Size of sample data is: N = (2 * # of Attributes) + 1

'''

with open(currDir + '/json_dictionaries/raw_data_mapping.json') as json_data:
	cardDict = dict(json.load(json_data))
with open(currDir + '/json_dictionaries/approach2_dict.json') as json_data:
	infoDeckDict = dict(json.load(json_data))
with open(currDir + '/json_dictionaries/approach1_dict.json') as json_data:
	cardAttrDict = dict(json.load(json_data))

####### CREATE DATA ARRAY #######

data = [0] * 149  # this is for raw_data.txt
attr_data = [0] * 23  # this is for approach1_data
attr_data_OLD = [0] * 33  # this is for approach1_data

####### INPUT MANUAL DATA #######
card_x = []
card_y = []
i = 0
while i < 8:
	entry = input("Enter the %d card for Player X. \n" % i)
	while entry not in cardDict.keys():
		print("Bitch type that in correctly!")
		entry = input("Enter the %d card for Player X. \n" % i)
	card_x.append(entry)
	i += 1
i = 0
while i < 8:
	entry = input("Enter the %d card for Player Y. \n" % i)
	while entry not in cardDict.keys():
		print("Bitch type that in correctly!")
		entry = input("Enter the %d card for Player Y. \n" % i)
	card_y.append(entry)
	i += 1

winner_str = input("Enter 1 if Player X won, or Enter 0 if Player Y won\n")

####### PARSE INPUT STRINGS #######

print(card_x)
print(card_y)
winner = int(winner_str)

####### INSERT INTO data ARRAY#######

for x in card_x:
	data[cardDict[x]] = 1
for y in card_y:
	data[cardDict[y] + 74] = 1

data[148] = winner

file = open(currDir + "/datasets/raw_data", "a")
file.write(str(data).strip('[]') + "\n")
file.close()

###### INSERT INTO approach1_data ARRAY#####
tx, ty = 0, 0
for x in card_x:
	attr_data[0] += infoDeckDict[x]['health']
	attr_data[1] += infoDeckDict[x]['cost'] / 8
	if infoDeckDict[x]['type'] in {'gtroop', 'atroop', 'dbuilding', 'sbuilding'}:
		tx += 1
		attr_data[2] += infoDeckDict[x]['ADPS']
	attr_data[3] += infoDeckDict[x]['building']
	attr_data[4] += infoDeckDict[x]['splash']
	attr_data[5] += infoDeckDict[x]['stunner']
	attr_data[6] += infoDeckDict[x]['tricky']
	attr_data[7] += infoDeckDict[x]['multi']
	attr_data[8] += infoDeckDict[x]['airdamage']
	attr_data[9] += infoDeckDict[x]['buildingbuster']
	if infoDeckDict[x]['type'] == 'dspell':
		attr_data[10] += 1

for y in card_y:
	attr_data[11] += infoDeckDict[y]['health']
	attr_data[12] += infoDeckDict[y]['cost'] / 8
	if infoDeckDict[y]['type'] in {'gtroop', 'atroop', 'dbuilding', 'sbuilding'}:
		ty += 1
		attr_data[13] += infoDeckDict[y]['ADPS']
	attr_data[14] += infoDeckDict[y]['building']
	attr_data[15] += infoDeckDict[y]['splash']
	attr_data[16] += infoDeckDict[y]['stunner']
	attr_data[17] += infoDeckDict[y]['tricky']
	attr_data[18] += infoDeckDict[y]['multi']
	attr_data[19] += infoDeckDict[y]['airdamage']
	attr_data[20] += infoDeckDict[y]['buildingbuster']
	if infoDeckDict[y]['type'] == 'dspell':
		attr_data[21] += 1
	if infoDeckDict[y]['type'] in {'gtroop', 'atroop', 'dbuilding', 'sbuilding'}:
		ty += 1
attr_data[2] = attr_data[2] / tx
attr_data[13] = attr_data[13] / tx
attr_data[22] = winner
print(attr_data)
file = open(currDir + "/datasets/approach2_data", "a")
file.write(str(attr_data).strip('[]') + "\n")
file.close()

for x in card_x:
	for attr in cardAttrDict[x]:
		attr_data_OLD[attr] += 1

for y in card_y:
	for attr in cardAttrDict[y]:
		attr_data_OLD[attr + 16] += 1

attr_data_OLD[32] = winner

file = open(currDir + "/datasets/approach1_data", "a")
file.write(str(attr_data_OLD).strip('[]') + "\n")
file.close()
