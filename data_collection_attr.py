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

14) MULTI - Cards that either spawn with multiple troops or create multiple troops


SAMPLE DATA WILL BE STRUCTURED AS FOLLOWS:

X = [PLAYER 1 ATTRIBUTES, PLAYER 2 ATTRIBUTES, WINNER] - Size of sample data is: N = (2 * # of Attributes) + 1

'''

cardDict = {'mirror': [14], 'graveyard': [14, 5, 10], 'bombtower': [0,7,10, 13], 'guards': [1, 14, 9, 4], 'rage': [5, 8], 'furnace': 47, 'barbarians': 40,
            'elitebarbarians': 36, 'speargoblin': 24, 'minipekka': 38, 'icegolem': 17, 'valkyrie': 61, 'threemusk': 51, 'firespirits': 46,
            'cannon': 9, 'fireball': 58, 'clone': 8, 'poison': 2, 'rocket': 11, 'skeletons': 41, 'battleram': 37, 'musketeer': 19,
            'megaminion': 65, 'log': 21, 'hogrider': 27, 'collector': 52, 'heal': 66, 'knight': 73, 'bomber': 6, 'icespirit': 5,
            'wizard': 57, 'darkprincess': 4, 'tombstone': 56, 'tornado': 22, 'executioner': 31, 'bandit': 48, 'infernotower': 67,
            'icewizard': 45, 'archer': 54, 'balloon': 60, 'miner': 26, 'royalgiant': 3, 'golem': 71, 'darkprince': 23, 'mortar': 0,
            'arrows': 72, 'bats': 16, 'nightwitch': 70, 'electrowizard': 55, 'witch': 69, 'giantpekka': 35, 'barbarianhut': 30,
            'lightning': 42, 'zap': 32, 'minions': 28, 'minionhorde': 63, 'dartgoblin': 44, 'goblinhut': 68, 'infernodragon': 18,
            'sparky': 39, 'tesla': 59, 'prince': 14, 'lavahound': 62, 'skeletonarmy': 33, 'babydragon': 50, 'goblinbarrel': 15,
            'giantskeleton': 25, 'freeze': 43, 'lumberjack': 13, 'xbow': 1, 'bowler': 12, 'goblingang': 20, 'princess': 7, 'goblins': 53,
            'giant':74}