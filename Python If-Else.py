# Task
# Given an integer, , perform the following conditional actions:

# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird
# Input Format: A single line containing a positive integer,
#Constraints : ( 1<= N <= 100 )
# Output Format: Print Weird if the number is weird. Otherwise, print Not Weird.
# Sample Input : 3
# Sample Output : Weird
# Explanation 0: n=3,  n is odd and odd numbers are weird, so print Weird.
# Sample Input 1: 24
# Sample Output: Not Weird
# Explanation 1: n=24,  n>20  >> and n is even, so it is not weird.


import math
import sys
import os
import random
import re


if __name__ == '__main__':
    n = int(input().strip())
    if(n % 2 != 0):
        print('Weird')
    else:
        if(n >= 2 and n <= 5):
            print('Not Weird')
        elif(n >= 6 and n <= 20):
            print('Weird')
        elif(n > 20):
            print('Not Weird')
