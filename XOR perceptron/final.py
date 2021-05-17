from tkinter import *
import matplotlib.pyplot as plt
from GA2 import GA2
from Perceptron import Neural_network

#fitness function 
def XOR(genotype):
#score variable that will be used later for the final score
    score = 0
#making an initial network
    network = Neural_network(2)
#the weights and biases are set to the arguements indicies so they can be modified later
    network.layer1[0].weights = [genotype[0], genotype[1]]
    network.layer1[0].bias = genotype[2]
    network.layer1[1].weights = [genotype[3], genotype[4]]
    network.layer1[1].bias = genotype[5]
    network.layer2[0].weights = [genotype[6],genotype[7]] 
    network.layer2[0].bias = genotype[8]
#truth table values that are now being used as inputs 
    o1 = network.forward([-1,-1])
    o2 = network.forward([-1,1])
    o3 = network.forward([1,-1])
    o4 = network.forward([1,1])
#if the neural network gets the right output, the score will be increased by 10 (40 being the maximum score one can get)
    if o1 == -1:
        score += 10
        
    if o2 == 1:
        score += 10
        
    if o3 == 1:
        score += 10
        
    if o4 == -1:
        score += 10
        
    return score

class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):

        Label(self, text = "Select a value for genetic algorithm:").grid()

        self.level = StringVar()

        self.level.set("1000")

        Radiobutton(self, text = "1000", variable = self.level,     value = "1000").grid()

        Radiobutton(self, text = "3000", variable = self.level,  value = "3000").grid()

        Radiobutton(self, text = "5000", variable = self.level,  value = "5000").grid()

        Button(self, text = "Begin process!", command = self.value).grid()


    def value(self):
#looping the evolution algorithm 10 times
        for i in range(10):
#variable that has the indicies, population, and the fitness function as arguments
            test = GA2(9,100,XOR)
#empty list for results
            fit_list = []
#running the tournament method 5000 times
            for j in range(int(self.level.get())):
#appending and plotting said results
                fit_list.append(test.tournament())
            plt.plot(fit_list)
#getting the best individual from the get_best method in the GA script        
            best_g = test.get_best()
#making a new neural network
            network = Neural_network(2)
#making the weights and biases equal to best individual's properties 
            network.layer1[0].weights = [best_g[0], best_g[1]]
            network.layer1[0].bias = best_g[2]
            network.layer1[1].weights = [best_g[3], best_g[4]]
            network.layer1[1].bias = best_g[5]
            network.layer2[0].weights = [best_g[6],best_g[7]] 
            network.layer2[0].bias = best_g[8]
#truth table values being uses as inputs
            o1 = network.forward([-1,-1])
            o2 = network.forward([-1,1])
            o3 = network.forward([1,-1])
            o4 = network.forward([1,1])
#score variable     
            score = 0
#conditional statements. if they network gets the right outputs,
#the score gets increased by 10
            if o1 == -1:
                score += 10
                
            if o2 == 1:
                score += 10
                
            if o3 == 1:
                score += 10
                
            if o4 == -1:
                score += 10
#x, y, title labels for the figure and saving it
        plt.title("Neural Network optimization \n Max expected fitness is 40. reps:")
        plt.xlabel("Tournaments")
        plt.ylabel("Best Fitness")
        plt.savefig("Network.png")

# main
root = Tk()
root.title("Effecient Perceptron")
root.geometry("450x300")
app = Application(root)
root.mainloop()