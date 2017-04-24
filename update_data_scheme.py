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

infoDeckDict = {
	'golem': {'tricky': 0, 'ADPS': 160, 'stunner': 0, 'buildingbuster': 1, 'cost': 8, 'splash': 0, 'health': 7500,
	          'multi': 2, 'airdamage': 0, 'type': 'gtroop', 'building': 0},
	'fireball': {'tricky': 0, 'ADPS': 832, 'buildingbuster': 0, 'stunner': 0, 'cost': 4, 'splash': 1, 'health': 0,
	             'multi': 0, 'airdamage': 1, 'type': 'dspell', 'building': 0},
	'infernodragon': {'tricky': 1, 'ADPS': 650, 'stunner': 0, 'buildingbuster': 0, 'cost': 4, 'splash': 0,
	                  'health': 1460, 'multi': 0, 'airdamage': 1, 'type': 'atroop', 'building': 0},
	'bandit': {'tricky': 0, 'ADPS': 330, 'buildingbuster': 0, 'stunner': 0, 'cost': 3, 'splash': 0, 'health': 1095,
	           'multi': 0, 'airdamage': 0, 'type': 'gtroop', 'building': 0},
	'barbarianhut': {'tricky': 0, 'ADPS': 154, 'buildingbuster': 0, 'stunner': 0, 'cost': 7, 'splash': 0,
	                 'health': 2816, 'multi': 2, 'airdamage': 0, 'type': 'sbuilding', 'building': 1},
	'sparky': {'tricky': 0, 'ADPS': 260, 'buildingbuster': 0, 'stunner': 0, 'cost': 6, 'splash': 1, 'health': 1752,
	           'multi': 0, 'airdamage': 0, 'type': 'gtroop', 'building': 0},
	'hogrider': {'tricky': 0, 'ADPS': 256, 'buildingbuster': 1, 'stunner': 0, 'cost': 4, 'splash': 0, 'health': 2048,
	             'multi': 0, 'airdamage': 0, 'type': 'gtroop', 'building': 0},
	'rocket': {'tricky': 0, 'ADPS': 1792, 'buildingbuster': 0, 'stunner': 0, 'cost': 6, 'splash': 1, 'health': 0,
	           'multi': 0, 'airdamage': 1, 'type': 'dspell', 'building': 0},
	'electrowizard': {'tricky': 1, 'ADPS': 85, 'stunner': 1, 'buildingbuster': 0, 'cost': 4, 'splash': 1, 'health': 876,
	                  'multi': 0, 'airdamage': 1, 'type': 'gtroop', 'building': 0},
	'goblingang': {'tricky': 0, 'ADPS': 90, 'buildingbuster': 0, 'stunner': 0, 'cost': 3, 'splash': 0, 'health': 200,
	               'multi': 6, 'airdamage': 1, 'type': 'gtroop', 'building': 0},
	'goblinhut': {'tricky': 0, 'ADPS': 56, 'buildingbuster': 0, 'stunner': 0, 'cost': 5, 'splash': 0, 'health': 1881,
	              'multi': 1, 'airdamage': 1, 'type': 'sbuilding', 'building': 1},
	'poison': {'tricky': 0, 'ADPS': 110, 'buildingbuster': 0, 'stunner': 0, 'cost': 4, 'splash': 1, 'health': 0,
	           'multi': 0, 'airdamage': 1, 'type': 'dspell', 'building': 0},
	'dartgoblin': {'tricky': 0, 'ADPS': 207, 'buildingbuster': 0, 'stunner': 0, 'cost': 3, 'splash': 0, 'health': 314,
	               'multi': 0, 'airdamage': 1, 'type': 'gtroop', 'building': 0},
	'speargoblins': {'tricky': 0, 'ADPS': 56, 'buildingbuster': 0, 'stunner': 0, 'cost': 2, 'splash': 0, 'health': 160,
	                 'multi': 3, 'airdamage': 1, 'type': 'gtroop', 'building': 0},
	'elitebarbarians': {'tricky': 0, 'ADPS': 246, 'buildingbuster': 0, 'stunner': 0, 'cost': 6, 'splash': 0,
	                    'health': 1415, 'multi': 2, 'airdamage': 0, 'type': 'gtroop', 'building': 0},
	'royalgiant': {'tricky': 0, 'ADPS': 135, 'buildingbuster': 1, 'stunner': 0, 'cost': 6, 'splash': 0, 'health': 3708,
	               'multi': 0, 'airdamage': 0, 'type': 'gtroop', 'building': 0},
	'firespirits': {'tricky': 0, 'ADPS': 247, 'buildingbuster': 0, 'stunner': 0, 'cost': 2, 'splash': 1, 'health': 132,
	                'multi': 3, 'airdamage': 1, 'type': 'gtroop', 'building': 0},
	'megaminion': {'tricky': 0, 'ADPS': 250, 'buildingbuster': 0, 'stunner': 0, 'cost': 3, 'splash': 0, 'health': 1011,
	               'multi': 0, 'airdamage': 1, 'type': 'atroop', 'building': 0},
	'barbarians': {'tricky': 0, 'ADPS': 154, 'buildingbuster': 0, 'stunner': 0, 'cost': 5, 'splash': 0, 'health': 927,
	               'multi': 4, 'airdamage': 0, 'type': 'gtroop', 'building': 0},
	'prince': {'tricky': 0, 'ADPS': 314, 'stunner': 0, 'buildingbuster': 0, 'cost': 5, 'splash': 0, 'health': 2123,
	           'multi': 0, 'airdamage': 0, 'type': 'gtroop', 'building': 0},
	'zap': {'tricky': 0, 'ADPS': 231, 'buildingbuster': 0, 'stunner': 1, 'cost': 2, 'splash': 1, 'health': 0,
	        'multi': 0, 'airdamage': 1, 'type': 'espell', 'building': 0},
	'knight': {'tricky': 0, 'ADPS': 210, 'buildingbuster': 0, 'stunner': 0, 'cost': 3, 'splash': 0, 'health': 2039,
	           'multi': 0, 'airdamage': 0, 'type': 'gtroop', 'building': 0},
	'icespirit': {'tricky': 0, 'ADPS': 139, 'buildingbuster': 0, 'stunner': 1, 'cost': 1, 'splash': 1, 'health': 278,
	              'multi': 0, 'airdamage': 1, 'type': 'gtroop', 'building': 0},
	'bats': {'tricky': 0, 'ADPS': 98, 'buildingbuster': 0, 'stunner': 0, 'cost': 2, 'splash': 0, 'health': 98,
	         'multi': 5, 'airdamage': 1, 'type': 'atroop', 'building': 0},
	'balloon': {'tricky': 0, 'ADPS': 386, 'stunner': 0, 'buildingbuster': 1, 'cost': 5, 'splash': 0, 'health': 2026,
	            'multi': 0, 'airdamage': 0, 'type': 'atroop', 'building': 0},
	'darkprince': {'tricky': 1, 'ADPS': 186, 'stunner': 0, 'buildingbuster': 0, 'cost': 4, 'splash': 0, 'health': 1700,
	               'multi': 0, 'airdamage': 0, 'type': 'gtroop', 'building': 0},
	'minions': {'tricky': 0, 'ADPS': 123, 'buildingbuster': 0, 'stunner': 0, 'cost': 3, 'splash': 0, 'health': 278,
	            'multi': 3, 'airdamage': 1, 'type': 'atroop', 'building': 0},
	'bowler': {'tricky': 1, 'ADPS': 138, 'stunner': 0, 'buildingbuster': 0, 'cost': 5, 'splash': 1, 'health': 2316,
	           'multi': 0, 'airdamage': 0, 'type': 'gtroop', 'building': 0},
	'princess': {'tricky': 1, 'ADPS': 68, 'stunner': 0, 'buildingbuster': 0, 'cost': 3, 'splash': 1, 'health': 315,
	             'multi': 0, 'airdamage': 1, 'type': 'gtroop', 'building': 0},
	'musketeer': {'tricky': 0, 'ADPS': 232, 'buildingbuster': 0, 'stunner': 0, 'cost': 4, 'splash': 0, 'health': 870,
	              'multi': 0, 'airdamage': 1, 'type': 'gtroop', 'building': 0},
	'arrows': {'tricky': 0, 'ADPS': 355, 'buildingbuster': 0, 'stunner': 0, 'cost': 3, 'splash': 1, 'health': 0,
	           'multi': 0, 'airdamage': 1, 'type': 'dspell', 'building': 0},
	'lumberjack': {'tricky': 1, 'ADPS': 414, 'stunner': 0, 'buildingbuster': 0, 'cost': 4, 'splash': 0, 'health': 1445,
	               'multi': 0, 'airdamage': 0, 'type': 'gtroop', 'building': 0},
	'nightwitch': {'tricky': 1, 'ADPS': 277, 'stunner': 0, 'buildingbuster': 0, 'cost': 4, 'splash': 0, 'health': 1095,
	               'multi': 1, 'airdamage': 1, 'type': 'gtroop', 'building': 0},
	'mortar': {'tricky': 0, 'ADPS': 66, 'buildingbuster': 0, 'stunner': 0, 'cost': 4, 'splash': 1, 'health': 1854,
	           'multi': 0, 'airdamage': 0, 'type': 'dbuilding', 'building': 1},
	'executioner': {'tricky': 1, 'ADPS': 170, 'stunner': 0, 'buildingbuster': 0, 'cost': 5, 'splash': 1, 'health': 1466,
	                'multi': 0, 'airdamage': 1, 'type': 'gtroop', 'building': 0},
	'collector': {'tricky': 1, 'ADPS': 0, 'buildingbuster': 0, 'stunner': 0, 'cost': 6, 'splash': 0, 'health': 1484,
	              'multi': 0, 'airdamage': 0, 'type': 'sbuilding', 'building': 1},
	'lightning': {'tricky': 0, 'ADPS': 1254, 'buildingbuster': 0, 'stunner': 0, 'cost': 6, 'splash': 1, 'health': 0,
	              'multi': 0, 'airdamage': 1, 'type': 'dspell', 'building': 0},
	'miner': {'tricky': 1, 'ADPS': 194, 'stunner': 0, 'buildingbuster': 1, 'cost': 3, 'splash': 0, 'health': 1460,
	          'multi': 0, 'airdamage': 0, 'type': 'gtroop', 'building': 0},
	'icegolem': {'tricky': 0, 'ADPS': 40, 'buildingbuster': 1, 'stunner': 1, 'cost': 2, 'splash': 0, 'health': 1523,
	             'multi': 0, 'airdamage': 0, 'type': 'gtroop', 'building': 0},
	'skeletonarmy': {'tricky': 0, 'ADPS': 98, 'stunner': 0, 'buildingbuster': 0, 'cost': 3, 'splash': 0, 'health': 98,
	                 'multi': 14, 'airdamage': 0, 'type': 'gtroop', 'building': 0},
	'minipekka': {'tricky': 0, 'ADPS': 462, 'buildingbuster': 0, 'stunner': 0, 'cost': 4, 'splash': 0, 'health': 1536,
	              'multi': 0, 'airdamage': 0, 'type': 'gtroop', 'building': 0},
	'tornado': {'tricky': 1, 'ADPS': 84, 'buildingbuster': 0, 'stunner': 1, 'cost': 3, 'splash': 1, 'health': 0,
	            'multi': 0, 'airdamage': 1, 'type': 'dspell', 'building': 0},
	'bombtower': {'tricky': 0, 'ADPS': 160, 'buildingbuster': 0, 'stunner': 0, 'cost': 5, 'splash': 1, 'health': 2436,
	              'multi': 0, 'airdamage': 0, 'type': 'dbuilding', 'building': 1},
	'babydragon': {'tricky': 0, 'ADPS': 120, 'stunner': 0, 'buildingbuster': 1, 'cost': 4, 'splash': 1, 'health': 1544,
	               'multi': 0, 'airdamage': 0, 'type': 'atroop', 'building': 0},
	'cannon': {'tricky': 0, 'ADPS': 231, 'buildingbuster': 0, 'stunner': 0, 'cost': 3, 'splash': 0, 'health': 1081,
	           'multi': 0, 'airdamage': 0, 'type': 'dbuilding', 'building': 1},
	'infernotower': {'tricky': 1, 'ADPS': 1850, 'buildingbuster': 0, 'stunner': 0, 'cost': 5, 'splash': 0,
	                 'health': 2048, 'multi': 0, 'airdamage': 1, 'type': 'dbuilding', 'building': 1},
	'giantpekka': {'tricky': 0, 'ADPS': 546, 'stunner': 0, 'buildingbuster': 0, 'cost': 7, 'splash': 0, 'health': 5018,
	               'multi': 0, 'airdamage': 0, 'type': 'gtroop', 'building': 0},
	'battleram': {'tricky': 1, 'ADPS': 716, 'buildingbuster': 1, 'stunner': 0, 'cost': 4, 'splash': 0, 'health': 1100,
	              'multi': 2, 'airdamage': 0, 'type': 'gtroop', 'building': 0},
	'valkyrie': {'tricky': 0, 'ADPS': 204, 'buildingbuster': 0, 'stunner': 0, 'cost': 4, 'splash': 1, 'health': 2252,
	             'multi': 0, 'airdamage': 0, 'type': 'gtroop', 'building': 0},
	'mirror': {'tricky': 1, 'ADPS': 0, 'buildingbuster': 0, 'stunner': 0, 'cost': 3, 'splash': 0, 'health': 0,
	           'multi': 0, 'airdamage': 0, 'type': 'espell', 'building': 0},
	'rage': {'tricky': 1, 'ADPS': 0, 'buildingbuster': 0, 'stunner': 0, 'cost': 4, 'splash': 0, 'health': 0, 'multi': 0,
	         'airdamage': 0, 'type': 'espell', 'building': 0},
	'goblins': {'tricky': 0, 'ADPS': 140, 'buildingbuster': 0, 'stunner': 0, 'cost': 2, 'splash': 0, 'health': 247,
	            'multi': 3, 'airdamage': 0, 'type': 'gtroop', 'building': 0},
	'clone': {'tricky': 1, 'ADPS': 0, 'buildingbuster': 0, 'stunner': 0, 'cost': 3, 'splash': 0, 'health': 0,
	          'multi': 1, 'airdamage': 0, 'type': 'espell', 'building': 0},
	'goblinbarrel': {'tricky': 1, 'ADPS': 140, 'buildingbuster': 1, 'stunner': 0, 'cost': 3, 'splash': 0, 'health': 247,
	                 'multi': 3, 'airdamage': 0, 'type': 'gtroop', 'building': 0},
	'furnace': {'tricky': 0, 'ADPS': 247, 'buildingbuster': 0, 'stunner': 0, 'cost': 4, 'splash': 1, 'health': 1459,
	            'multi': 2, 'airdamage': 1, 'type': 'sbuilding', 'building': 1},
	'lavahound': {'tricky': 1, 'ADPS': 55, 'stunner': 0, 'buildingbuster': 1, 'cost': 7, 'splash': 0, 'health': 5500,
	              'multi': 7, 'airdamage': 1, 'type': 'atroop', 'building': 0},
	'minionhorde': {'tricky': 0, 'ADPS': 123, 'buildingbuster': 0, 'stunner': 0, 'cost': 5, 'splash': 0, 'health': 278,
	                'multi': 6, 'airdamage': 1, 'type': 'atroop', 'building': 0},
	'guards': {'tricky': 1, 'ADPS': 104, 'stunner': 0, 'buildingbuster': 0, 'cost': 3, 'splash': 0, 'health': 400,
	           'multi': 3, 'airdamage': 0, 'type': 'gtroop', 'building': 0},
	'threemusk': {'tricky': 0, 'ADPS': 232, 'buildingbuster': 0, 'stunner': 0, 'cost': 9, 'splash': 0, 'health': 870,
	              'multi': 3, 'airdamage': 1, 'type': 'gtroop', 'building': 0},
	'tesla': {'tricky': 0, 'ADPS': 246, 'buildingbuster': 0, 'stunner': 0, 'cost': 4, 'splash': 0, 'health': 1390,
	          'multi': 0, 'airdamage': 1, 'type': 'dbuilding', 'building': 1},
	'giant': {'tricky': 0, 'ADPS': 204, 'buildingbuster': 1, 'stunner': 0, 'cost': 5, 'splash': 0, 'health': 4864,
	          'multi': 0, 'airdamage': 0, 'type': 'gtroop', 'building': 0},
	'log': {'tricky': 1, 'ADPS': 350, 'buildingbuster': 0, 'stunner': 1, 'cost': 2, 'splash': 1, 'health': 0,
	        'multi': 0, 'airdamage': 0, 'type': 'dspell', 'building': 0},
	'bomber': {'tricky': 0, 'ADPS': 207, 'stunner': 0, 'buildingbuster': 0, 'cost': 3, 'splash': 1, 'health': 454,
	           'multi': 0, 'airdamage': 0, 'type': 'gtroop', 'building': 0},
	'archers': {'tricky': 0, 'ADPS': 105, 'buildingbuster': 0, 'stunner': 0, 'cost': 3, 'splash': 0, 'health': 370,
	            'multi': 2, 'airdamage': 1, 'type': 'gtroop', 'building': 0},
	'wizard': {'tricky': 0, 'ADPS': 237, 'buildingbuster': 0, 'stunner': 0, 'cost': 5, 'splash': 1, 'health': 870,
	           'multi': 0, 'airdamage': 1, 'type': 'gtroop', 'building': 0},
	'tombstone': {'tricky': 0, 'ADPS': 98, 'buildingbuster': 0, 'stunner': 0, 'cost': 3, 'splash': 0, 'health': 614,
	              'multi': 1, 'airdamage': 0, 'type': 'sbuilding', 'building': 1},
	'icewizard': {'tricky': 1, 'ADPS': 60, 'stunner': 1, 'buildingbuster': 0, 'cost': 3, 'splash': 1, 'health': 970,
	              'multi': 0, 'airdamage': 1, 'type': 'gtroop', 'building': 0},
	'skeletons': {'tricky': 0, 'ADPS': 98, 'buildingbuster': 0, 'stunner': 0, 'cost': 1, 'splash': 0, 'health': 98,
	              'multi': 4, 'airdamage': 0, 'type': 'gtroop', 'building': 0},
	'graveyard': {'tricky': 0, 'ADPS': 98, 'buildingbuster': 0, 'stunner': 0, 'cost': 5, 'splash': 0, 'health': 98,
	              'multi': 17, 'airdamage': 0, 'type': 'gtroop', 'building': 0},
	'freeze': {'tricky': 0, 'ADPS': 0, 'buildingbuster': 0, 'stunner': 1, 'cost': 4, 'splash': 0, 'health': 0,
	           'multi': 0, 'airdamage': 0, 'type': 'espell', 'building': 0},
	'witch': {'tricky': 1, 'ADPS': 142, 'stunner': 0, 'buildingbuster': 0, 'cost': 5, 'splash': 1, 'health': 965,
	          'multi': 1, 'airdamage': 1, 'type': 'gtroop', 'building': 0},
	'heal': {'tricky': 0, 'ADPS': 256, 'buildingbuster': 0, 'stunner': 0, 'cost': 3, 'splash': 0, 'health': 0,
	         'multi': 0, 'airdamage': 0, 'type': 'espell', 'building': 0},
	'giantskeleton': {'tricky': 1, 'ADPS': 166, 'stunner': 0, 'buildingbuster': 0, 'cost': 6, 'splash': 1,
	                  'health': 3860, 'multi': 0, 'airdamage': 0, 'type': 'gtroop', 'building': 0},
	'xbow': {'tricky': 0, 'ADPS': 152, 'buildingbuster': 0, 'stunner': 0, 'cost': 6, 'splash': 0, 'health': 1930,
	         'multi': 0, 'airdamage': 0, 'type': 'dbuilding', 'building': 1}}

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

