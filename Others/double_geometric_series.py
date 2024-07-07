
# Consider the following series: 1,1,2,3,4,9,8,27,16,81,32,243……

# This series is a mixture of 2 series : all the odd terms in this series form a
# geometric series and all the even terms form yet another geometric series.
# Write a program to find the Nth term in the series.

# Constraints
# The value of N will not exceed 30.

# Input Format:
# The value N is a positive integer that should be read from STDIN.

# Output Format:
# The Nth term that is calculated by the program should be written to STDOUT.
# Other than the value of the nth term, no other character/string or message 
# should be written to STDOUT.


# Example:
# Input:
# 16

# Output:
# 2187

# Explanation:
# The 16th value that will come within the series is 2187 and that is displayed 
# as the output.

n = int(input())

if n%2==1:
    print(2**((n+1)//2-1))
else :
    print(3**(n//2-1))