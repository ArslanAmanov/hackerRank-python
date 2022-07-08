"""
_summary_
Task 
Designer Door Mat 

Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the
following specifications:
Mat size must be N x M . (N is an odd natural number, M and is 3 times N.)
The design should have 'WELCOME' written in the center.
The design pattern should only use | , . and - characters.

Size: 7 x 21
---------.|.---------
------.|..|..|.------
---.|..|..|..|..|.---
-------WELCOME-------
---.|..|..|..|..|.---
------.|..|..|.------
---------.|.---------
Size: 11 x 33
---------------.|.---------------
------------.|..|..|.------------
---------.|..|..|..|..|.---------
------.|..|..|..|..|..|..|.------
---.|..|..|..|..|..|..|..|..|.---
-------------WELCOME-------------
---.|..|..|..|..|..|..|..|..|.---
------.|..|..|..|..|..|..|.------
---------.|..|..|..|..|.---------
------------.|..|..|.------------
---------------.|.---------------

Input Format
A single line containing the space separated values of N and M.

Constraints 
5<N<101 
15<M<303

Output Format
Outpt the design pattern 

Sample Input 
9 27 
Sample Output 
------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------
Note:
More than 6 lines of code will result in a score of 0. Comment lines are counted. Blank lines are not
counted.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
N, M = map(int, input().split())
for i in range(1, N, 2):
    print(str('.|.' * i).center(M, '-'))
print('WELCOME'.center(M, '-'))
for i in range(N-2, -1, -2):
    print(str('.|.' * i).center(M, '-'))
