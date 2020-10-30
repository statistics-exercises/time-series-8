# Sample mean for poisson process

In the last exercise you should have seen that the dependence of the number of events with time is roughly linear, which makes total sense as we know that the expectation for a Poisson process is ![](https://render.githubusercontent.com/render/math?math=X(t)) is:

![](https://render.githubusercontent.com/render/math?math=\mathbb{E}[X(t)]=\lambda\t)

In these next two exercises we are going to revise the business of computing sample means and computing histograms one further time.  We will do this by writing a function to simulate a Poisson process over a period of time of fixed length and that will count the number of events that occur during this time period.  This function will thus generate a Poisson random variable.  In this first exercise we are then going to look at how the sample mean converges on the value for the true expectation for the random variable.  To complete the exercise you must therefore:

1. Write a function called `poisson` that takes in two parameters `lam` (the lambda parameter for your poisson process) and `time` (the amount of time that you would like to simulate for.  This function should return the number of events that occur during a time window of length `time`.  You will thus need to use the algorithm for generating a poisson random variable that you learned about in the previous exercise together with a while loop.
2. You need to set the variable called `expectation` equal to the value of the true expectation for this type of random variable.  
3. You need to write a loop that calls your poisson function multiple times and that computes the sample mean from these multiple samples.  When calling this function you should use the variables `lamd` and `time` as the two parameters of poisson function.  The values of the sample means with different sizes samples should be stored in a list called `average`.  Meanwhile, the list `indices` should store the number of random variables that each sample mean was computed from.

The final result from your program will be a graph that shows how the value of the sample mean changes as you increase the number of random variables from which it is computed. 

 
