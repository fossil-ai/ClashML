import matplotlib
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import os
import gzip
import numpy as np
import scipy as sp
import theano
import lasagne
from lasagne import layers
from lasagne.updates import nesterov_momentum
from nolearn.lasagne import NeuralNet

X_samples_shape = (1,32)

def load_dataset():
	data = np.loadtxt('attr_data', delimiter=',')
	Y_train = data[:,data.shape[1] - 1]
	X_train = sp.delete(data, data.shape[1] - 1, axis=1)
	X_train = X_train.reshape(-1,X_samples_shape[0],X_samples_shape[1])
	Y_train = Y_train.astype(np.uint8)
	print(X_train)
	return X_train, Y_train

X_train, Y_train = load_dataset()

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
    dropout1_p=0.5,
    # dense
    dense_num_units=256,
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
    max_epochs=10,
    verbose=1,
    )
# Train the network
nn = net1.fit(X_train, Y_train)

preds = net1.predict(X_train)
print(preds)
