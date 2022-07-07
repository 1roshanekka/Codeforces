#479A
a = int(input())
b = int(input())
c = int(input())

#bracket and sign
l = []
# + an *
l.append( (a+b)*c )
l.append( a+(b*c) )
# * and +
l.append( (a*b)+c )
l.append( a*(b+c) )
# * and * no need of bracket
l.append( a*b*c )
# + and + nop need of bracket
l.append( a+b+c )

print(max(l))
print(l)