
import matplotlib.pyplot as plt

def func(n,count):
    count+=1
    if n==0:
        return count
    return func(n-1,count)

xpoints = [i for i in range(1,101)] 
ypoints = [func(i,0) for i in range(1,101)]


plt.plot(xpoints, ypoints,label ='recursion-line')
plt.xlabel("Size of n")
plt.ylabel("No. of recursions")
plt.legend()
plt.show()
