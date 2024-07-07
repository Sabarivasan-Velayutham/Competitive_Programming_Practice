
# Implement Factorial using recursion and draw a graph for the number of steps
#  the algorithm takes to accomplish the task for different sizes of n.


import matplotlib.pyplot as plt

def factorial(n,count):
    count+=1
    if n==0:
        return count
    return factorial(n-1,count)

xpoints = [] 
ypoints = []

for i in range(1,50):
    count = 0  
    xpoints.append(i)
    ypoints.append(factorial(i,count))


plt.plot(xpoints, ypoints,label ='recursion-line')
plt.xlabel("Integer size")
plt.ylabel("No. of recursions")
plt.legend()
plt.show()