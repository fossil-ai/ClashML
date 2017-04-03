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

####### CREATE DATA ARRAY #######

data = [0] * 151

####### INPUT MANUAL DATA #######

cards = input("Enter Player X's and Player Y's 8 cards (EACH), separate each card-name with DOUBLE whitespace '  ' and '?' for each player \n"
              "Example: A  B  C  D  E  F  G  H?I  J  K  L  M  N  O  P\n")
wins = input("Enter number of total wins and three crown wins for X followed by Y, separate player entries with a '?'\n"
             "Example: 435 123?546 234\n")
winner_str = input("Enter 1 if Player X won, or Enter 0 if Player Y won\n")

####### PARSE INPUT STRINGS #######

card_x = (cards.split("?"))[0].split("  ")
print(card_x)
card_y = (cards.split("?"))[1].split("  ")
print(card_y)

win_x  = (wins.split("?"))[0].split(" ")
win_y  = (wins.split("?"))[1].split(" ")

x_skills = int(win_x[1])/int(win_x[0])
print(x_skills)
y_skills = int(win_y[1])/int(win_y[0])
print(y_skills)

winner = int(winner_str)

####### INSERT INTO DATA ARRAY#######

for x in card_x:
	data[cardDict[x]] = 1
for y in card_y:
	data[cardDict[y] + 74] = 1

data[148] = x_skills
data[149] = y_skills
data[150] = winner

file = open("data","a")
file.write(str(data).strip('[]') + "\n")
file.close()








