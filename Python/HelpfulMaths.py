#339A
'''
A. Helpful Maths
time limit per test2 seconds
memory limit per test256 megabytes
inputstandard input
outputstandard output
Xenia the beginner mathematician is a third year student at elementary school. She is now learning the addition operation.

The teacher has written down the sum of multiple numbers. Pupils should calculate the sum. To make the calculation easier,
 the sum only contains numbers 1, 2 and 3. Still, that isn't enough for Xenia. She is only beginning to count, 
 so she can calculate a sum only if the summands follow in non-decreasing order. For example, 
 she can't calculate sum 1+3+2+1 but she can calculate sums 1+1+2 and 3+3.

You've got the sum that was written on the board. Rearrange the summans and print the sum in such a way that Xenia can calculate the sum.

Input
The first line contains a non-empty string s — the sum Xenia needs to count. String s contains no spaces. 
It only contains digits and characters "+". Besides, string s is a correct sum of numbers 1, 2 and 3. String s is at most 100 characters long.

Output
Print the new sum that Xenia can count.
'''

n = input()
l=[]
l = n.split('+')

# print(l)
x=[]
while(len(l)>0):
    min=l[0]
    for i in range(len(l)):
        if(l[i]<min):
            min = l[i]
    x.append(min)
    l.remove(min)

# print(x)

for i in range(0,len(x)-1):
    print(x[i]+'+', end='')
print(x[len(x)-1])

