#importing modules
import numpy as np
import matplotlib.pyplot as plt
#perceptron class
class Perceptron:
#initializer that has weights and biases as arguements
    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias
#fire method that gets the output of said neuron
    def fire(self, inputs):
#score variable
        net = 0
#loops over the inputs that were given for the neuron 
        for i in range(len(inputs)):
#the score is added to variable along with the bias
            net += self.weights[i] * inputs[i]
        net += self.bias
#conditional statement that if the score is greater than 0, it will return a 1
#otherwise, it will return a -1
        if net > 0:
            return 1
        else:
            return -1
#neural network class   
class Neural_network:
#initializer that has the amount of neurons as an argument 
    def __init__(self, n):
        self.n = n
#empty lists that will act as layers
        self.layer1 = []
        self.layer2 = []
#appending the amount of neurons that the user wants (neurons already have set weights/biases)
        for i in range(self.n):
            self.layer1.append(Perceptron([-1,1], .5))
        for i in range(1):
            self.layer2.append(Perceptron([-1,1], .5))
#method that makes the neural network send the information forward
#the arguement is the inputs the user wants the network to have
    def forward(self, inputs):
#neurons having the set input while the last neuron has the pervious neurons output as inputs
        output1 = self.layer1[0].fire(inputs)
        output2 = self.layer1[1].fire(inputs)
        output3 = self.layer2[0].fire([output1,output2])
        #returning the final output
        return output3
    
