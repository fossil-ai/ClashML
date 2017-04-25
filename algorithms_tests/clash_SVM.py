import numpy as np
import scipy as sp
from sklearn import svm
from sklearn import preprocessing
import os

# get current working directory
currDir = os.getcwd()

M = 23 # number of features plus label for Approach 2 (23) and Approach 1 (33)
K = int((M-1)/2) # number of features for one player
X_samples_shape = (1,M-1) # Dimension of one sample data

# number of trials to run
trials = 250

# initialize accuracy score
accuracy_train = 0
accuracy_test = 0

def standardize(X,y):
	a = preprocessing.StandardScaler()
	new = a.fit_transform(X,y)
	return new

def normalize(X,y):
	a = preprocessing.Normalizer()
	new = a.fit_transform(X,y)
	return new

def load_dataset():
	data = np.loadtxt(currDir + "/datasets/approach2_data", delimiter=',')
	np.random.shuffle(data) # Shuffle data to obtain randomness between trials
	train_perc = 90 # Cross Validation Split
	cross = int((data.shape[0]) * (train_perc / 100))

	# LABEL DATA
	Y_train = data[:cross, data.shape[1] - 1]
	Y_train_1 = [0] * cross
	for i in range(cross):
		Y_train_1[i] = (~ int(np.asscalar(Y_train[i]))) + 2
	Y_train = np.concatenate((Y_train, Y_train_1), axis=0)
	Y_test = data[cross:, data.shape[1] - 1]
	Y_train = Y_train.astype(np.uint8)
	Y_test = Y_test.astype(np.uint8)

	# SAMPLE DATA
	X_data = sp.delete(data, data.shape[1] - 1, axis=1)
	X_train = X_data[:cross]
	X_train_1 = np.copy(X_train)
	for i in X_train_1:
		temp = np.copy(i[:K])
		i[:K] = np.copy(i[K:])
		i[K:] = temp
	X_train = np.concatenate((X_train, X_train_1), axis=0)
	X_test = X_data[cross:]

	# PREPROCESSING
	X_train = standardize(X_train, Y_train)
	X_test = standardize(X_test, Y_test)

	return X_train, Y_train, X_test, Y_test

for i in range(trials):
	print("Starting Trial {}".format(i))
	X_train, Y_train, X_test, Y_test = load_dataset()

	# Fit SVM Model
	clf = svm.SVC(kernel='rbf', C=2, probability=True)
	clf.fit(X_train, Y_train)

	# PREDICT ON TRAINING DATA
	preds = clf.predict(X_train)
	score = 0
	for x,y in zip(Y_train, preds):
		if x == y:
			score+=1

	accuracy_tr = score/len(Y_train)
	accuracy_train += accuracy_tr

	# PREDICT ON TEST DATA
	preds = clf.predict(X_test)
	score = 0
	for x,y in zip(Y_test,preds):
		if x == y:
			score+=1

	accuracy_ts = score / len(Y_test)
	accuracy_test += accuracy_ts


print('TRAINING ACCURACY IS: {}'.format(str(accuracy_train/trials)))
print('TEST ACCURACY IS: {}'.format(str(accuracy_test/trials)))