N = len(cardDict)  # number of cards
M = 23  # length of feature vector - also # of Attributes = M/2 - 1
M0 = 33

####### CREATE DATA ARRAY #######

def updateData():
	file = open("raw_data", "r")
	curr_line = file.readlines()
	for line in curr_line:
		X_data = []
		Y_data = []
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
		bruteDataToAttrData_1(X_data, Y_data, winner)
		bruteDataToAttrData(X_data, Y_data, winner)
	file.close()


def bruteDataToAttrData_1(X_data, Y_data, winner):
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
	attr_data[0] = attr_data[0] / tx
	attr_data[2] = attr_data[2] / tx
	attr_data[11] = attr_data[11] / ty
	attr_data[13] = attr_data[13] / tx
	attr_data[22] = winner
	file = open("approach2_data", "a")
	file.write(str(attr_data).strip('[]') + "\n")
	file.close()


def bruteDataToAttrData(X_data, Y_data, winner):
	attr_data = [0] * M0  # this is for approach1_data
	for x in X_data:
		for attr in cardAttrDict[x]:
			attr_data[attr] += 1
	for y in Y_data:
		for attr in cardAttrDict[y]:
			attr_data[attr + int((M0-1)/2)] += 1
	attr_data[M0-1] = winner
	file = open("approach1_data", "a")
	file.write(str(attr_data).strip('[]') + "\n")
	file.close()


updateData()
