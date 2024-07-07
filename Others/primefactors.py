
# 4
# 1 1
# 2 1
# 4 6
# 3 5

from math import sqrt
# n is the number to be check whether it is prime or not
def prime(n):
    prime_flag = 0
    if(n > 1):
        for i in range(2, int(sqrt(n)) + 1):
            if (n % i == 0):
                prime_flag = 1
                break
        if (prime_flag == 0):
            return 1 
        else:
            return 0 
    else:
        return 0 


def print_factors(x):
   for i in range(2, x + 1):
       if x % i == 0:
           print(i,x//i)
           break

for t in range(int(input())):
    x,y=map(int,input().split())
    if x==1 and y ==1  :
        print(-1)
    elif x==1 and y>1 and prime(y):
        print(-1)
    elif x==1 and y>1 and not prime(y):
        print(1,y)
        if y%2==0:
            print(2,y//2)
        else :
            print_factors(y)
    else :
        print(0,x)
        print(1,x-1)

# 5
# 1 24
# 24 1 
# 1 35
# 1 17
# 3 30
