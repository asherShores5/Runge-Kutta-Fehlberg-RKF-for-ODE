#Asher Shores
#Dr. Ricardo Citro
#CST-305: Project 2 – Runge-Kutta-Fehlberg (RKF) for ODE
#This is my own work


#Differential Equation: dy/dx = (-y + np.exp(x))

#Implementation
#Use numerical and odeint based methods to create and solve differential equations.
#Solve dy/dx using runge kutta and compare results.
#Show time for each solution
#Show percent error

import numpy as np                  #import lib numpy as np for math
import matplotlib.pyplot as plt     #import lib matplotlib to graph
import time                         #including time to time the functions
from scipy.integrate import odeint  #importing scipy to use ODEINT

#ODE function for ODEINT

def fn1(y, x):                   #creating a function to return the ODE value at specific points
    return (-y + np.log(x))    #returning the value of the ODE



#ODE function for Runge-Kutta

def fn(x, y):   #defining a model to return the ODE
    return (-y + np.log(x))    #returns value of the ODE


#Runge-Kutta function

def rk(Xn, Yn, h):    #calculates each k, t4, returns Yn+1, input Xn, Yn, h
    k1 = fn(Xn, Yn)                         #calculating k1
    k2 = fn((Xn + (h/2)), (Yn + (h/2)*k1))  #calculating k2
    k3 = fn((Xn + (h/2)), (Yn + (h/2)*k2))  #calculating k3
    k4 = fn((Xn + h), (Yn + h*k3))          #calculating k4

    t4 = T4(k1, k2, k3, k4)                 #calculating t4

    Yn1 = Yn + h * t4                       #calculating Yn+1 from t4
    return Yn1                              #returning Yn+1


#T4 function

def T4(k1, k2, k3, k4):   #Offputs t4 caclulation to this function
    return ((1/6)*(k1 + 2*k2 + 2*k3 + k4))  #returns value of t4


#initial conditions 

x0 = 2          #setting x0 to 2
y0 = 1          #setting y0 to 1
h = 0.3         #setting h to 0.3
n = 1000       #setting the number of times to run

# Creating and storing values using RK method

yValuesRK = []              #Array for all y values
xValuesRK = []              #Array for all x values

yValuesRK.append(y0)        #adding y0 (inital) to the yValuesRK array
xValuesRK.append(x0)        #adding x0 (inital) to the xValuesRK array

Xn1 = x0                    #setting Xn1 to x0 to use in the for loop
Yn1 = y0                    #setting Yn1 to y0 to use in the for loop
#These are the first values for the loop

t1 = time.time()            #finding the time before runge-kutta
#allows for calculation of computational time

for i in range(1, n):       #finding the RK values n (times to run) times
    Yn1 = rk(Xn1, Yn1, h)   #setting the next y to the RK value based on the previous y
    Xn1 = x0 + (i * h)      #setting the x to the correct x based on the step
    yValuesRK.append(Yn1)   #appending the new y value to the array
    xValuesRK.append(Xn1)   #appending the new x value to the array
t2 = time.time()            #finding the time after runge-kutta


#Solving ODE using odeint to compare to RK method

t3 = time.time()                                #finding the time before ODEINT
xValsSci = np.linspace(1, (int)(n * h) + 1, n)  #creating the linear space of x values for ODEINT
yValsSci = odeint(fn1, y0, xValsSci)             #using ODEINT to solve the equation for the preset values
t4 = time.time()                                #finding the time after ODEINT


#time analysis

print("\nTotal time for Runge-Kutta: ", (t2-t1))#displaying the total time for Runge-Kutta
print("Total time for ODEINT: ", (t4-t3))       #displaying the total time for ODEINT


#Final Solutions

print("\nODEint Solution:            ", yValsSci[-1])           #ODEINT  solution
print("Runge-Kutta Solution:        ", yValuesRK[-1], "\n")     #Runge-Kutta  solution

count = 0
for i in range(0, 6):
    print("Value of Y", count, "is: ",  yValuesRK[i])
    count = count +1
    
#Percent error
err = 0                                                                #error variable
errRange = []                                                          #array to for error vals
errSpace = np.linspace(1, (int)(n * h) + 1, 41)                        #error space for error analysis
for i in range((int)(n * h) + 1):                                      #for loop to run through every all x values
    err += (np.abs(yValuesRK[i] - yValsSci[i])/yValsSci[i]) * 100      #sum all the error values for percent error
    errRange.append((np.abs(yValuesRK[i] - yValsSci[i])/yValsSci[i]) * 100)    #appending the error at point i to the array
print("\nAverage Error is", err/((int)(n * h) + 1), "%\n")                     #print the total error divided by the total number of x values


    
plt.title("Runge-Kutta Analysis")                           #Title
plt.xlabel("x")                                             #labele x-axis
plt.ylabel("y")                                             #labele - y-axis
plt.plot(xValuesRK, yValuesRK, 'r-', label = "Runge Kutta") #set RK color
plt.legend()                                                #Legend
plt.show()                                                  #plot

plt.title("ODEINT")                                         #Title
plt.xlabel("x")                                             #labele x-axis
plt.ylabel("y")                                             #labele y-axis
plt.plot(xValsSci, yValsSci, 'b-', label = "ODEint")        #ODEint color
plt.legend()                                                #Show legend
plt.show()                                                  #graph

plt.title("ODEINT and Runge-Kutta Analysis")                #Title
plt.xlabel("x")                                             #lable x
plt.ylabel("y")                                             #labele y
plt.plot(xValuesRK, yValuesRK, 'r-', label = "Runge Kutta") #plotting x,y for RK (blue)
plt.plot(xValsSci, yValsSci, 'b-', label = "ODEINT")        #plotting x,y for ODEint (red)
plt.legend()                                                #Legend
plt.show()                                                  #graph

