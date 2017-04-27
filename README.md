# Strategy Analysis of Clash Royale - A Supervised Learning Approach

![Alt text](https://cloud.githubusercontent.com/assets/13232148/25375697/9137fcfe-296f-11e7-9778-6ab978515fb5.jpg)

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

*collect_data.py* was the Python script that took input data about a battle, and then used pre-defined dictionary mappings to construct each
sample **X**. (Please look through the code for details)

## Machine Learning

Three algorithms were used to train 3 seperate models, each in their own respective Python script. Python libraries such as NumPy, scikit-learn, 
SciPy, Theano/Lasagne were used. Cross-validation with shuffling was used in every trial, where the data matrix would be shuffled and then split usually
80/20 for train/test.

1. Simple Neural Net
2. Support Vector Machine
3. Random Forest

Several hundred trials were made for each algorithms and the accuracy was tested on the test data created from the cross validation split. Accuracy was averaged in order to obtain a 
estimated generalization accuracy of the model. Each hundreds of trials also involved tweaking hyperparameters of each algorithm. 
Results are shown below.

## Analysis:

For each algorithm, the data matrix was shuffled before the cross-validation splits.

 **Neural Net (Theano/Lasagne) - Each CV split was averaged over 50 trials (NN on approach2_data was so terrible, I didn't bother doing an analysis on it. So this is only for approach1_data)**
 
 Parameters: 
 
 learning rate = 0.05, max # of epochs = 250, Layers [Input, Dense (64 units), Dropout (*p=0.25*), Output]

| Cross-Validation Split (Train/Test)|   Training Accuracy  | Test Accuracy  |
| :-------------:|:-------------:| :-----:|
| 60/40         | 90.91%      | 60.45% |
| 80/20         | 91.81% |   65.5% |
| 95/5 | 92.86%    |    63.0% |

**Support Vector Machine (scikit-learn) - Each CV split was averaged over 250 trials, done on both datasets. We do not particular care about the training accuracy, so we will look at only test accuracy** 

Parameters:
penalty term of error *C* = 2, kernal = RBF

| Cross-Validation Split (Train/Test)|  Test Accuracy (Approach 1 Dataset) | Test Accuracy (Approach 2 Dataset) |
| :-------------: |:-------------:| :-------------:|
| 60/40         | 65.69%      | 66.56% |
| 80/20         | 67.92% |   68.43% |
| 95/5 | 65.30%   |   65.20% |

So far for both SVM and NN, test accuracy was higher on the 80/20 split. I guess that's why it's conventional :)

** Random Forest Classifier (RFC) (scikit-learn) - Each CV split per dataset was averaged over 100 trials. The RandomForestClassifier API provided a very nice feature (.feature_importances) which I assumes ranks the features we decided on in the order they contribute the most to the binary classification decision.** 

Parameters:
number of trees in forest = 15 

| Cross-Validation Split (Train/Test)|  Test Accuracy (Approach 1 Dataset) | Test Accuracy (Approach 2 Dataset) |
| :-------------: |:-------------:| :-------------:|
| 60/40         | 66.06%      | 66.80% |
| 80/20         | 66.50% |   `68.56%`  |
| 95/5 | 64.25%   |   `69.00%` |

Interesting how the 95/5 split for Approach 2 gave 69% where it performed much lower for Approach 1. To be honest, it's hard to predict much based on only 77 samples, so I will be updating results here and there once I collect more in the future (or you can collect some as well :D ). Getting the feature importance from the RFC gave the following for the 95/5 split on Approach 2:

ADPS_Y : 0.1585116432655841
ADPS_X : 0.15705471661361553
AIRDAMAGE_Y : 0.04008767428358454
BB_Y : 0.03981336635515329
AIRDAMAGE_X : 0.039719407378624456
HEALTH_Y : 0.03927363435433432
BUILDINGS_Y : 0.038275569313462696
TRICKY_Y : 0.03679796389356237
DSPELL_X : 0.03629248739955291
TRICKY_X : 0.03618435955547795
BUILDINGS_X : 0.03584786846806187
BB_X : 0.03549451997354712
SPLASH_Y : 0.03448379427572234
SPLASH_X : 0.03328395369083422
DSPELL_Y : 0.033145979606698045
MULTI_Y : 0.03246443066060067
HEALTH_X : 0.03180474329703207
MULTI_X : 0.03180109137800274
STUNNER_Y : 0.03125509994131526
STUNNER_X : 0.03108361712571109
COST_X : 0.024086202652025778
COST_Y : 0.02323787651749665

Whereas many of the features for player X and Y contribute roughly ~2-4% each, the ADPS_X,ADPS_Y features, which stood for Attack Damage Per Second (averaged over the deck), had a whopping combined total of ~30% importance. This should not come as a surprise, but it shows that since we do not have direct access to the average damage per second of a DECK like we do for the average cost of the deck (which happened to be the least contributing factor), that it's often overlooked by many players. 

Anyhow, with only 77 samples, Random Forest performed the best, then SVM, and then NN. To be honest NN might be terrible for this case. Especially with the small amount of samples. 

Remember this was BINARY CLASSIFICATION. A test accuracy of 50% would have meant this study was pointless, since 50% is random guessing. BUT, but we must remember, without observing the actual gameplay or skills of the players, we are trying to predict the winner. So even reaching 75% test accuracy would be pretty impressive for judging a winner solely on deck composition. Maybe if we had about 1000 samples, we could see some exciting patterns! Well that is all from me. I encourage those reading this to use what I have so far and tweak whatever they see fit. I'm no machine learning expert, so I'm sure there are plenty of other algorithms to try, and hyperparamters to tune! Good Luck!


