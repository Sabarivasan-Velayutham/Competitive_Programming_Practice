
# Implement sum of even numbers and draw a graph for the number 
# of steps the algorithm takes to accomplish the task for different sizes of n. 
# Compare the graph with function n

import matplotlib.pyplot as plt

xpoints = [i for i in range(1,101)] 
ypoints = [j//2 for j in xpoints]


plt.plot(xpoints, ypoints,label ='steps-line')
plt.xlabel("Numbers")
plt.ylabel("No. of steps for adding even numbers ")
plt.legend()
plt.show()