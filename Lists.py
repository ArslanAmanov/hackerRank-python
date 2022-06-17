"""
Lists 
Consider a list (list=[]) You can perform the following commands 
1. insert i e: Instert integer e at position i 
2. print: Print the list 
3. remove e: Delete the first occurance of integer e 
4. append e: Instert integer e at the end of the list 
5. sort: Sort the list 
6. pop: Pop the last element from the list 
7. reverse: Reverse the list  

Initialize your list and read in the value of n followed by n lines of commands where each commands will be of the 
7 types listed above. Iterate through each command in order and perform the corresponding operations on your list 

Input Format 
The first line contains an integer, n denoting the number of commands. 
Each line i of the n subsequent lines contains one of the commands described above. 

Contraints
The elements added to the list must be integers 

Output Format 
For each command of type print, print the list on a new line. 

Sample Output 0 
12 
insert 0 5 
insert 1 10 
insert 0 6 
print 
remove 6 
append 9 
append 1 
sort 
print
pop 
reverse 
print 

Sample Output 0 
[6,5,10]
[1,5,9,10]
[9,5,1]  
"""

if __name__ == '__main__':
    N = int(input())
    arr = []
    for i in range(0, N):
        inp = input().split()
        if inp[0] == "print":
            print(arr)
        elif inp[0] == "insert":
            arr.insert(int(inp[1]), int(inp[2]))
        elif inp[0] == "remove":
            arr.remove(int(inp[1]))
        elif inp[0] == "append":
            arr.append(int(inp[1]))
        elif inp[0] == "sort":
            arr.sort()
        elif inp[0] == "pop":
            arr.pop()
        else:
            arr.reverse()
