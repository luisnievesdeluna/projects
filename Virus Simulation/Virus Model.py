
#imported modules for assignment
import city
import matplotlib.pyplot as plt
import numpy as np
#added a pre-determined size 
size = 10
#number for steps
num_steps = 2000

def first_function():
#populated a city with a 10x10 matrix and a threshold of .5
    #1)0.9, 0.05 
    #2) 0.05 0.05
    Bloomington = city.City(100,0.5, 0.1, 0.2)
#populated the city of Bloomington
    Bloomington.populate()
#showing the figure
    Bloomington.show("Starting(B)")
#making empty list so the "races" can step 
    result = []
    population = []
#for loops so they begin stepping in the city
    for step in range(num_steps):
        if step == 250:
            Bloomington.infect()
        for i in range((100)):
            
#step method so races can step
            Bloomington.step()
#appending the level of segregation to list
        result.append(Bloomington.measureSeg())
        population.append(Bloomington.measurePop())
#show segregated city 
    Bloomington.show("Ending(B)")
#saving the figure with the measurement of segregation
#labeling the x and y labels while saving it as well
    plt.xlabel("Segreation")
    plt.ylabel("Segregation index")
    plt.plot(result)
    plt.savefig("Segregation_Index(B).png")
    plt.figure()
    plt.plot(population)
    plt.savefig("population(B).png")
    plt.show()
    
    
    
    
def second_function():
#populated a city with a 10x10 matrix and a threshold of .5
    #1)0.9, 0.05 
    #2) 0.05 0.05
    Goshen = city.City(100, 0.5, 0.2, 0.4)
#populated the city of Bloomington
    Goshen.populate()
#showing the figure
    Goshen.show("Starting(G)")
#making empty list so the "races" can step 
    result = []
    population = []
#for loops so they begin stepping in the city
    for step in range(num_steps):
        if step == 250:
            Goshen.infect()
        for i in range((100)):
            
#step method so races can step
            Goshen.step()
#appending the level of segregation to list
        result.append(Goshen.measureSeg())
        population.append(Goshen.measurePop())
#show segregated city 
    Goshen.show("Ending(G)")
#saving the figure with the measurement of segregation
#labeling the x and y labels while saving it as well
    plt.xlabel("Segreation(G)")
    plt.ylabel("Segregation index(G)")
    plt.plot(result)
    plt.savefig("Segregation_Index(G).png")
    plt.figure()
    plt.plot(population)
    plt.savefig("population(G).png")
    plt.show()
    
    
    
    
def third_function():
#populated a city with a 10x10 matrix and a threshold of .5
    #1)0.9, 0.05 
    #2) 0.05 0.05
    Gary = city.City(100,0.5, 0.3, 0.6)
#populated the city of Bloomington
    Gary.populate()
#showing the figure
    Gary.show("Starting(GA)")
#making empty list so the "races" can step 
    result = []
    population = []
#for loops so they begin stepping in the city
    for step in range(num_steps):
        if step == 250:
            Gary.infect()
        for i in range((100)):
            
#step method so races can step
            Gary.step()
#appending the level of segregation to list
        result.append(Gary.measureSeg())
        population.append(Gary.measurePop())
#show segregated city 
    Gary.show("Ending(GA)")
#saving the figure with the measurement of segregation
#labeling the x and y labels while saving it as well
    plt.xlabel("Segreation(GA)")
    plt.ylabel("Segregation index(GA)")
    plt.plot(result)
    plt.savefig("Segregation_Index(GA).png")
    plt.figure()
    plt.plot(population)
    plt.savefig("population(GA).png")
    plt.show()
    


#calling the first function  
    
    
def fourth_function():
#populated a city with a 10x10 matrix and a threshold of .5
    #1)0.9, 0.05 
    #2) 0.05 0.05
    Elkhart = city.City(100,0.5, 0.4, 0.8)
#populated the city of Bloomington
    Elkhart.populate()
#showing the figure
    Elkhart.show("Starting(E)")
#making empty list so the "races" can step 
    result = []
    population = []
#for loops so they begin stepping in the city
    for step in range(num_steps):
        if step == 250:
            Elkhart.infect()
        for i in range((100)):
            
#step method so races can step
            Elkhart.step()
#appending the level of segregation to list
        result.append(Elkhart.measureSeg())
        population.append(Elkhart.measurePop())
#show segregated city 
    Elkhart.show("Ending(E)")
#saving the figure with the measurement of segregation
#labeling the x and y labels while saving it as well
    plt.xlabel("Segreation(E)")
    plt.ylabel("Segregation index(E)")
    plt.plot(result)
    plt.savefig("Segregation_Index(E).png")
    plt.figure()
    plt.plot(population)
    plt.savefig("population(E).png")
    plt.show()
    
    
first_function()
second_function()
third_function()
fourth_function()




