import numpy as np
import scipy as sp
import lasagne
from lasagne import layers
from lasagne.updates import nesterov_momentum
from nolearn.lasagne import NeuralNet
from sklearn import preprocessing


M = 33
K = int((M-1)/2)
X_samples_shape = (1,M-1)
trials = 25
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
	data = np.loadtxt('approach1_data', delimiter=',')
	np.random.shuffle(data)
	train_perc = 80
	half = int((data.shape[0]) * (train_perc/100))

	# LABEL DATA
	Y_train = data[:half,data.shape[1] - 1]
	Y_train_1 = [0] * half
	for i in range(half):
		Y_train_1[i] = (~ int(np.asscalar(Y_train[i]))) + 2
	Y_train = np.concatenate((Y_train,Y_train_1), axis= 0)
	Y_test = data[half :, data.shape[1] - 1]

	# SAMPLE DATA
	X_data = sp.delete(data, data.shape[1] - 1, axis=1)
	X_train = X_data[:half]
	X_train_1 = np.copy(X_train)
	for i in X_train_1:
		temp = np.copy(i[:K])
		i[:K] = np.copy(i[K:])
		i[K:] = temp
	X_train = np.concatenate((X_train,X_train_1),axis=0)
	X_test = X_data[half:]

	#RESHAPE FOR NN ENTRY
	X_train = X_train.reshape(-1,X_samples_shape[0],X_samples_shape[1])
	X_test = X_test.reshape(-1, X_samples_shape[0], X_samples_shape[1])
	Y_train = Y_train.astype(np.uint8)
	Y_test = Y_test.astype(np.uint8)


	return X_train, Y_train, X_test, Y_test


for i in range(trials):

	net1 = NeuralNet(
		layers=[('input', layers.InputLayer),
		        ('dense', layers.DenseLayer),
		        ('dropout2', layers.DropoutLayer),
		        ('output', layers.DenseLayer),
		        ],
		# input layer
		input_shape=(None, 1, X_samples_shape[1]),
		# dense
		dense_num_units=54,
		dense_nonlinearity=lasagne.nonlinearities.rectify,
		# dropout2
		dropout2_p=0.5,
		# output
		output_nonlinearity=lasagne.nonlinearities.softmax,
		output_num_units=2,
		# optimization method params
		update=nesterov_momentum,
		update_learning_rate=0.01,
		update_momentum=0.9,
		max_epochs=200,
	)

	print('--------- Trial #{} ------------'.format(i))

	X_train, Y_train, X_test, Y_test = load_dataset()
	# Train the network
	nn = net1.fit(X_train, Y_train)

	print("TRAINING DATA ACCURACY")

	preds = net1.predict(X_train)

	score = 0
	#print("TR || P")
	for x,y in zip(Y_train, preds):
		#print(str(x) + "  " + str(y))
		if x == y:
			score+=1

	accuracy_tr = score/len(Y_train)
	accuracy_train += accuracy_tr
	print('{} % \n'.format(accuracy_tr*100))

	print("TEST DATA ACCURACY")

	preds = net1.predict(X_test)

	score = 0
	#print("TS || P")
	for x,y in zip(Y_test,preds):
		#print(str(x) + "  " + str(y))
		if x == y:
			score+=1

	accuracy_ts = score / len(Y_test)
	accuracy_test += accuracy_ts
	print('{} %'.format(accuracy_ts*100))
	print('-------------------------------- \n')

print('TRAINING ACCURACY IS: {} %'.format(str(100 *accuracy_train/trials)))
print('TEST ACCURACY IS: {} %'.format(str(100* accuracy_test/trials)))