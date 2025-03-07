import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_gaussian_quantiles

def Neural_network_numpy():
    """
    Implements a simple neural network using NumPy for binary classification.  
    Generates a dataset, defines activation functions, initializes parameters, and trains the model  
    using backpropagation and gradient descent. The training error is plotted over iterations.  
    """
    
    # Generate a synthetic dataset for binary classification
    N = 1000
    gaussian_quantiles = make_gaussian_quantiles(
        mean=None,
        cov=0.1,
        n_samples=N,
        n_features=2,
        n_classes=2,
        shuffle=True,
        random_state=None)

    # Extract features (X) and labels (Y) from the dataset
    X, Y = gaussian_quantiles
    Y = Y[:, np.newaxis]  # Reshape Y to be a column vector

    # Print the shapes of X and Y to verify
    print(X.shape)
    print(Y.shape)

    # Plot the dataset to visualize the distribution
    plt.figure()
    plt.scatter(X[:, 0], X[:, 1], c=Y, s=40, cmap=plt.cm.Spectral)
    plt.show()
    
    # Define activation functions and their derivatives
    def sigmoid(x, derivate=False):
        if derivate:
            return np.exp(-x) / (np.exp(-x) + 1)**2  # Derivative of sigmoid
        else:
            return 1 / (1 + np.exp(-x))  # Sigmoid function

    def relu(x, derivate=False):
        if derivate:
            x[x <= 0] = 0
            x[x > 0] = 1
            return x  # Derivative of ReLU
        else:
            return np.maximum(0, x)  # ReLU function

    # Define the loss function (Mean Squared Error) and its derivative
    def mse(y, y_hat, derivate=False):
        if derivate:
            return (y_hat - y)  # Derivative of MSE
        else:
            return np.mean((y_hat - y)**2)  # MSE

    # Initialize the parameters (weights and biases) for the neural network
    def initialize_parameters_deep(layers_dims):
        parameters = {}
        L = len(layers_dims)
        for l in range(0, L - 1):
            # Initialize weights randomly between -1 and 1
            parameters['W' + str(l + 1)] = (np.random.rand(layers_dims[l], layers_dims[l + 1]) * 2) - 1
            # Initialize biases randomly between -1 and 1
            parameters['b' + str(l + 1)] = (np.random.rand(1, layers_dims[l + 1]) * 2) - 1
        return parameters

    # Define the training function that performs forward and backward propagation
    def train(x_data, learning_rate, params, training=True):
        # Forward propagation
        params['A0'] = x_data  # Input layer

        # First hidden layer
        params['Z1'] = np.matmul(params['A0'], params['W1']) + params['b1']
        params['A1'] = relu(params['Z1'])

        # Second hidden layer
        params['Z2'] = np.matmul(params['A1'], params['W2']) + params['b2']
        params['A2'] = relu(params['Z2'])

        # Output layer
        params['Z3'] = np.matmul(params['A2'], params['W3']) + params['b3']
        params['A3'] = sigmoid(params['Z3'])

        output = params['A3']

        if training:
            # Backpropagation
            # Gradients for the output layer
            params['dZ3'] = mse(Y, output, True) * sigmoid(params['A3'], True)
            params['dW3'] = np.matmul(params['A2'].T, params['dZ3'])

            # Gradients for the second hidden layer
            params['dZ2'] = np.matmul(params['dZ3'], params['W3'].T) * relu(params['A2'], True)
            params['dW2'] = np.matmul(params['A1'].T, params['dZ2'])

            # Gradients for the first hidden layer
            params['dZ1'] = np.matmul(params['dZ2'], params['W2'].T) * relu(params['A1'], True)
            params['dW1'] = np.matmul(params['A0'].T, params['dZ1'])

            # Gradient descent: Update weights and biases
            params['W3'] = params['W3'] - params['dW3'] * learning_rate
            params['W2'] = params['W2'] - params['dW2'] * learning_rate
            params['W1'] = params['W1'] - params['dW1'] * learning_rate

            params['b3'] = params['b3'] - (np.mean(params['dW3'], axis=0, keepdims=True)) * learning_rate
            params['b2'] = params['b2'] - (np.mean(params['dW2'], axis=0, keepdims=True)) * learning_rate
            params['b1'] = params['b1'] - (np.mean(params['dW1'], axis=0, keepdims=True)) * learning_rate

        return output

    # Define the architecture of the neural network
    layers_dims = [2, 6, 10, 1]  # Input layer: 2, Hidden layers: 6 and 10, Output layer: 1
    params = initialize_parameters_deep(layers_dims)
    errors = []

    # Training loop
    for _ in range(50000):
        output = train(X, 0.0001, params)
        if _ % 50 == 0:
            print(mse(Y, output))  # Print the loss every 50 iterations
            errors.append(mse(Y, output))  # Store the loss for plotting

    # Plot the training error over iterations
    plt.plot(errors)
    plt.show()

    # Test the trained model on new data
    data_test_x = (np.random.rand(1000, 2) * 2) - 1  # Generate random test data
    data_test_y = train(data_test_x, 0.0001, params, training=False)  # Make predictions
    y = np.where(data_test_y > 0.5, 1, 0)  # Convert probabilities to binary labels

    # Plot the predictions
    plt.figure()
    plt.scatter(data_test_x[:, 0], data_test_x[:, 1], c=y, s=40, cmap=plt.cm.Spectral)
    plt.show()
