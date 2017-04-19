import numpy as np
import scipy as sp
import lasagne
from lasagne import layers
from lasagne.updates import nesterov_momentum
from nolearn.lasagne import NeuralNet

X_samples_shape = (1,32)

def load_dataset():
	data = np.loadtxt('attr_data', delimiter=',')
	np.random.shuffle(data)
	train_perc = 90
	half = int((data.shape[0]) * (train_perc/100))
	Y_train = data[:half,data.shape[1] - 1]
	Y_test = data[half :, data.shape[1] - 1]
	X_data = sp.delete(data, data.shape[1] - 1, axis=1)
	X_train = X_data[:half]
	X_test = X_data[half:]
	X_train = X_train.reshape(-1,X_samples_shape[0],X_samples_shape[1])
	X_test = X_test.reshape(-1, X_samples_shape[0], X_samples_shape[1])
	Y_train = Y_train.astype(np.uint8)
	Y_test = Y_test.astype(np.uint8)
	return X_train, Y_train, X_test, Y_test

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
    dropout1_p=0.25,
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
    max_epochs=256,
    verbose=1,
    )


X_train, Y_train, X_test, Y_test = load_dataset()
# Train the network
nn = net1.fit(X_train, Y_train)

print("CHECK AGAINST TRAINING DATA")

preds = net1.predict(X_train)

score = 0
print("TR || P")
for x,y in zip(Y_train, preds):
	print(str(x) + "  " + str(y))
	if x == y:
		score+=1

print(score/len(Y_train))

print("CHECK AGAINST TEST DATA")

preds = net1.predict(X_test)
prob = net1.predict_proba(X_test)

score = 0
print("TS || P")
for x,y in zip(Y_test,preds):
	print(str(x) + "  " + str(y))
	if x == y:
		score+=1

print(score/len(Y_test))

print(prob)
