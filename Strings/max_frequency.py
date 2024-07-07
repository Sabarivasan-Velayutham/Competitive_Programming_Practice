
# https://www.hackerrank.com/contests/ssn-acmw-contest-3/challenges/who-da-winner/problem

'''
Given a string s only consisting of lowercase letters ('a'-'z'), you have to print the character that occurs the most number of times in the string. In case of a tie, print the character that comes first in the alphabetical order.

Input Format
The first line contains the string s

Output Format
A single character

Write a python program for the above problem 
'''

s = input()  # read the input string

# create a dictionary to store the frequency of each character in the string
freq = {}
for c in s:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1

# find the character with the maximum frequency
max_freq = 0
max_char = 'a'  # initialize max_char to 'a'
for c in freq:
    if freq[c] > max_freq:
        max_freq = freq[c]
        max_char = c
    elif freq[c] == max_freq:
        max_char = min(max_char, c)

# print the character with the maximum frequency
print(max_char)
