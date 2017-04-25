import json
import os

'''
FAISAL MOHAMMAD
4/25/2017

data_collection - script to collection sample data one by one. Dictionary mapping containing how the user input is
converted into meaningful feature data is via the json files located in json_dictionaries directory. This script will
enter a data sample into all three data text files: raw_data, approach1_data, and approach2_data.

'''

currDir = os.getcwd()
with open(currDir + '/json_dictionaries/raw_data_mapping.json') as json_data:
	cardDict = dict(json.load(json_data))
with open(currDir + '/json_dictionaries/approach2_dict.json') as json_data:
	infoDeckDict = dict(json.load(json_data))
with open(currDir + '/json_dictionaries/approach1_dict.json') as json_data:
	cardAttrDict = dict(json.load(json_data))

####### CREATE DATA ARRAY #######

data = [0] * 149  # this is for raw_data.txt
attr_data = [0] * 23  # this is for approach2_data
attr_data_OLD = [0] * 33  # this is for approach1_data

####### INPUT MANUAL DATA #######
card_x = []
card_y = []
i = 0
while i < 8:
	entry = input("Enter the %d card for Player X. \n" % i)
	while entry not in cardDict.keys():
		print("Make sure you type it in correctly!")
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
