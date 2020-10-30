import matplotlib.pyplot as plt
import numpy as np

def poisson( lam, time ) : 
  # Your function to simulate a poisson process for a fixed interval of time
  # goes here.
  
lamd = 2.0
time = 10.0
expectation =     ## Set the true value of the expectation here
indices, average = np.zeros(200), np.zeros(200) 
# Add code here to calculate the sample mean for a poisson process with parameter 
# lamd that is simulated for time seconds.  You should calculate the sample mean 
# for different sample sizes using the code that should now be familiar from other
# exercises.  The commands below will draw a graph of your sample mean as a function
# of the sample size.



# This will plot the graph for the data
plt.plot( indices, average, 'b.' )
plt.xlabel("Number of random variables")
plt.ylabel("Sample mean")
plt.plot( [0,200], [expectation,expectation], 'r-')
plt.savefig("average_exponential.png")
