import numpy as np

def heading(title="Fibonacci__Series", length=50, char="-"):
    """This function prints a centered title with a border of the specified character"""
    print(str(title).center(length, char))

def fibonacci_series(n):
    """coding the series of fibonacci with numpy"""
    F_S = np.zeros(n, dtype=int)#In this line of code we are make an array with the data type of int.
    F_S[0], F_S[1] = 0, 1#The first number of the Fibonacci sequence is 0.,The second number of the Fibonacci sequence is 1.
    for i in range(2, n):# this loop will start from 2nd index upto n-1.
        F_S[i] = F_S[i-1] + F_S[i-2]
    return F_S#return the sum of n-1 and n-2.

n= 5
heading()
print("Output : ",fibonacci_series(n))
