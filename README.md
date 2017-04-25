# Strategy Analysis of Clash Royale - A Supervised Learning Approach

Supercell's Clash Royale is a free mobile strategy game on various platforms mainly iOS/Android. The game takes an unconventional approach using 
card game concepts. Players collect and upgrade cards to use them for battle. Each deck may consist of 8 cards of the player's choosing. Once the battle begins
it is up to the players to figure out various strategies using these combos. 

## Task: 
Using information about two player's decks and who won the battle, learn a model that can predict the winner based only on the decks alone.

## Feature Engineering

Two completely separate data model approaches were were used. Each samples in the datasets corresponded to one battle.

### Approach 1:
Each sample vector **X** will be a (1 *x* 32) vector. 

The following features were analyzed:

0) DEFENSE - # of cards with high health
1) BRAWLERS - # of cards that attack one troop/building at a time ie. PEKKA
2) HARD-HITTERS - # of cards with high attack damage
3) FLYING - # of aerial troops
4) GROUND - # of ground troops
5) DAMAGE-SPELLS - Spell cards that cause damage or increase damage ie. Lightning, Fireball
6) STUN-SPELLS - Spells that slow down/stun/freeze movement
7) SPLASH - # of cards which cause splash damage
8) CHEAP - # of cards with low elixer cost (1-2)
9) MODERATE - # of cards with moderate elixer cost (3-4)
10) HIGH - # of cards with high elixer cost (5+)
11) AIR-DAMAGE - # of cards that can inflict damage to flying troops
12) BUILDING-BUSTERS - # of cards that specifically attack building cards/towers
13) BUILDING - # of building cards such as X-Bow, towers, etc.
14) MULTI - # of cards that either spawn with multiple troops or create multiple troops (3 or more)
15) TRICKY - # of cards has some unique attribute to it ie. Princess long range, Miner spawn freedom, etc.

#### Hence our sample vector had the following structure:

**X** = [DEFENSE_X, BRAWLERS_X ... TRICKY_X, DEFENSE_Y, BRAWLERS_Y ... TRICKY_ Y]

**Y** = 1 (Player X won)

**Y** = 0 (Player Y won)

### Approach 2:
Each sample vector **X** will be a (1 *x* 22) vector. 

0) AVG-HEALTH       - Average total hit points of each card
1) ELIXER-COST      - Average elixer cost of deck
2) AVG-ADPS         - Average attack damage per second
3) BUILDINGS        - # of building cards
4) SPLASH           - # of splash damage cards
5) STUNNERS         - # of cards with a stun/freeze effect
6) TRICKY           - # of cards with unique perks (princess, miner, clone)
7) MULTI            - # of multi-spawn cards
8) AIR-DAMAGE       - # of cards who can attack air troops
9) BUILDING-BUSTERS - # of cards who attack only building cards
10) DAMAGE-SPELLS   - # of card spells that cause damage


#### Hence our sample vector had the following structure:

**X** = [AVG-HEALTH_X, AVG_ELIXER-COST_X ... DAMAGE-SPELLS_X, AVG-HEALTH_Y, ... DAMAGE-SPELLS_Y]

**Y** = 1 (Player X won)

**Y** = 0 (Player Y won)

*data_collection_new.py* was the Python script that took input data about a battle, and then used pre-defined dictionary mappings to construct each
sample **X**. (Please look through the code for details)

## Machine Learning

Three algorithms were used to train 3 seperate models, each in their own respective Python script. Python libraries such as NumPy, scikit-learn, 
SciPy, Theano/Lasagne were used. Cross-validation with shuffling was used in every trial, where the data matrix would be shuffled and then split usually
80/20 for train/test.

1. Simple Neurel Net
2. Support Vector Machine
3. Random Forest

Several hundred trials were made for each algorithms and the accuracy was tested on the test data created from the cross validation split. Accuracy was averaged in order to obtain a 
estimated generalization accuracy of the model. Each hundreds of trials also involved tweaking hyperparameters of each algorithm. 
Results are shown below.

## Analysis:
[MORE TO COME :) - Collecting more samples!]
