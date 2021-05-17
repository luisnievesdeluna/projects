#importing model
import numpy as np
#creating the neural network class
class CTRNN:
#init with a size variable for the amount of the neurons and step size for euler method
    def __init__(self, size=2, step_size=0.01):
        """
        Constructer that initializes a random network
        with unit time-constants and biases
        args = size:integer = network size
               step_size = Euler integration step size
        """
        self.size = size
        self.step_size = step_size
#taus, biases, and weights are equal to arrays to store values      
        self.taus = np.ones(size)
        self.biases = np.ones(size)
        self.weights = np.random.rand(size, size)

#states and outputs 
        self.states = np.random.rand(size)
        self.outputs = self.sigmoid(self.states)
#step method to get network to do oscillation, with user giving how many external outputs needed
    def step(self, external_inputs):
        """
        Euler stepping the network by self.step_size with provided inputs
        args = external_inputs:array[size,] = one float input per neuron
        """
#external outputs made into array
        external_inputs = np.asarray(external_inputs)

        # update states
#for loop to update the states of the neurons
        for i in range(self.size):
            total_input = external_inputs[i]
            
            for j in range(self.size):
#eulers method to get right output for neurons
                total_input += self.weights[i][j] * self.outputs[j]
            self.states[i] += self.step_size * (1/self.taus[i]) * (total_input - self.states[i])

# update outputs
        for i in range(self.size):
            self.outputs[i] = self.sigmoid(self.states[i] + self.biases[i])
            
        return list(self.outputs)

    def sigmoid(self, s):
        """
        Computes the sigmoid function on input array
        args = s:array of any Size
        output = sigmoid(s):array of same size as input
        """
        return 1 / (1 + np.exp(-s))

    def inverse_sigmoid(self, o):
        """
        Computes the inverse of the sigmoid function
        args = o:array of any size
        returns = inverse_sigmoid(o):array same size as o
        """
        return np.log(o / (1 - o))
