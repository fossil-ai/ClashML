# ONLY USE WHEN NEW ATTRIBUTES ARE ADDED AND REMOVED - DO NOT WRITE ON brute_data.txt, that is pure data and cannot be recovered.

cardDict = {
	'mirror': 29, 'graveyard': 34, 'bombtower': 10, 'guards': 49, 'rage': 64, 'furnace': 47, 'barbarians': 40,
	'elitebarbarians': 36, 'speargoblins': 24, 'minipekka': 38, 'icegolem': 17, 'valkyrie': 61, 'threemusk': 51,
	'firespirits': 46,
	'cannon': 9, 'fireball': 58, 'clone': 8, 'poison': 2, 'rocket': 11, 'skeletons': 41, 'battleram': 37,
	'musketeer': 19,
	'megaminion': 65, 'log': 21, 'hogrider': 27, 'collector': 52, 'heal': 66, 'knight': 73, 'bomber': 6,
	'icespirit': 5,
	'wizard': 57, 'tombstone': 56, 'tornado': 22, 'executioner': 31, 'bandit': 48, 'infernotower': 67,
	'icewizard': 45, 'archers': 54, 'balloon': 60, 'miner': 26, 'royalgiant': 3, 'golem': 71, 'darkprince': 23,
	'mortar': 0,
	'arrows': 72, 'bats': 16, 'nightwitch': 70, 'electrowizard': 55, 'witch': 69, 'giantpekka': 35,
	'barbarianhut': 30,
	'lightning': 42, 'zap': 32, 'minions': 28, 'minionhorde': 63, 'dartgoblin': 44, 'goblinhut': 68,
	'infernodragon': 18,
	'sparky': 39, 'tesla': 59, 'prince': 14, 'lavahound': 62, 'skeletonarmy': 33, 'babydragon': 50,
	'goblinbarrel': 15,
	'giantskeleton': 25, 'freeze': 43, 'lumberjack': 13, 'xbow': 1, 'bowler': 12, 'goblingang': 20,
	'princess': 7, 'goblins': 53,
	'giant': 4}

cardAttrDict = {
	'archers': [1, 4, 9, 11], 'arrows': [5, 7, 9, 11],
	'babydragon': [0, 3, 7, 9, 11], 'balloon': [0, 2, 3, 7, 10, 12], 'bandit': [2, 1, 4, 9, 15],
	'barbarianhut': [14, 10, 4, 1, 13],
	'barbarians': [1, 4, 10, 14], 'bats': [8, 3, 14, 11, 1], 'battleram': [1, 2, 4, 9, 12], 'bomber': [9, 7, 4],
	'bombtower': [0, 7, 10, 13], 'bowler': [0, 7, 4, 10], 'cannon': [0, 1, 9, 13], 'clone': [14, 9, 15],
	'collector': [13, 10],
	'darkprince': [9, 4, 1, 2], 'dartgoblin': [4, 1, 9, 11], 'electrowizard': [6, 4, 11, 9, 1],
	'elitebarbarians': [1, 2, 4, 10],
	'executioner': [0, 4, 7, 10, 11], 'fireball': [5, 9, 7, 11], 'firespirits': [4, 7, 8, 11, 14], 'freeze': [9, 6],
	'furnace': [7, 9, 13, 14], 'giant': [0, 4, 10, 12], 'giantpekka': [0, 1, 2, 4, 10],
	'giantskeleton': [0, 1, 4, 10, 15],
	'goblinbarrel': [1, 4, 14, 9], 'goblingang': [14, 1, 4, 9, 11], 'goblinhut': [14, 13, 11, 10, 4, 1],
	'goblins': [14, 4, 8, 1], 'golem': [0, 1, 4, 10, 12],
	'graveyard': [14, 5, 10], 'guards': [1, 14, 9, 4], 'heal': [9], 'hogrider': [4, 9, 12],
	'icegolem': [8, 12, 4, 1, 6],
	'icespirit': [11, 8, 6, 4], 'icewizard': [4, 6, 7, 9, 11], 'infernodragon': [0, 3, 1, 9, 11, 15],
	'infernotower': [1, 0, 10, 11, 13],
	'knight': [0, 9, 4], 'lavahound': [0, 3, 7, 10, 12, 15], 'lightning': [2, 5, 7, 10, 11], 'log': [5, 8],
	'lumberjack': [2, 1, 4, 9, 15],
	'megaminion': [1, 3, 2, 11, 9], 'miner': [4, 9, 12, 1, 0, 15], 'minionhorde': [14, 11, 10, 3, 1],
	'minions': [1, 3, 9, 11, 14],
	'minipekka': [1, 2, 4, 9], 'mirror': [14, 15], 'mortar': [0, 13, 7, 9], 'musketeer': [1, 4, 9, 11],
	'nightwitch': [14, 11, 9, 4, 2, 1],
	'poison': [5, 7, 9, 11], 'prince': [0, 1, 2, 4, 10], 'princess': [4, 7, 9, 11, 15], 'rage': [5, 8],
	'rocket': [2, 5, 10, 11],
	'royalgiant': [0, 12, 10, 4], 'skeletonarmy': [14, 9, 4], 'skeletons': [14, 8, 4, 1], 'sparky': [0, 2, 4, 7, 10],
	'speargoblins': [14, 11, 8, 4, 1],
	'tesla': [1, 13, 11, 9], 'threemusk': [1, 4, 10, 11, 14], 'tombstone': [14, 13, 9, 4], 'tornado': [5, 6, 7, 9, 11],
	'valkyrie': [1, 4, 7, 9],
	'witch': [14, 11, 10, 7, 4], 'wizard': [11, 10, 7, 4], 'xbow': [13, 10, 0], 'zap': [5, 6, 11, 8]}


####### NOMINAL VALUES ##########

N = len(cardDict) #number of cards
M = 33 #length of feature vector - also # of Attributes = M/2 - 1

####### CREATE DATA ARRAY #######

def updateData():
	file = open("brute_data", "r")
	curr_line = file.readlines()
	for line in curr_line:
		X_data = []
		Y_data = []
		temp = line.split(', ')
		results = list(map(int, temp))
		for i in range(len(results) - 1 - N):
			x = [name for name, index in cardDict.items() if (results[i] == 1 and index == i)]
			y = [name for name, index in cardDict.items() if (results[i+N] == 1 and index == i)]
			if(len(x) == 1):
				X_data.append(x[0])
			if (len(y) == 1):
				Y_data.append(y[0])
		winner = results[N*2]
		bruteDataToAttrData(X_data,Y_data,winner)
	file.close()

def bruteDataToAttrData(X_data, Y_data, winner):
	attr_data = [0] * M  # this is for attr_data
	for x in X_data:
		for attr in cardAttrDict[x]:
			attr_data[attr] += 1
	for y in Y_data:
		for attr in cardAttrDict[y]:
			attr_data[attr + int((M-1)/2)] += 1
	attr_data[M-1] = winner
	file = open("test_attr_data", "a")
	file.write(str(attr_data).strip('[]') + "\n")
	file.close()

updateData()