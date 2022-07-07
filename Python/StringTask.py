#118A
'''
A. String Task
time limit per test2 seconds
memory limit per test256 megabytes
inputstandard input
outputstandard output
Petya started to attend programming lessons. On the first lesson his task was to write a simple program. The program was supposed to do the following: in the given string, consisting if uppercase and lowercase Latin letters, it:

deletes all the vowels,
inserts a character "." before each consonant,
replaces all uppercase consonants with corresponding lowercase ones.
Vowels are letters "A", "O", "Y", "E", "U", "I", and the rest are consonants. The program's input is exactly one string, it should return the output as a single string, resulting after the program's processing the initial string.

Help Petya cope with this easy task.

Input
The first line represents input string of Petya's program. This string only consists of uppercase and lowercase Latin letters and its length is from 1 to 100, inclusive.

Output
Print the resulting string. It is guaranteed that this string is not empty.
'''

n = input()
x = n.lower()
#A", "O", "Y", "E", "U", "I"
l=[]
f=[]
for j in range(len(x)):
    l.append(x[j])
# print(l)
# print(len(l))
x = len(l)

for j in range(x):
    c = len(l)
    for i in range(c):
        if(l[i]=='a'):
            l.remove(l[i])
        elif(l[i]=='o'):
            l.remove(l[i])
        elif(l[i]=='y'):
            l.remove(l[i])
        elif(l[i]=='e'):
            l.remove(l[i])
        elif(l[i]=='u'):
            l.remove(l[i])
        elif(l[i]=='i'):
            l.remove(l[i])
        if(len(l)<c):
            break

for i in range(len(l)):
    print('.'+ l[i], end='')


