"""
_summary_

Nested Lists 

Given the names and grades for each student in a Physics class of N students, store them in a nested list 
and print the names(s) of any student(s) having second lowest grade. 

Note: If there are multiple students witht the same grade, order their names alphabetically and print each name 
on a new line. 

Input Format 
The first line contains an integer, N , the number of students. 
The 2N subsequent lines describe each student over 2 lines; 
the first line contains a student's name, and the second line contains their grade. 

Contraints 
2<=N<=5 
There will always be one or more students having the second lowest grade. 

Output Format 
Print the name(s) of any student(s) having the second lowest grade in Physics; If there are multiple 
students, order their names alphabetically and print each one on a new line. 

Sample Input 
5 
Harry
37.21
Berry 
37.21
Tina 
37.2
Akriti 
41 
Harsh
39 

Sample Output 
Berry 
Harry  

Explanation 0
There are 5 students in this class whose names and grades are assembled to build the following list: 
python students = [['Harry', 37.21], ['Berry', 37.21],['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]] 

The lowest grade of 37.2 belongs to Tina. The second lowest grade of 37.21 belongs to both Harry and Berry 
so we order their names alphabetically and print each name on a new line. 
"""


Result = []
scorelist = []

if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        Result += [[name, score]]
        scorelist += [score]
        b = sorted(list(set(scorelist)))[1]
    for a, c in sorted(Result):
        if c == b:
            print(a)
