
# Consider the following series: 0,0,2,1,4,2,6,3,8,4,10,5,12,6,14,7,16,8
# This series is a mixture of 2 series, all the odd terms in this series form even numbers
# in ascending order and every even terms is derived from the previous term using the formula (x/2).

# Write a program to find the nth term in this series.

# Input Format:
# The value of n is a positive integer that should be read from STDIN

# Output Format:
# The nth term that is to be calculated by the program should be written to STDOUT. 
# Other than the value of the nth term, no other characters /strings or message should be 
# written to STDOUT.


# Input:
# 10

# Output:
# 4


# n=10, the 10th term in the series is to be derived from the 9th term in the series.
# The 9th term is 8 so the 10th term is (8/2)=4. Only the value 4 should be printed to STDOUT.

n=int(input())
if n%2==1:
   print(n-1)
else:
   print((n-2)//2)