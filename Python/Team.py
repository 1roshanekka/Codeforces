#231A
'''
A. Team
time limit per test2 seconds
memory limit per test256 megabytes
inputstandard input
outputstandard output
One day three best friends Petya, Vasya and Tonya decided to form a team and take part in programming contests.
Participants are usually offered several problems during programming contests. 
Long before the start the friends decided that they will implement a problem if at least two of them are sure about the solution. 
Otherwise, the friends won't write the problem's solution.

This contest offers n problems to the participants. For each problem we know, 
which friend is sure about the solution. Help the friends find the number of problems for which they will write a solution.

Input
The first input line contains a single integer n (1 ≤ n ≤ 1000) 
— the number of problems in the contest. Then n lines contain three integers each, 
each integer is either 0 or 1. If the first number in the line equals 1, 
then Petya is sure about the problem's solution, otherwise he isn't sure. 
The second number shows Vasya's view on the solution, the third number shows Tonya's view. The numbers on the lines are separated by spaces.

Output
Print a single integer — the number of problems the friends will implement on the contest.

Examples
inputCopy
3
1 1 0
1 1 1
1 0 0
outputCopy
2
inputCopy
2
1 0 0
0 1 1
outputCopy
1
Note
In the first sample Petya and Vasya are sure that they know how to solve the first problem and all three of them know how to solve the second problem.
 That means that they will write solutions for these problems. Only Petya is sure about the solution for the third problem, but that isn't enough,
  so the friends won't take it.

In the second sample the friends will only implement the second problem, as Vasya and Tonya are sure about the solution.
'''

n = int(input())

# import pdb
# pdb.set_trace()
# d=[[1,1,0],[1,1,1],[1,0,0]]


def addAgreement(c):
    t = 0
    for j in range(len(c)):
        sum=0
        for k in range(3):
            #!!!!!!!!!!!!!!!
            #here '1' is str and dont ==1 that is int
            #we take here split which is str
            if(c[j][k]=='1'):
                sum = sum + 1
        if(sum>=2):
            t = t+1
    print(t)

def inputLines(b):
    l=[]
    m=[]
    for i in range(b):
        x = input()
        l = x.split(' ')
        m.append(l)
    return m

def checkLines(a):
    if(1<=a<=1000):
        return True
    else:
        return False

if(checkLines(n)):
    addAgreement((inputLines(n)))

# n = int(input())
# if(1<=n<=1000):
#     l=[]
#     m=[]
#     t = 0

#     for i in range(n):
#         x = input()
#         l = x.split(' ')
#         m.append(l)
#     print(m)

#     for j in range(len(m)):
#         sum=0
#         for k in range(3):
#             print(m[j][k],'look leme')
#             if(m[j][k]=='1'):
#                 sum = sum + 1
#         print(sum, 'sum')
#         if(sum>=2):
#             t = t + 1
#         print(t,'t')
#         print()
#     print(t)
    
