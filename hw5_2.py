import numpy as np
from scipy.optimize import minimize
import math
import random

#Using rosenbrock function as objective function becasue our project is not as good for this method
def obj(x):
    return (1-x[0])**2+100*(x[1]-x[0]**2)**2

#fitness function
def fit(f):
    delta_f = 1.1 * np.max(f) - 0.1 * np.min(f)
    F = (-f + delta_f) / max(1, (delta_f - np.min(f)))
    return F

#Roulette wheel (makes a random number between 0 and 1.
def rou():
    r = random.uniform(0, 1)
    return r

##Genetic algorithm##
######################
n = 2 #number of columbs (don't change)
m = 20 #number of parents (can change) (use 20)
xu = 3.0 #set upper bound search area
xl = 0.0  #set lower bound search area

p_k = [xl + np.random.random(n)*(xu - xl) for y in range(m)] #makes initial guesses (parents)
print("p_k (randomly generated parent points) =",'\n',p_k, '\n')

k = 0
while k < 2:
    ##Compute## (step 1 of 4)
    #Evaluates funcation at parent points
    f_k = np.array([obj(p) for p in p_k]) #function evaluations at p_k points
    print("f_k (functino evaluated at points) =",'\n',f_k,'\n')

    ##Select## (step 2 of 4)
    #Selects Np/2 parent pairs for crossover
    F = fit(f_k) #finds fitness of each function evaluation
    print("F (fitness) = ",'\n',F, '\n')


    S_j = np.array([(np.sum(F[0: j]) / np.sum(F)) for j in range(1,m+1)]) #this comprehension spaces out the roulette wheel pie slices
    print("S_j (roulette wheel spacing) =", S_j, '\n')

    #Roulette wheel and fill mating pool
    mate_pool = [0] * 0
    s = 0
    for s in range(m): #the spin
        spin = rou() #random number between 0 and 1
        i = 0
        while i < m: #select
            if spin < S_j[i]:
                mate_pool.append(p_k[i])
                break
            else:
                i = i + 1
        s = s + 1
    print("length mate pool",len(mate_pool))
    print(mate_pool)
    mate_pool = np.array((mate_pool))

    ##Generate## (step 3 of 4)
    #Generate a new population of Np offspring aka p_k+1
    p1 = np.array((mate_pool[np.argsort(mate_pool)[10:]])) #best 10 of mate pool
    p2 = np.array((mate_pool[np.argsort(mate_pool)[:10]])) #worst 10 of mate pool
    print("p1 =", len(p1))
    print("p2 =", len(p2))

    c1 = 0.5 * p1 + 0.5 * p2
    c2 = 2.0 * p1 + p2
    print("c1 =",'\n', len(c1))
    print("c2 =",'\n', len(c2))

    # ##Mutate## (step 4 of 4)
    # #Randomly mutate some points in the population
    x = np.array((c1, c2))
    #print("x =",'\n',x, '\n')


    i_delt = 0.005 #can play with later

    x_m = np.array(([x[0] + (random.uniform(0, 1) - 0.5)*i_delt for x[0] in range(m)], [x[1] + (random.uniform(0, 1) - 0.5)*i_delt for x[1] in range(m)] ))
    #     print("x_m",'\n',x_m)
    #
    p_k  = x_m
    k = k + 1
    ##We have incremented p_k and steps 1-4 will be repeated a set number of times and hopefully converge

##End of Genetic algorithem
# print() #f_star
# print() #x_star
print("best value",obj(p_k[0]))
