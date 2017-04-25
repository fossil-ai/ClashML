import json
import os

'''
FAISAL MOHAMMAD
4/25/2017

update_data_scheme - this Python script is used only for instances of changes in the data collection scheme. It uses the
raw_data.txt file which contains the exact card information, and allows us to regenerate the approach1_data.txt and
approach2_data.txt files in order to fit the new schema. Any changes to the schema should be made inside the
bruteDataToApprTwoData and bruteDataToApprOneData functions and in the data_collection.py as well for additional data
collection.

'''

# get working directory
currDir = os.getcwd()

# load json data to dictionaries for the raw data and the two approaches
with open(currDir + '/json_dictionaries/raw_data_mapping.json') as json_data:
	cardDict = dict(json.load(json_data))
with open(currDir + '/json_dictionaries/approach2_dict.json') as json_data:
	infoDeckDict = dict(json.load(json_data))
with open(currDir + '/json_dictionaries/approach1_dict.json') as json_data:
	cardAttrDict = dict(json.load(json_data))

# Nominal Values
N = len(cardDict)  # number of cards
M = 23  # length of feature vector + label - also # of Attributes = M/2 - 1 (APPROACH 2)
M0 = 33 # length of feature vector + label - also # of attributes = M0/2 - 1 (APPROACH 1)

# conversion from raw_data.txt to the approach1_data/approach2_data files.
def updateData():
	file = open(currDir + "/datasets/raw_data", "r")
	curr_line = file.readlines()
	for line in curr_line:
		X_data, Y_data = [],[]
		temp = line.split(', ')
		results = list(map(int, temp))
		for i in range(len(results) - 1 - N):
			x = [name for name, index in cardDict.items() if (results[i] == 1 and index == i)]
			y = [name for name, index in cardDict.items() if (results[i + N] == 1 and index == i)]
			if (len(x) == 1):
				X_data.append(x[0])
			if (len(y) == 1):
				Y_data.append(y[0])
		winner = results[N * 2]
		bruteDataToApprOneData(X_data, Y_data, winner)
		bruteDataToApprTwoData(X_data, Y_data, winner)
	file.close()
# similar code from data_collection.py, generates entire approach2_data.txt
def bruteDataToApprTwoData(X_data, Y_data, winner):
	attr_data = [0] * M  # this is for approach1_data
	tx, ty = 0, 0
	for x in X_data:
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

	for y in Y_data:
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
	file = open(currDir + "/datasets/approach2_data", "a")
	file.write(str(attr_data).strip('[]') + "\n")
	file.close()
# similar code from data_collection.py, generates entire approach1_data.txt
def bruteDataToApprOneData(X_data, Y_data, winner):
	attr_data = [0] * M0
	for x in X_data:
		for attr in cardAttrDict[x]:
			attr_data[attr] += 1
	for y in Y_data:
		for attr in cardAttrDict[y]:
			attr_data[attr + int((M0-1)/2)] += 1
	attr_data[M0-1] = winner
	file = open(currDir + "/datasets/approach1_data", "a")
	file.write(str(attr_data).strip('[]') + "\n")
	file.close()

updateData()
