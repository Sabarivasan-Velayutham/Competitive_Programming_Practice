
# Write a Program to read the upper and lower limits dynamically and print the count
# of numbers having unique digits.

# Constraints:
# Input Format:

# Integer – Lower Limit
# Integer – Upper Limit

# Output Format:
# Integer

# Example:
# Input:
# 10
# 15

# Output:
# 5

# Explanation:
# lower = 10
# upper = 15

# Numbers in this range are = 10, 11, 12, 13, 14, 15
# In this numbers with unique digits are = 10, 12, 13, 14, 15
# The count of which is 5
# And that is our output.

num1 = int(input())
num2 = int(input())

ans = 0
while (num1 <= num2):
    if len(set(str(num1))) == len(str(num1)):
        ans += 1
    num1 += 1
print(ans)
