import numpy as np

#microbial class
class GA2:
#init for the gene length, population size, and fitness function
    def __init__(self, n, p, fitFunc):
#population list
        self.pop = []
#gene list
        self.genes = []
#population value
        self.p = p
#gene length value
        self.n = n
#mutation probability
        self.m = 0.1
#recombination probability
        self.r = 0.5
#initial value for the bestfit
        self.bestFit = -np.inf
#fitness function
        self.fitFunc = fitFunc
#how to make the initial population(THE NEW GENE TYPE IS BETWEEN THE RANGE OF [-1,1] INSTEAD OF BEING BINARY)
        self.pop = np.random.rand(p, n)*2 - 1
#tournament method
    def tournament(self):
#variables to take a random gene
        a = np.random.randint(self.p)
        b = np.random.randint(self.p)
#variable to make the genes fight
        fit_win = self.fight(a,b)
#if the winners value is less than bestFit, value stays the same
        if fit_win < self.bestFit:
            return self.bestFit
#if not, the winners value is now the new value
        else:
            self.bestFit = fit_win
            return self.bestFit
#fighting method
    def fight(self, a, b):
#variables for genes to undergo the fitness function
        fit_a = self.fitFunc(self.pop[a])
        fit_b = self.fitFunc(self.pop[b])
#if gene a is better than gene b, it will be mutated
        if fit_a > fit_b:
#loser being recombined and mutated
            self.recombine(a,b)
            self.mutate(b)
#returning the winner
            return fit_a
#if gene b is better than gene a, it will be mutated
        else:
#loser being recombined mutated
            self.recombine(b,a)
            self.mutate(a)
#returning the winner
            return fit_b
#mutate method        
    def mutate(self, loser):
#looping through the genes length
        for gene in range(self.n):
#making the gene into a normal distribution
            self.pop[loser][gene] += np.random.normal(0.0, self.m)
#since this method of mutating has the possibility of going 
#over the range of [-1,1], conditionals are made
#if the gene composition is less than -1, it will become -1
            if self.pop[loser][gene] < -1:
                self.pop[loser][gene] = -1
#if the gene composition is greater than 1, it will become 1
            elif self.pop[loser][gene] > 1:
                self.pop[loser][gene] = 1
                
#recombining method
    def recombine(self,winner,loser):
#looping through the loser genes composition
        for gene in range(len(self.pop[loser])):
#if the probability is less than self.r, the loser gene will recombine 
            if np.random.rand() < self.r:
                self.pop[loser][gene] = self.pop[winner][gene]
#gets the best individual                
    def get_best(self):
#variables that can keep track of the score and position of individual
        best = 0
        location = 0 
#loops over the population 
        for i in range(len(self.pop)):
#variable that keeps track of every individuals score
            fit_ind = self.fitFunc(self.pop[i])
#if statement that if one individual has a better score than another, they will be swapped
            if fit_ind > best:
                best = fit_ind
#also keeps track of that individuals position 
                location = i
#returns that best individual of population
        return self.pop[location]
            
        
            