import json
import os

'''
FAISAL MOHAMMAD
4/25/2017

data_collection - script to collection sample data one by one. Dictionary mapping containing how the user input is
converted into meaningful feature data is via the json files located in json_dictionaries directory. This script will
enter a data sample into all three data text files: raw_data, approach1_data, and approach2_data.

'''
# get current working directory and use path to get json data files for dictionary mappings

class DataCollection:
	def __init__(self):
		self.currDir = os.getcwd()
		self.rawDict,self.apprTwoDict,self.apprOneDict = self.getDictionaryMapping()
		self.N = len(self.rawDict)

	# Enter data
	def collectData(self):
		card_x, card_y = [], []
		i = 0
		while i < 8:
			entry = input("Enter the %d card for Player X. \n" % i)
			while entry not in self.rawDict.keys():
				print("Make sure you type it in correctly!")
				entry = input("Enter the %d card for Player X. \n" % i)
			card_x.append(entry)
			i += 1
		i = 0
		while i < 8:
			entry = input("Enter the %d card for Player Y. \n" % i)
			while entry not in self.rawDict.keys():
				print("Bitch type that in correctly!")
				entry = input("Enter the %d card for Player Y. \n" % i)
			card_y.append(entry)
			i += 1

		winner_str = input("Enter 1 if Player X won, or Enter 0 if Player Y won\n")
		winner = int(winner_str)
		return card_x,card_y,winner

	# Get a data sample for the raw data file
	def createRawDataSample(self,card_x, card_y, winner):
		rawData = [0] * 149
		for x in card_x:
			rawData[self.rawDict[x]] = 1
		for y in card_y:
			rawData[self.rawDict[y] + 74] = 1
		rawData[148] = winner
		output = str(rawData).strip('[]') + "\n"
		file = open(self.currDir + "/datasets/raw_data", "a")
		file.write(output)
		file.close()
		return output

	# Get a data sample via Approach Two
	def createApprTwoDataSample(self,card_x, card_y, winner):
		apprTwoData = [0] * 23  # this is for approach2_data
		tx, ty = 0, 0
		for x in card_x:
			apprTwoData[0] += self.apprTwoDict[x]['health']
			apprTwoData[1] += self.apprTwoDict[x]['cost'] / 8
			if self.apprTwoDict[x]['type'] in {'gtroop', 'atroop', 'dbuilding', 'sbuilding'}:
				tx += 1
				apprTwoData[2] += self.apprTwoDict[x]['ADPS']
			apprTwoData[3] += self.apprTwoDict[x]['building']
			apprTwoData[4] += self.apprTwoDict[x]['splash']
			apprTwoData[5] += self.apprTwoDict[x]['stunner']
			apprTwoData[6] += self.apprTwoDict[x]['tricky']
			apprTwoData[7] += self.apprTwoDict[x]['multi']
			apprTwoData[8] += self.apprTwoDict[x]['airdamage']
			apprTwoData[9] += self.apprTwoDict[x]['buildingbuster']
			if self.apprTwoDict[x]['type'] == 'dspell':
				apprTwoData[10] += 1

		for y in card_y:
			apprTwoData[11] += self.apprTwoDict[y]['health']
			apprTwoData[12] += self.apprTwoDict[y]['cost'] / 8
			if self.apprTwoDict[y]['type'] in {'gtroop', 'atroop', 'dbuilding', 'sbuilding'}:
				ty += 1
				apprTwoData[13] += self.apprTwoDict[y]['ADPS']
			apprTwoData[14] += self.apprTwoDict[y]['building']
			apprTwoData[15] += self.apprTwoDict[y]['splash']
			apprTwoData[16] += self.apprTwoDict[y]['stunner']
			apprTwoData[17] += self.apprTwoDict[y]['tricky']
			apprTwoData[18] += self.apprTwoDict[y]['multi']
			apprTwoData[19] += self.apprTwoDict[y]['airdamage']
			apprTwoData[20] += self.apprTwoDict[y]['buildingbuster']
			if self.apprTwoDict[y]['type'] == 'dspell':
				apprTwoData[21] += 1
			if self.apprTwoDict[y]['type'] in {'gtroop', 'atroop', 'dbuilding', 'sbuilding'}:
				ty += 1
		apprTwoData[2] = apprTwoData[2] / tx
		apprTwoData[13] = apprTwoData[13] / tx
		apprTwoData[22] = winner
		output = str(apprTwoData).strip('[]') + "\n"
		file = open(self.currDir + "/datasets/approach2_data", "a")
		file.write(output)
		file.close()
		return output

	# Get a data sample via Approach One
	def createApprOneDataSample(self,card_x, card_y, winner):
		apprOneData = [0] * 33  # this is for approach1_data
		for x in card_x:
			for attr in self.apprOneDict[x]:
				apprOneData[attr] += 1
		for y in card_y:
			for attr in self.apprOneDict[y]:
				apprOneData[attr + 16] += 1
		apprOneData[32] = winner
		output = str(apprOneData).strip('[]') + "\n"
		file = open(self.currDir + "/datasets/approach1_data", "a")
		file.write(output)
		file.close()
		return output

	# insert data to text files!
	def insertData(self, card_x, card_y, winner):
		self.createRawDataSample(card_x, card_y, winner)
		self.createApprOneDataSample(card_x, card_y, winner)
		self.createApprTwoDataSample(card_x, card_y, winner)

	# Pull Json dictionary mapping files
	def getDictionaryMapping(self):
		with open(self.currDir + '/json_dictionaries/raw_data_mapping.json') as json_data:
			rawDict = dict(json.load(json_data))
		with open(self.currDir + '/json_dictionaries/approach2_dict.json') as json_data:
			apprTwoDict = dict(json.load(json_data))
		with open(self.currDir + '/json_dictionaries/approach1_dict.json') as json_data:
			apprOneDict = dict(json.load(json_data))
		return rawDict, apprTwoDict, apprOneDict

	# conversion from raw_data.txt to the approach1_data/approach2_data files - used to recover data from raw_data ONLY.
	def updateData(self):
		file = open(self.currDir + "/datasets/raw_data", "r")
		curr_line = file.readlines()
		for line in curr_line:
			X_data, Y_data = [], []
			temp = line.split(', ')
			results = list(map(int, temp))
			for i in range(len(results) - 1 - self.N):
				x = [name for name, index in self.rawDict.items() if (results[i] == 1 and index == i)]
				y = [name for name, index in self.rawDict.items() if (results[i + self.N] == 1 and index == i)]
				if (len(x) == 1):
					X_data.append(x[0])
				if (len(y) == 1):
					Y_data.append(y[0])
			winner = results[self.N * 2]
			self.createApprOneDataSample(X_data,Y_data,winner)
			self.createApprTwoDataSample(X_data,Y_data,winner)
		file.close()

data_collection = DataCollection()
card_x, card_y, winner = data_collection.collectData()
data_collection.insertData(card_x,card_y,winner)