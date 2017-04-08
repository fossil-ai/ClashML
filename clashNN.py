import numpy as np
import scipy as sp
import lasagne
from lasagne import layers
from lasagne.updates import nesterov_momentum
from nolearn.lasagne import NeuralNet

X_samples_shape = (1,32)

def load_dataset():
	data = np.loadtxt('attr_data', delimiter=',')
	half = int((data.shape[0]) / 2)
	Y_train = data[:half,data.shape[1] - 1]
	Y_test = data[half :, data.shape[1] - 1]
	X_data = sp.delete(data, data.shape[1] - 1, axis=1)
	X_train = X_data[half:]
	X_test = X_data[:half]
	X_train = X_train.reshape(-1,X_samples_shape[0],X_samples_shape[1])
	X_test = X_test.reshape(-1, X_samples_shape[0], X_samples_shape[1])
	Y_train = Y_train.astype(np.uint8)
	Y_test = Y_test.astype(np.uint8)
	return X_train, Y_train, X_test, Y_test

X_train, Y_train, X_test, Y_test = load_dataset()

net1 = NeuralNet(
    layers=[('input', layers.InputLayer),
            ('dropout1', layers.DropoutLayer),
            ('dense', layers.DenseLayer),
            ('dropout2', layers.DropoutLayer),
            ('output', layers.DenseLayer),
            ],
    # input layer
    input_shape=(None, 1, X_samples_shape[1]),
    # dropout1
    dropout1_p=0.75,
    # dense
    dense_num_units=256,
    dense_nonlinearity=lasagne.nonlinearities.rectify,
    # dropout2
    dropout2_p=0.75,
    # output
    output_nonlinearity=lasagne.nonlinearities.softmax,
    output_num_units=2,
    # optimization method params
    update=nesterov_momentum,
    update_learning_rate=0.001,
    update_momentum=0.9,
    max_epochs=250,
    verbose=1,
    )
# Train the network
nn = net1.fit(X_train, Y_train)

print("CHECK AGAINST TRAINING DATA")

preds = net1.predict(X_train)

score = 0
for x,y in zip(preds,Y_train):
	print(x,y)
	if x == y:
		score+=1

print(score/len(Y_train))

print("CHECK AGAINST TEST DATA")

preds = net1.predict(X_test)

score = 0
for x,y in zip(preds,Y_test):
	print(x,y)
	if x == y:
		score+=1

print(score/len(Y_test))
