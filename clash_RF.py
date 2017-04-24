from sklearn.ensemble import RandomForestClassifier
import numpy as np
import scipy as sp
from sklearn import preprocessing

M = 33
K = int((M-1)/2)
X_samples_shape = (1,M-1)
trials = 50
accuracy_train = 0
accuracy_test = 0

# features = ['HEALTH_X','COST_X','ADPS_X','BUILDINGS_X','SPLASH_X','STUNNER_X','TRICKY_X','MULTI_X','AIRDAMAGE_X','BB_X','DSPELL_X',
#             'HEALTH_Y', 'COST_Y', 'ADPS_Y', 'BUILDINGS_Y', 'SPLASH_Y', 'STUNNER_Y', 'TRICKY_Y', 'MULTI_Y', 'AIRDAMAGE_Y', 'BB_Y', 'DSPELL_Y']
#
# features_rank = {'HEALTH_X':0,'COST_X':0,'ADPS_X':0,'BUILDINGS_X':0,'SPLASH_X':0,'STUNNER_X':0,'TRICKY_X':0,'MULTI_X':0,'AIRDAMAGE_X':0,'BB_X':0,'DSPELL_X':0,
#             'HEALTH_Y':0, 'COST_Y':0, 'ADPS_Y':0, 'BUILDINGS_Y':0, 'SPLASH_Y':0, 'STUNNER_Y':0, 'TRICKY_Y':0, 'MULTI_Y':0, 'AIRDAMAGE_Y':0, 'BB_Y':0, 'DSPELL_Y':0}

features = ['DEFENSE_X','BRAWLERS_X','HARD-HITTERS__X', 'FLYING_X', 'GROUND_X' ,'DAMAGE-SPELLS_X' ,'STUN-SPELLS_X' ,'SPLASH_X' ,'CHEAP_X' ,'MODERATE_X' ,
            'HIGH_X' ,'AIR-DAMAGE_X', 'BUILDING-BUSTERS_X', 'BUILDING_X', 'MULTI_X', 'TRICKY_X', 'DEFENSE_Y','BRAWLERS_Y','HARD-HITTERS_Y',
            'FLYING_Y', 'GROUND_Y' ,'DAMAGE-SPELLS_Y' ,'STUN-SPELLS_Y' ,'SPLASH_Y' ,'CHEAP_Y' ,'MODERATE_Y' ,
             'HIGH_Y' ,'AIR-DAMAGE_Y', 'BUILDING-BUSTERS_Y', 'BUILDING_Y', 'MULTI_Y', 'TRICKY_Y']

features_rank = {'DEFENSE_X':0,'BRAWLERS_X':0,'HARD-HITTERS__X':0, 'FLYING_X':0, 'GROUND_X':0 ,'DAMAGE-SPELLS_X':0,'STUN-SPELLS_X' :0 ,'SPLASH_X' :0,'CHEAP_X' :0,'MODERATE_X':0 ,
            'HIGH_X' :0,'AIR-DAMAGE_X':0, 'BUILDING-BUSTERS_X':0, 'BUILDING_X':0, 'MULTI_X':0, 'TRICKY_X':0, 'DEFENSE_Y':0,'BRAWLERS_Y':0,'HARD-HITTERS_Y':0,
            'FLYING_Y':0, 'GROUND_Y' :0,'DAMAGE-SPELLS_Y':0 ,'STUN-SPELLS_Y':0 ,'SPLASH_Y' :0,'CHEAP_Y' :0,'MODERATE_Y' :0,
             'HIGH_Y' :0,'AIR-DAMAGE_Y':0, 'BUILDING-BUSTERS_Y':0, 'BUILDING_Y':0, 'MULTI_Y':0, 'TRICKY_Y':0}


def standardize(X,y):
	a = preprocessing.StandardScaler()
	new = a.fit_transform(X,y)
	return new

def normalize(X,y):
	a = preprocessing.Normalizer()
	new = a.fit_transform(X,y)
	return new

def load_dataset():
	data = np.loadtxt('attr_data', delimiter=',')
	np.random.shuffle(data)
	train_perc = 85
	half = int((data.shape[0]) * (train_perc / 100))

	# LABEL DATA
	Y_train = data[:half, data.shape[1] - 1]
	Y_train_1 = [0] * half
	for i in range(half):
		Y_train_1[i] = (~ int(np.asscalar(Y_train[i]))) + 2
	Y_train = np.concatenate((Y_train, Y_train_1), axis=0)
	Y_test = data[half:, data.shape[1] - 1]

	# SAMPLE DATA
	X_data = sp.delete(data, data.shape[1] - 1, axis=1)
	X_train = X_data[:half]
	X_train_1 = np.copy(X_train)
	for i in X_train_1:
		temp = np.copy(i[:K])
		i[:K] = np.copy(i[K:])
		i[K:] = temp
	X_train = np.concatenate((X_train, X_train_1), axis=0)
	X_test = X_data[half:]
	Y_train = Y_train.astype(np.uint8)
	Y_test = Y_test.astype(np.uint8)


	#SCALING AND PREPROCESSING
	#Standardizing hurt performance, so stick with normalization
	X_train = normalize(X_train,Y_train)
	X_test = normalize(X_test,Y_test)


	return X_train, Y_train, X_test, Y_test

for i in range(trials):
	print("Starting Trial {}".format(i))
	X_train, Y_train, X_test, Y_test = load_dataset()
	# fit the model,
	clf = RandomForestClassifier(n_estimators=15, max_features=None, random_state=0,n_jobs=-1)
	clf.fit(X_train, Y_train)
	feature_imp = clf.feature_importances_
	indices = np.argsort(feature_imp)[::-1]
	for f in range(M-1):
		#print("%2d) %-*s %f" % (f+1,30,features[indices[f]],feature_imp[indices[f]]))
		features_rank[features[indices[f]]] += feature_imp[indices[f]]


	# print("CHECK AGAINST TRAINING DATA")

	preds = clf.predict(X_train)

	score = 0
	# print("TR || P")
	for x,y in zip(Y_train, preds):
		#print(str(x) + "  " + str(y))
		if x == y:
			score+=1

	accuracy_tr = score/len(Y_train)
	accuracy_train += accuracy_tr
	# print(score/len(Y_train))

	# print("CHECK AGAINST TEST DATA")

	preds = clf.predict(X_test)

	score = 0
	# print("TS || P")
	for x,y in zip(Y_test,preds):
		#print(str(x) + "  " + str(y))
		if x == y:
			score+=1

	accuracy_ts = score / len(Y_test)
	accuracy_test += accuracy_ts


print('TRAINING ACCURACY IS: {}'.format(str(accuracy_train/trials)))
print('TEST ACCURACY IS: {} \n'.format(str(accuracy_test/trials)))

# FEATURE RANKING
for i in features_rank:
	features_rank[i] = features_rank[i]/trials

print(" ---  FEATURE IMPORTANCE --- \n")
for w in sorted(features_rank, key=features_rank.get, reverse=True):
	print('{} : {}'.format(w, features_rank[w]))