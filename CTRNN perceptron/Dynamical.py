#importing modules
from ctrnn import CTRNN
import random
import math
import numpy as np
import matplotlib.pyplot as plt
from GA2 import GA2

#fitness function
def fitFunc(genotype): 
#initializing an object
    network = CTRNN()
#going through the taus, biases, and weights to provided optimal network
    network.taus = [(genotype[0] + 1) * 2 + 0.5 , (genotype[1] + 1) * 2 + 0.5]
    network.biases = [(genotype[2] * 5), (genotype[3] * 5)]
    network.weights = [[genotype[4] * 5, genotype[5] * 5], [genotype[6] * 5, genotype[7] * 5]]
#empty list to store the steps  
    outputs = []
    for i in range(5000):
        outputs.append(network.step([0,0]))
#variable to keep track of the score
    total_diff = 0    
#Getting the differences of the outputs
    for i in range(len(outputs)-1):
        diff1 = abs(outputs[i][0] - outputs[i+1][0])
        diff2 = abs(outputs[i][1] - outputs[i+1][1])
#adding differences to get score to measure optimization 
        total_diff += diff1 + diff2
        
    return total_diff
#main function 
def main():

#variable that has the indicies, population, and the fitness function as arguments
    test = GA2(8,100,fitFunc)
#empty list for results
    fit_list = []
#running the tournament method 500 times
    for i in range(7000):
#appending and plotting said results
        fit_list.append(test.tournament())
        print(i)
#tracking the value of the individual 
    plt.plot(fit_list)
#labels and saving the figure
    plt.title("Neural Network optimization")
    plt.xlabel("Tournament")
    plt.ylabel("Best Fitness")
    plt.savefig("Fitness.png")
#getting the best individual from the get_best method in the GA script        
    best_g = test.get_best()
#making a new neural network
    network = CTRNN()
#setting the taus, biases, and weights from best individual     
    network.taus = [(best_g[0] + 1) * 2 + 0.5 , (best_g[1] + 1) * 2 + 0.5]
    network.biases = [(best_g[2] * 5), (best_g[3] * 5)]
    network.weights = [[best_g[4] * 5, best_g[5] * 5], [best_g[6] * 5, best_g[7] * 5]]
#empty list to keep track of time and outputs
    time = []   
    outputs = []
    for i in range(5000):
        outputs.append(network.step([0,0]))
        time.append(i)
#converting to array to plot
    outputs = np.array(outputs)
    plt.figure()
    for i in range(2):
#plotting the network to wave
#labels and saving the figure
        plt.plot(time, outputs[:,i])
    plt.title("Activity")
    plt.xlabel("Time")
    plt.ylabel("Outputs")
    plt.savefig("Network.png")
    plt.show()
#calling the main
main()   

