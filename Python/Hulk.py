#705A
n = int(input())


# if number odd - I hate that
# if number even - I love that

if(n%2!=0):
    a = 'I hate it'  #odd
else:
    a = 'I love it'  #even

for i in range(n,1,-1):
    # print(i)
    if(i%2!=0):
        a = 'I love that ' + a
    else:
        a = 'I hate that ' + a 
    # print(a)

print(a)

