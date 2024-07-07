
# Description:
# Automated Teller Machine (ATM) is an electronic device that enables people to withdraw cash from
# their bank account every ATM has a limit for number of currency notes (say N), it can give at a
# time.

# A bank wants to design an ATM for school students the unique feature of this ATM would be that it
#  would always give maximum number of currency notes possible to make the students happy. Available
# denominations of the currency note in the ATM are 100, 200, 500, 1000


# Constraints:
# N<100

# Input Format:

# First line provides an integer N
# Second line provides an integer denoting the amount you want to withdraw in multiples of 100
# Third line provides an integer denominating the available currency notes of ₹100 into ATM
# Fifth line provides an integer denoting the available currency notes of ₹200 into ATM
# Fifth line provides an integer denoting the available currency notes of ₹500 into ATM
# Fifth line provides an integer denoting the available currency notes of ₹1000 into ATM


# Output:

# Output in containing the maximum number of currency notes possible for the desired withdrawal
# amount. Output should be 0 if transaction is not possible, for example if sufficient fund is not
# available in the ATM.


# Example:
# Input:

# 10
# 1300
# 10
# 10
# 10
# 10

# Output:
# 10

# Explanation:


# Here –
# 7*100 + 3*200 + 0*500 + 0*1000
# Hence maximum possible currency is  = 10

n = int(input())
amt = int(input())
n_100 = int(input())
n_200 = int(input())
n_500 = int(input())
n_1000 = int(input())

maxnotes = 0

for i in range(n_1000 + 1):
    for j in range(n_500 + 1):
        for k in range(n_200 + 1):
            for l in range(n_100 + 1):
                total = i*1000 + j*500 + k*200 + l*100
                if total == amt and i+j+k+l <= n:
                    maxnotes = max(maxnotes, i+j+k+l)

print(maxnotes)
