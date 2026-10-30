import numpy as np



# Follow the tasks below to practice basic Python concepts.
# Write your code in between the dashed lines.
# Don't import additional packages. Numpy suffices.

# Task 1: 
# Instructions:
#Write a function that takes one numeric argument as input. 
#If the number is larger than zero, the function should return 1, otherwise is should return -1.
#The name of the function should be step

# Your code here:
# -----------------------------------------------

def step(x):

    if x>0:
        return 1
    else:
        return -1
    

step(4)

# -----------------------------------------------


# Task 2:
# Instructions:
#Write a function that takes in two arguments: a numpy array, and an integer (call argument "cutoff" and set default to 0).
#The function should return a numpy array of the same length, with all elements smaller than the cutoff being set to cutoff).
#The name of the function should be ReLu


# Your code here:
# -----------------------------------------------
def ReLu(x, cutoff=0):
    y = x.copy()
    for i in range(len(y))  :
        if y[i] <cutoff:
            y[i]=cutoff

    return y

test= np.array([0,2,4,-4,1])

ReLu(test)
# -----------------------------------------------


# Task 3:
# Instructions:
#Write a function that takes in a two-dimensional numpy array of size (n, p) and a one-dimensional numpy array of size p.
#The function should start by multiplying the two numpy arrays (matrix multiplication).
#Next, apply the ReLu function from above to the resulting matrix and return the result.
#Name the function neural_net_layer

# Your code here:
# -----------------------------------------------

def neural_net_layer(array1,array2):
   
   multiplied= np.multiply(array1 ,array2)

   result = ReLu(multiplied)

   return result

test1= np.array([0,2,4,-4,1])
test2=np.array([[0,2,4,-4,1],[6,7,8,3,1]])

np.multiply(test1 ,test2)

neural_net_layer(test1,test2)
# ------------------------------------------