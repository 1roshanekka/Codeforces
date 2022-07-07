#131A
n = input()
lower = 0
upper = 0
for each in n:
    if( each.islower() ):
        lower += 1
    else:
        upper += 1

print(lower,'lower')
print(upper,'upper')

case1 = (upper==len(n))
case21 = (upper==(len(n)-1))
case22 = (lower==1)
case23 = n[0].islower()

if(case1):
    print(n.lower())
elif(case21 and case22 and case23):
    print(n.title())
else:
    print(n)