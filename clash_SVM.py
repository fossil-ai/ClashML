import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from sklearn import svm

X_samples_shape = (1,32)

def load_dataset():
	data = np.loadtxt('attr_data', delimiter=',')
	np.random.shuffle(data)
	train_percentage = 99
	half = int((data.shape[0]) * (train_percentage/100))
	Y_train = data[:half,data.shape[1] - 1]
	Y_test = data[half:, data.shape[1] - 1]
	X_data = sp.delete(data, data.shape[1] - 1, axis=1)
	X_train = X_data[:half]
	X_test = X_data[half:]
	Y_train = Y_train.astype(np.uint8)
	Y_test = Y_test.astype(np.uint8)
	return X_train, Y_train, X_test, Y_test

X_train, Y_train, X_test, Y_test = load_dataset()

# fit the model
clf = svm.SVC(kernel='linear')
clf.fit(X_train, Y_train)

print("CHECK AGAINST TRAINING DATA")

preds = clf.predict(X_train)

score = 0
print("TR || P")
for x,y in zip(Y_train, preds):
	print(str(x) + "  " + str(y))
	if x == y:
		score+=1

print(score/len(Y_train))

print("CHECK AGAINST TEST DATA")

preds = clf.predict(X_test)

score = 0
print("TS || P")
for x,y in zip(Y_test,preds):
	print(str(x) + "  " + str(y))
	if x == y:
		score+=1

print(score/len(Y_test))

