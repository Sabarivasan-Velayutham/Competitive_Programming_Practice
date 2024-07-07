
# Find minimum number of coins required to form any value between one to N both inclusive.
# Cumulative value of coins should not exceed N. Coin denominations are ₹1 to rupee and ₹5

# Consider value of N is 13 then the minimum number of coins required to formulate any value
# between 1 and 13 is 6. One ₹5, three ₹2 and two ₹1 coins are required to realise any value
# between one and 13. Hence this is the answer.

# However if one takes two ₹5 coins, one ₹2 coin and two ₹1 coin, then tpp all the values
# between 1 and 13 are achieved. But since the cumulative value of all the coin equals 14,
# i.e exceeds 13 this is not the answer.


# Input Format:
# A Single Integer value.

# Output:

# Four space separated integer values.

# 1st = Total number of coins
# 2nd = Number of 5 Rupee coins
# 3rd  = Number of 2 Rupee coins
# 4th  = Number of 1 Rupee coins

# Input:
# 13

# Output:
# 6 1 3 2

# Explanation:

# The minimum number of coins required is 6 within it:

# 5 Rupee = 1
# 2 Rupee =
# 1 Rupee = 2

number = int(input())
five = int((number - 4) / 5)
if ((number - 5 * five) % 2) == 0:
    one = 2
else:
    one = 1
two = (number - 5 * five - one) // 2
print(one + two + five, five, two, one)
