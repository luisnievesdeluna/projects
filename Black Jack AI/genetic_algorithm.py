import random
from blackjack import *
from operator import itemgetter

def geneticAlgorithmTesting(generations, players, mutationWeight, topPlayerRatio):

    results = [] #stores each player's fitness score and genome
    playerGenomes = [] #stores all unique genomes for each player
    averageFitness = 0 #tracks Fitness of each overall run of the algorithm
    allFitness = []
    topPlayers = int(topPlayerRatio*players) #number of players in specified %
    numOfChildren = int(1/topPlayerRatio)
    numOfWins = 0
    wins = []

    #randomly fills genomes for first generation
    for i in range(players):
        genome = [] #stores unique genome values
        for j in range(6):       
            genome.append(random.random() * 2 - 1) #random values between -1 and 1
        playerGenomes.append(genome) #stores genome
        results.append([0, [0]]) #initializes results

    for i in range(generations): 

        #creates new generations 
        if i > 0:
            #slightly genetically mutates the top 10% from previous generation
            for j in range(topPlayers):
                child = results[j][1] #sets the child genome equal to its parent
                #mutates copied parent genome to create 10 unique children
                for k in range(numOfChildren):
                    for x in range(6):
                        child[x] = child[x] + (random.random() * mutationWeight - (mutationWeight * (1/2)))
                    playerGenomes[j*numOfChildren+k] = child #places child into new generation of playerGenomes

        #generates Players and executes hands
        for j in range(players):   
            #instantiates all objects necessary for game play
            player = Player(playerGenomes[j])
            game = Game()
            deck = Deck()
            deck.shuffle()

            #executes game and stores result 
            result = game.playSingleHand(deck, player)
            if result > 0:
                numOfWins += 1
            results[j] = [result, playerGenomes[j]]

        wins.append(numOfWins)
        numOfWins = 0

        #fitness analysis for AI 
        fitness = sum(v[0] for v in results)/len(results) #average Fitness for current generation       
        averageFitness += fitness #tracks Fitness for final calculation
        allFitness.append(fitness)

        #print(fitness) #useful to collect data
        results = sorted(results, key = itemgetter(0), reverse = True) #sorts results based off fitness (winnings)
        
    #print(allFitness)

    return averageFitness/generations

def playRandomGame(generations, players):
    results = [] #stores each player's fitness score and genome
    playerGenomes = []*players #stores all unique genomes for each player
    averageFitness = 0 #tracks Fitness of each overall run of the algorithm
    allFitness = []
    topPlayers = int(topPlayerRatio*players) #number of players in specified %
    numOfChildren = int(1/topPlayerRatio)
    numOfWins = 0
    wins = []
    lastGenerationResult = 0

    for i in range(generations): 

        #creates new generations 
        for k in range(players):
            genome = [] #stores unique genome values
            for j in range(6):       
                genome.append(random.random() * 2 - 1) #random values between -1 and 1
            if i == 0: 
                playerGenomes.append(genome)
            else:
                playerGenomes[k]= (genome) #stores genome
            results.append([0, [0]]) #initializes results

        #generates Players and executes hands
        for j in range(players):   
            #instantiates all objects necessary for game play
            player = Player(playerGenomes[j])
            game = Game()
            deck = Deck()
            deck.shuffle()

            #executes game and stores result 
            result = game.playSingleHand(deck, player)
            if result > 0:
                numOfWins += 1
            results[j] = [result, playerGenomes[j]]

        wins.append(numOfWins)
        numOfWins = 0
        #fitness for AI 
        fitness = sum(v[0] for v in results)/len(results) #average Fitness for current generation
        averageFitness += fitness #tracks Fitness for final calculation
        allFitness.append(fitness)

        #print(fitness) #useful to create graphics
        results = sorted(results, key = itemgetter(0), reverse = True) #sorts results based off fitness (winnings)
    print(wins)
    #print(allFitness)
    return averageFitness/generations

def geneticAlgorithm():

    results = [] #stores each player's fitness score and genome
    playerGenomes = [] #stores all unique genomes for each player
    averageFitness = 0 #tracks Fitness of each overall run of the algorithm
    allFitness = []
    numOfWins = 0
    wins = []

    #randomly fills genomes for first generation
    for i in range(250):
        genome = [] #stores unique genome values
        for j in range(6):       
            genome.append(random.random() * 2 - 1) #random values between -1 and 1
        playerGenomes.append(genome) #stores genome
        results.append([0, [0]]) #initializes results

    for i in range(1000): 

        #creates new generations 
        if i > 0:
            #slightly genetically mutates the top 10% from previous generation
            for j in range(125):
                child = results[j][1] #sets the child genome equal to its parent
                #mutates copied parent genome to create 10 unique children
                for k in range(2):
                    for x in range(6):
                        child[x] = child[x] + (random.random() * 5.00E-05 - (5.00E-05 * (1/2)))
                    playerGenomes[j*2+k] = child #places child into new generation of playerGenomes

        #generates Players and executes hands
        for j in range(250):   
            #instantiates all objects necessary for game play
            player = Player(playerGenomes[j])
            game = Game()
            deck = Deck()
            deck.shuffle()

            #executes game and stores result 
            result = game.playSingleHand(deck, player)
            if result > 0:
                numOfWins += 1
            results[j] = [result, playerGenomes[j]]

        wins.append(numOfWins)
        numOfWins = 0

        #fitness analysis for AI 
        fitness = sum(v[0] for v in results)/len(results) #average Fitness for current generation       
        averageFitness += fitness #tracks Fitness for final calculation
        allFitness.append(fitness)

        #print(fitness) #useful to collect data
        results = sorted(results, key = itemgetter(0), reverse = True) #sorts results based off fitness (winnings)

    return averageFitness/1000

### REGULAR GAME RUN ###
iterations = 5
overallFitness = 0
perfectOverallFitness = 0
for i in range(iterations):    
    currentFitness = geneticAlgorithm()
    overallFitness += currentFitness
print("----------------------------------------------------------")
print("\nGame Analysis")
print("Overall Winning Ratio:", overallFitness/iterations, "\n")
print("Parameters Used")
print("Generations: 1000")
print("Players per Generaton: 250")
print("Percent Used as Parents: 50%")
print("Mutation Weight: 5.00E-5\n")
print("----------------------------------------------------------")


# ### TESTING GAME RUN ###

#parameters for testing, make alterations here
#note: generations should be evenly divisible by 10
#current top parameters: g1000, p250, m5E-05, r0.5
generations = 1000
players = 250
mutationWeight = 5.00E-05
topPlayerRatio = 0.5
iterations = 1

#runs the alg and provides analysis 
overallFitness = 0
#perfectOverallFitness = 0
for i in range(iterations):    
    #currentFitness = geneticAlgorithm(generations, players, mutationWeight, topPlayerRatio)
    currentFitness = playRandomGame(generations, players)
    overallFitness += currentFitness
print("\n\nGame Analysis:")
print("----------------------------------------------------------")
print("Generations:", generations)
print("Players:", players)
print("Mutation Weight:", mutationWeight)
print("Top Player Ratio:", topPlayerRatio)
print("----------------------------------------------------------")
print("Overall Fitness of Above Parameters over", iterations, "Runs: ", overallFitness/iterations)



    

