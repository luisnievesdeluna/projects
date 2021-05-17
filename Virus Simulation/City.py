import random
import numpy as np
import matplotlib.pyplot as plt

class City():

    def __init__(self, size, threshold, mortalityProb, recoverProb):
        self.size = size        # Size of the neighborhood measured along one dimension
        self.threshold = threshold*8
        self.pop = np.zeros((size,size)) # Houses in a neighborhood
        self.emptyProb = 0.1    # Probability that a house will be empty
        self.raceProb = 0.5     # Probability that a house will have one race
        self.recoverProb = recoverProb
        self.mortalityProb = mortalityProb
        self.dead = 0
        self.infected = 0
        self.binfected = 0
        self.ainfected = 0
        self.adead = 0
        self.bdead = 0

    def populate(self):
        # Populate the neighborhood at random
        for i in range(self.size):
            for j in range(self.size):
                # Flip a coin to see if the house is vacant or not
                if random.random() < self.emptyProb:
                    self.pop[i][j] = 0
                else:
                    # Flip another coin to see if the house will have race A or B living in it
                    if random.random() < self.raceProb:
                        self.pop[i][j] = 1
                    else:
                        self.pop[i][j] = -1
                        
  

    def show(self,title):
        plt.imshow(self.pop, interpolation="nearest", cmap="bwr")
        plt.xticks([])
        plt.yticks([])
        plt.title(title)
        plt.savefig(title)
        plt.show()
        plt.savefig(title + ".jpg")

    def step(self):
        # pick random house
        i,j = self.randomHouse()
        # find a place to move to if it's unhappy
        if self.pop[i][j] != 0.5 and self.pop[i][j] != -0.5:
            infected = self.numberInfected(i,j)
            if np.random.rand() < infected/8:
                if self.pop[i][j] == 1:
                    self.pop[i][j] = 0.5
                    self.ainfected += 1
                else:
                    self.pop[i][j] = -0.5
                    self.binfected += 1
                self.infected += 1
                    
        elif self.pop[i][j] != 0:
            if np.random.rand() < self.recoverProb:
                if self.pop[i][j] == 0.5:
                    self.pop[i][j] = 1
                    self.ainfected -= 1
                elif self.pop[i][j] == -0.5:
                    self.pop[i][j] = -1
                    self.binfected -= 1
                self.infected -= 1
                    
            elif np.random.rand() < self.mortalityProb:
                self.pop[i][j] = 0
                self.dead += 1
                self.infected -= 1
        if self.numberKin(i,j) < self.threshold and self.pop[i][j] != 0:
            self.move(i,j)
            
        
            
        return self.infected, self.dead, self.ainfected, self.binfected   
    
    def randomHouse(self):
        found = False
        while not found:
            i = random.randint(0,self.size-1)
            j = random.randint(0,self.size-1)
            if self.pop[i][j] != 0:
                found = True
        return i, j
    
    def infect(self):
        for k in range(self.size):
            i,j=self.randomHouse()
            if self.pop[i][j] == 1:
                self.pop[i][j] = 0.5
            elif self.pop[i][j] == -1:
                self.pop[i][j] = -0.5

    def randomVacant(self):
        found = False
        while not found:
            i = random.randint(0,self.size-1)
            j = random.randint(0,self.size-1)
            if self.pop[i][j] == 0:
                found = True
        return i, j

    def numberInfected(self, i, j):
        infected = 0
        # Check neighbors' race and count kin
        for x in range(i-1,i+2):
            ni = x%self.size
            for y in range(j-1,j+2):
                nj = y%self.size
                if self.pop[ni][nj] == 0.5 or self.pop[ni][nj] == -0.5:
                    infected += 1
        return infected


    def numberKin(self, i, j):
        myrace = self.pop[i][j]
        kin = 0
        # Check neighbors' race and count kin
        for x in range(i-1,i+2):
            ni = x%self.size
            for y in range(j-1,j+2):
                nj = y%self.size
                if myrace == self.pop[ni][nj]:
                    kin += 1
        return kin-1

    def move(self, i, j):
        newi,newj = self.randomVacant()
        self.pop[newi][newj] = self.pop[i][j]
        self.pop[i][j] = 0

    def measureSeg(self):
        # Should return a value between 0 and 1
        # Representing the average amount of kin neighbors in the pop
        avgkin = 0.0
        for i in range(self.size):
            for j in range(self.size):
                k = self.numberKin(i,j)
                avgkin += k/8.0
        return avgkin/(self.size*self.size)
    
    def measurePop(self):
        acount = 0
        bcount = 0
        for i in range(self.size):
            for j in range(self.size):
                if self.pop[i][j] == 1 or self.pop[i][j] == 0.5:
                    acount += 1
                elif self.pop[i][j] == -1 or self.pop[i][j] == -0.5:
                    bcount += 1
        return acount,bcount
                    

    

