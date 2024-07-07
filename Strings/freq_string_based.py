
# https://www.hackerrank.com/contests/ssn-acmw-contest-3/challenges/gunanicaa-election/problem


# Gunanicaa is contesting for AIT election. She asked Nithin Balaji's help to find people who is not supporting her. 
# Nithin sends her a password protected file with all the details of the members supporting and opposing her.

# The file can be opened by any string which has some character whose frequency is equal to the sum of frequency of 
# other characters in the string.

# Given a list of strings determine which of the following string can open the file and which cannot. Print YES if the 
# string can open the file or NO otherwise.

# Input Format
# The first line of the input contains an integer T denoting the number of test cases. Each of the next T lines 
# contains one string S consisting of lowercase latin letters.

# Constraints
# 1 ≤ T ≤ 10
# 1 ≤ length of S ≤ 10000

# Output Format
# Print YES if the string can open the file or NO otherwise.

# ----------
# ----------
# 3
# aaaaaaaaaaa
# abababab
# abcdefedcba

# NO
# YES
# NO

def can_open_file(password):
    freq = {}
    for char in password:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    total_freq = sum(freq.values())
    for char in freq:
        if freq[char] == total_freq - freq[char]:
            return "YES"

    return "NO"


# reading input T
T = int(input())

# iterating through each test case
for i in range(T):
    s = input().strip()
    print(can_open_file(s))

# The can_open_file function takes a string password as input and checks whether the file can be 
# opened with the given password or not. It does so by first calculating the frequency of each 
# character in the password and then iterating through each character to check whether its 
# frequency is equal to the sum of the frequencies of the other characters. If such a character 
# is found, the function returns "YES". Otherwise, it returns "NO".