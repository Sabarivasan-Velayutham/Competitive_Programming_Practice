
#  ABC telecom services offers internet
# services in two bandwidths, 50Gbps and
# 100Gbps.

# Routers operated at 50 Gbps consumes
# 1Whrs and 100Gbps consumes 1.5Whrs. 

# These
# plans can ve availed at the cost of 500
# Rs per month and 750 Rs per month
# respectively. 

# ABC telecom has decided not
# to consume more than 300 Whrs per month.
# A cumulative speed of 1Tbps can be
# offered. What could be the maximum profit
# AB telecom can earn without violating the
# constaints. 

# 50x + 100y <= 1000 
# x + 2y <= 20 ---- 1 
# x + 1.5y <= 300
# 2x + 3y <= 600 --- 2 

import matplotlib.pyplot as plt

x=[i for i in range(30)]
y=[ (20-i)/2 for i in x ]
z=[ (600-2*i)/3 for i in x ]

x1=[0 for i in x]
y1=[0 for i in x]

plt.plot(x, y,label ='x + 2y <= 20 - line')
plt.plot(x, z,label ='2x + 3y <= 600 - line')
plt.plot(x, y1,label ='zero - line' ,color="red")
plt.plot(x1,x,label ='zero - line' ,color="red")

plt.fill_between(x, y, z, color='green',alpha=0.5)
plt.fill_between(x, y, x1, color='blue',alpha=0.5)

plt.xlabel("X - AXIS ")
plt.ylabel("Y - AXIS ")
plt.legend()
plt.show()

