#200B
# from posixpath import split


n = int(input())

x = input()

dummyStr = x.split()
#split automatically defines variable as list type
OrangePercentage = []

for i in range(n):
    OrangePercentage.append(int(dummyStr[i]))

SumOfFraction = 0
for i in range(n):
    SumOfFraction += OrangePercentage[i]

print(SumOfFraction/n)

# print(dummyStr)